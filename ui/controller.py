""" Houses UIController class """
from PyQt6.QtWidgets import (
    QWidget,
    QStackedLayout,
    QVBoxLayout
)
from PyQt6.QtCore import QCoreApplication

from logs import Logger
from spotify import SpotifyDataFetcher
from models import Data
from ui import LoginScreen, DataSelectionScreen, ProgressDialog, ChoiceScreen, ExportScreen
from serializer import DataSerializer
from applemusic import AppleMusicInteractor


class UIController(QWidget):
    """ Main UI and screen controller """

    def __init__(self):
        self.spotify = None
        self.data = None
        self.logger = Logger()
        self.serializer = DataSerializer()
        self.applemusic = AppleMusicInteractor()

        super().__init__()
        self.setFixedSize(750, 750)
        self.setWindowTitle("Spotify to Apple Music Migrator")

        self.layout = QVBoxLayout(self)
        self.stack = QStackedLayout()
        self.layout.addLayout(self.stack)

        self.login_screen = LoginScreen()
        self.stack.addWidget(self.login_screen)
        self.choice_screen = ChoiceScreen()
        self.stack.addWidget(self.choice_screen)
        self.data_screen = DataSelectionScreen()
        self.stack.addWidget(self.data_screen)
        self.export_screen = ExportScreen()
        self.stack.addWidget(self.export_screen)

        self.login_screen.login_button.clicked.connect(self.handle_login)
        self.choice_screen.import_button.clicked.connect(self.handle_import)
        self.choice_screen.export_button.clicked.connect(self.handle_export)
        self.data_screen.fetch_data_button.clicked.connect(self.fetch_data)
        self.export_screen.export_data_button.clicked.connect(self.export_data)

        self.data_screen.back_button.clicked.connect(self.return_to_choice)
        self.export_screen.back_button.clicked.connect(self.return_to_choice)

        self.load_styles()

    def handle_login(self) -> None:
        """ Create the spotify object to trigger authentication """
        self.spotify = SpotifyDataFetcher()
        if self.spotify.auth_manager.get_cached_token():
            # If successful, move to next screen
            self.stack.setCurrentWidget(self.choice_screen)

    def handle_import(self) -> None:
        """ Display the import screen based on the user's choice """
        self.stack.setCurrentWidget(self.data_screen)

    def handle_export(self) -> None:
        """ Display the export screen based on the user's choice """
        self.stack.setCurrentWidget(self.export_screen)

    def return_to_choice(self) -> None:
        self.stack.setCurrentWidget(self.choice_screen)

    def fetch_data(self) -> None:
        """ Ask SpotifyDataFetcher to fetch requested data, then we serialize the data """
        selected_options = self.data_screen.get_selected_options()

        progress_dialog = ProgressDialog(parent=self)
        progress_dialog.show()
        QCoreApplication.processEvents()

        if selected_options['playlists']:
            playlists = self.spotify.fetch_playlists()
            self.logger.log("INFO", "Fetched playlists")
        else:
            playlists = None
        QCoreApplication.processEvents()
        progress_dialog.update_logs()

        if selected_options['liked songs']:
            albums = self.spotify.fetch_albums()
            self.logger.log("INFO", "Fetched albums")
        else:
            albums = None
        QCoreApplication.processEvents()
        progress_dialog.update_logs()

        if selected_options['liked songs']:
            liked_songs = self.spotify.fetch_saved_tracks()
            self.logger.log("INFO", "Fetched liked songs")
        else:
            liked_songs = None
        QCoreApplication.processEvents()
        progress_dialog.update_logs()

        if selected_options['artists']:
            followed_artists = self.spotify.fetch_followed_artists()
            self.logger.log("INFO", "Fetched followed artists")
        else:
            followed_artists = None
        QCoreApplication.processEvents()
        progress_dialog.update_logs()

        self.data = Data(playlists, albums, liked_songs, followed_artists)

        self.logger.log("INFO", "Data fetch complete")
        QCoreApplication.processEvents()
        progress_dialog.update_logs()
        progress_dialog.unlock()
        progress_dialog.exec()

        self.serialize_data()

    def export_data(self) -> None:
        """ Export data into Apple Music """
        if not self.data:
            self.data = self.serializer.load_from_pickle(self.data)
        if not self.data:
            return

        selected_options = self.export_screen.get_selected_options()

        progress_dialog = ProgressDialog(parent=self)
        progress_dialog.show()
        QCoreApplication.processEvents()

        if selected_options['playlists'] and self.data.playlists:
            playlists = self.data.playlists
            for playlist in playlists:
                self.applemusic.create_playlist(playlist.name)
                self.applemusic.search_for_playlist(playlist)
            self.logger.log("INFO", "Exported playlists")
        else:
            playlists = None
        QCoreApplication.processEvents()
        progress_dialog.update_logs()

        if selected_options['liked songs'] and self.data.albums:
            albums = self.data.albums
            for album in albums:
                for track in album.tracks:
                    self.applemusic.search_track(track)
            self.logger.log("INFO", "Exported albums")
        else:
            albums = None
        QCoreApplication.processEvents()
        progress_dialog.update_logs()

        if selected_options['liked songs'] and self.data.liked_songs:
            liked_songs = self.data.liked_songs
            for track in liked_songs:
                self.applemusic.search_track(track)
            self.logger.log("INFO", "Exported liked songs")
        else:
            liked_songs = None
        QCoreApplication.processEvents()
        progress_dialog.update_logs()

        self.logger.log("INFO", "Data fetch complete")
        QCoreApplication.processEvents()
        progress_dialog.update_logs()
        progress_dialog.unlock()
        progress_dialog.exec()

    def serialize_data(self) -> None:
        """ Export all data to both pickle and human-readable formats """
        self.serializer.save_to_json(self.data)
        self.serializer.save_to_pickle(self.data)
        self.serializer.save_to_markdown(self.data)

    def load_styles(self) -> None:
        """ Load and apply CSS stylesheet """
        with open("./assets/styles.css", "r", encoding='utf8') as file:
            self.setStyleSheet(file.read())

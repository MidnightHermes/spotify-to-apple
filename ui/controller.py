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
from ui import LoginScreen, DataSelectionScreen, ProgressDialog
from serializer import DataSerializer


class UIController(QWidget):
    """ Main UI and screen controller """

    def __init__(self):
        self.spotify = None
        self.data = None
        self.logger = Logger()
        self.serializer = DataSerializer()

        super().__init__()
        self.setFixedSize(750, 750)
        self.setWindowTitle("Spotify to Apple Music Migrator")

        self.layout = QVBoxLayout(self)
        self.stack = QStackedLayout()
        self.layout.addLayout(self.stack)

        self.login_screen = LoginScreen()
        self.stack.addWidget(self.login_screen)
        self.data_screen = DataSelectionScreen()
        self.stack.addWidget(self.data_screen)

        self.login_screen.login_button.clicked.connect(self.handle_login)
        self.data_screen.fetch_data_button.clicked.connect(self.fetch_data)

        self.load_styles()

    def handle_login(self) -> None:
        """ Create the spotify object to trigger authentication """
        self.spotify = SpotifyDataFetcher()
        if self.spotify.auth_manager.get_cached_token():
            # If successful, move to next screen
            self.stack.setCurrentWidget(self.data_screen)

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

        # TODO: Change this when actual export page is done
        self.export_data()

    def export_data(self):
        """ Export all data to both pickle and human-readable formats """
        self.serializer.save_to_json(self.data)
        self.serializer.save_to_pickle(self.data)
        self.serializer.save_to_markdown(self.data)

    def load_styles(self) -> None:
        """ Load and apply CSS stylesheet """
        with open("./assets/styles.css", "r", encoding='utf8') as file:
            self.setStyleSheet(file.read())

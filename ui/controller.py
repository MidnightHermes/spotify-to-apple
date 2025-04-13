""" Houses UIController class """
from PyQt6.QtWidgets import (
    QWidget,
    QStackedLayout,
    QVBoxLayout
)

from spotify import SpotifyDataFetcher
from models import Data
from ui.screens.login import LoginScreen
from ui.screens.data_select import DataSelectionScreen


class UIController(QWidget):
    """ Main UI and screen controller """

    def __init__(self):
        self.spotify = None
        self.data = None

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
            print("AUTHENTICATION SUCCESS!")
            # If successful, move to next screen
            self.stack.setCurrentWidget(self.data_screen)

    def fetch_data(self) -> None:
        """ Ask SpotifyDataFetcher to fetch requested data """
        selected_options = self.data_screen.get_selected_options()
        if self.spotify:
            playlists = self.spotify.fetch_playlists if selected_options['playlists'] else None
            albums = self.spotify.fetch_albums if selected_options['liked songs'] else None
            liked_songs = self.spotify.fetch_saved_tracks if selected_options['liked songs'] else None
            followed_artists = self.spotify.fetch_followed_artists if selected_options['artists'] else None

            self.data = Data(playlists, albums, liked_songs, followed_artists)
        else:
            # TODO: Handle error
            pass

    def load_styles(self) -> None:
        """ Load and apply CSS stylesheet """
        with open("./assets/styles.css", "r", encoding='utf8') as file:
            self.setStyleSheet(file.read())

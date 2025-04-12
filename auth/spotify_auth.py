""" House the SpotifyAuthManager object """
from spotipy.oauth2 import SpotifyOAuth  # type: ignore
from constants import SPOTIFY_SCOPES


class SpotifyAuthManager:
    """ Manages authorization for Spotify """

    def __init__(self):
        self.auth_manager = None
        self.authorize()

    def authorize(self) -> None:
        """ Creates SpotifyOAuth object from spotipy to implement Authorization Code Flow """
        self.auth_manager = SpotifyOAuth(scope=SPOTIFY_SCOPES, open_browser=self.open_browser())

    def get_auth_manager(self) -> SpotifyOAuth:
        """ Return the object's auth manager """
        return self.auth_manager

    def open_browser(self) -> bool:
        """ Return whether to open the browser based on whether the user has authenticated """
        # Check whether the auth_manager has already been created
        if self.auth_manager:
            # If it has, check if a token has been cached
            return not self.auth_manager.get_cached_token()
        # Otherwise, we should open the browser
        return True

""" House the SpotifyAuthManager object """
import sys
from spotipy.oauth2 import SpotifyOAuth  # type: ignore

from constants import SPOTIFY_SCOPES
from logs import Logger


class SpotifyAuthManager:
    """ Manages authorization for Spotify """

    _instance = None
    _initialized = False

    def __new__(cls):
        """ Ensure Singleton, only one instance may exist """
        if not hasattr(cls, 'instance'):
            cls.instance = super(SpotifyAuthManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not self.__class__._initialized:
            self.auth_manager = None
            self.logger = Logger()
            self.authorize()
            self.__class__._initialized = True

    def authorize(self) -> None:
        """ Creates SpotifyOAuth object from spotipy to implement Authorization Code Flow """
        try:
            self.auth_manager = SpotifyOAuth(scope=SPOTIFY_SCOPES, open_browser=self.open_browser())
            self.logger.log("INFO", "Successfully authorized")
        except Exception as e:
            self.logger.log("FATAL", f"Failed to authorize: {e}")
            sys.exit(1)

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

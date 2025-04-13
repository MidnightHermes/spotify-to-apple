""" Houses the AppleMusicInteractor class """
import string

import applescript  # type: ignore

from models import Track, Playlist
from logs import Logger


class AppleMusicInteractor:
    """ Wrapper for AppleScript scripts to interact with the local Apple Music app """

    def __init__(self):
        self.logger = Logger()

    def create_playlist(self, name: str) -> None:
        """ Uses AppleScript to tell the Music app to create a new playlist with a given name """
        try:
            applescript.tell.app("Music", f'make new user playlist with properties {{name: "{name}"}}')
            self.logger.log("INFO", f"AppleScript successfully created playlist {name}")
        except Exception as e:
            self.logger.log("WARNING", f"AppleScript failed to create playlist {name}: {e}")

    def search_for_playlist(self, playlist: Playlist) -> None:
        """ Uses AppleScript to search for multiple songs to add into the playlist """
        for track in playlist.tracks:
            self.search_track(track)

    def search_track(self, track: Track) -> None:
        """ Uses AppleScript to open the Music app then simulate keyboard input to search a song """
        try:
            with open('./applemusic/scripts/search_track.applescript', 'r', encoding='utf8') as fp:
                primary_artist = ''.join(char for char in track.artists[0] if char not in string.punctuation)
                script = f'set songName to "{track.name} {primary_artist}"' + fp.read()
        except Exception as e:
            self.logger.log("WARNING", f"Failed to load AppleScript script to search for tracks: {e}")
        try:
            applescript.run(script)
            self.logger.log("INFO", "AppleScript successfully searched for a track")
        except Exception as e:
            self.logger.log("WARNING", f"AppleScript failed to search for a track: {e}")

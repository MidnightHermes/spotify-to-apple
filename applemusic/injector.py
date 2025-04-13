""" Houses the AppleMusicInteractor class """
import applescript  # type: ignore

from models import Track, Playlist


class AppleMusicInteractor:
    """ Wrapper for AppleScript scripts to interact with the local Apple Music app """

    def create_playlist(self, name: str) -> None:
        """ Uses AppleScript to tell the Music app to create a new playlist with a given name """
        applescript.tell.app("Music", f'make new user playlist with properties {{name: "{name}"}}')

    def search_for_playlist(self, playlist: Playlist) -> None:
        """ Uses AppleScript to search for multiple songs to add into the playlist """
        for track in playlist.tracks:
            self.search_track(track)

    def search_track(self, track: Track) -> None:
        """ Uses AppleScript to open the Music app then simulate keyboard input to search a song """
        with open('/applemusic/scripts/search_track.applescript', 'r', encoding='utf8') as fp:
            script = f'set songName to "{track.name} by {track.artists}"' + fp.read()
        applescript.run(script)

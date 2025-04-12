""" House constants """
from typing import List


SPOTIPY_REDIRECT_URI: str = "http://127.0.0.1:9090"
SPOTIFY_SCOPES: List[str] = [
    "playlist-read-private",
    "playlist-read-collaborative",
    "user-follow-read",
    "user-library-read"
]

MAX_PLAYLISTS_PER_REQUEST: int = 50
MAX_ALBUMS_PER_REQUEST: int = MAX_PLAYLISTS_PER_REQUEST
MAX_TRACKS_PER_REQUEST: int = 1
MAX_ARTISTS_PER_REQUEST: int = 20

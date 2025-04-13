""" House constants """
from typing import List


# SpotifyAuthManager Constants
SPOTIPY_REDIRECT_URI: str = "http://127.0.0.1:9090"
SPOTIFY_SCOPES: List[str] = [
    "playlist-read-private",
    "playlist-read-collaborative",
    "user-follow-read",
    "user-library-read"
]
# SpotifyDataFetcher Constants
MAX_PLAYLISTS_PER_REQUEST: int = 50
MAX_ALBUMS_PER_REQUEST: int = MAX_PLAYLISTS_PER_REQUEST
MAX_TRACKS_PER_REQUEST: int = 50
MAX_ARTISTS_PER_REQUEST: int = 20
# DataSerializer Constants
DEFAULT_JSON_PATH = "./data/data.json"
DEFAULT_PICKLE_PATH = "./data/data.pickle"
DEFAULT_MARKDOWN_PATH = "./data/data.md"
MARKDOWN_TEMPLATE = """\
# Spotify to Apple Music Migration

## Playlists:
{playlist_section}

## Albums:
{album_section}

## Liked Songs:
{liked_section}

## Followed Artists:
{artist_section}
"""

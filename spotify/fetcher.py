""" House the SpotifyDataFetcher object """
from typing import List, Dict, Optional

from spotipy import Spotify  # type: ignore

from auth import SpotifyAuthManager
from models import Playlist, Track, Album
from constants import MAX_PLAYLISTS_PER_REQUEST, MAX_ALBUMS_PER_REQUEST, MAX_TRACKS_PER_REQUEST, MAX_ARTISTS_PER_REQUEST


class SpotifyDataFetcher:
    """ Manages fetching of data from Spotify """

    def __init__(self):
        self.auth_manager = SpotifyAuthManager().get_auth_manager()
        self.spotify = Spotify(auth_manager=self.auth_manager)

    def fetch_playlists(self, limit: int = MAX_PLAYLISTS_PER_REQUEST) -> List[Playlist]:
        """ Fetch the user's playlists from Spotify """
        playlists = []
        spotify_playlists = self.spotify.current_user_playlists(limit=limit)
        for playlist in spotify_playlists['items']:
            cover_image = self.spotify.playlist_cover_image(playlist['id'])
            name = playlist['name']
            description = playlist['description']
            author = playlist['owner']['display_name']
            tracks = self.fetch_playlist_tracks(playlist['id'])

            playlists.append(Playlist(name, f"{description} by {author}", cover_image, tracks))

        return playlists

    def fetch_playlist_tracks(self, playlist_id: str,
                              offset: int = 0,
                              limit: int = MAX_TRACKS_PER_REQUEST) -> List[Track]:
        """ Fetch and parse tracks from a given playlist_id """
        playlist_items = self.spotify.playlist_items(playlist_id=playlist_id,
                                                     limit=limit,
                                                     offset=offset,
                                                     additional_types='track')
        out = self.create_track_list(playlist_items)

        curr_offset = playlist_items['offset']
        playlist_len = playlist_items['total']
        if playlist_items['next'] and curr_offset < playlist_len:
            out.extend(self.fetch_playlist_tracks(playlist_id, curr_offset + limit, limit))

        return out

    def fetch_albums(self, limit: int = MAX_ALBUMS_PER_REQUEST) -> List[Album]:
        """ Fetch the user's saved albums from Spotify """
        albums = []
        spotify_albums = self.spotify.current_user_saved_albums(limit=limit)
        for album in spotify_albums['items']:
            album = album['album']
            name = album['name']
            artists = [artist['name'] for artist in album['artists']]
            album_id = album['id']
            tracks = self.parse_album_tracks(name, album_id, album['tracks'], limit=limit)
            albums.append(Album(name, artists, album_id, tracks))

        return albums

    def parse_album_tracks(self, album_name: str,
                           album_id: str,
                           tracks: Dict,
                           offset: int = 0,
                           limit: int = MAX_TRACKS_PER_REQUEST) -> List[Track]:
        """ Parse tracks in an album into a list of Track objects """
        out = self.create_track_list(tracks, album_name)

        curr_offset = tracks['offset']
        album_len = tracks['total']
        if tracks['next'] and curr_offset < album_len:
            new_tracks = self.spotify.album_tracks(album_id, limit=limit, offset=offset)
            out.extend(self.parse_album_tracks(album_name, album_id, new_tracks, curr_offset + limit, limit))

        return out

    def create_track_list(self, spotify_output: Dict,
                          album_name: Optional[str] = None) -> List[Track]:
        """ Given the output of a spotify query, parse the fields to create a list of Track objects """
        out = []
        for track in spotify_output['items']:
            if 'track' in track.keys():
                track = track['track']
            name = track['name']
            artists = [artist['name'] for artist in track['artists']]
            # TODO: Fetch more data than album name?
            album = album_name if album_name else track['album']['name']
            track_id = track['id']
            out.append(Track(name, artists, album, track_id))

        return out

    # def fetch_saved_tracks(self, limit: int = MAX_TRACKS_PER_REQUEST) -> List[Track]:
    #     """ Fetch the user's saved tracks from Spotify """
    #     saved_tracks = self.spotify.current_user_saved_tracks(limit=limit)
    #     print(saved_tracks)

    # def fetch_liked_songs(self) -> List[Track]:
    #     pass

    def fetch_followed_artists(self, limit: int = MAX_ARTISTS_PER_REQUEST) -> List[str]:
        """ Fetch the names of the user's followed artists from Spotify """
        artists = self.spotify.current_user_followed_artists(limit=limit)['artists']['items']
        return [artist['name'] for artist in artists]

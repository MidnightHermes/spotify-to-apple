""" Houses data objects: Track, Playlist, Data """
from typing import Optional, List, Dict


class Track:
    """ Data object for tracks aka songs """

    def __init__(self, name: str,
                 artists: List[str],
                 album: Optional[str],
                 track_id: str):
        self.name = name
        self.artists = artists
        self.album = album
        self.id = track_id

    def __repr__(self):
        """ Override __repr__ method to print a json formatted string representation of the object """
        return (f'{{"Track name": "{self.name.replace('"', "'")}",'
                f'"Track artists": {str(self.artists).replace("'", '"')},'
                f'"Track album name": "{self.album.replace('"', "'")}",'
                f'"Track id": "{self.id}"}}')

    def __str__(self):
        """ Override __str__ method to pretty print a the object """
        return f"{self.name} by {self.artists} from {self.album} with id of {self.id}"


class Playlist:
    """ Data object for playlists """

    def __init__(self, name: str,
                 description: str,
                 cover_image: List[Dict[str, Optional[int] | str]],
                 tracks: List[Track]):
        self.name = name
        self.description = description
        self.cover_image = cover_image
        self.tracks = tracks

    def __repr__(self):
        """ Override __repr__ method to print a json formatted string representation of the object """
        return (f'{{"Playlist name": "{self.name.replace('"', "'")}",'
                f'"Playlist description": "{self.description.replace('"', "'")}",'
                f'"Playlist tracks": {self.tracks}}}')

    def __str__(self):
        """ Override __str__ method to pretty print a the object """
        return f"{self.name}, {self.description} with these tracks: {self.tracks}"


class Album:
    """ Data object for albums """

    def __init__(self, name: str,
                 artists: List[str],
                 album_id: str,
                 tracks: List[Track]):
        self.name = name
        self.artists = artists
        self.id = album_id
        self.tracks = tracks

    def __repr__(self):
        """ Override __repr__ method to print a json formatted string representation of the object """
        return (f'{{"Album name": "{self.name.replace('"', "'")}",'
                f'"Album artists": {str(self.artists).replace("'", '"')},'
                f'"Album id": "{self.id}",'
                f'"Album tracks": {self.tracks}}}')

    def __str__(self):
        """ Override __str__ method to pretty print a the object """
        return f"{self.name} by {self.artists} (id of {self.id}) with these tracks: {self.tracks}"


class Data:
    """ Single data object to hold all objects """

    def __init__(self, playlists: List[Playlist],
                 albums: List[Album],
                 liked_songs: List[Track],
                 followed_artists: List[str]):
        self.liked_songs = liked_songs
        self.albums = albums
        self.playlists = playlists
        self.followed_artists = followed_artists

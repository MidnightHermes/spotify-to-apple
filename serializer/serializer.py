""" Houses DataSerializer class """
import pickle
import json

from constants import DEFAULT_JSON_PATH, DEFAULT_PICKLE_PATH, DEFAULT_MARKDOWN_PATH, MARKDOWN_TEMPLATE
from models import Data


class DataSerializer:
    """ Serializes data into either a pickle or a human-readable format (json + markdown) """

    def __init__(self):
        pass

    def save_to_json(self, data: Data,
                     filepath: str = DEFAULT_JSON_PATH) -> None:
        """ Save data to a human-readable json """
        with open(filepath, 'w', encoding='utf8') as fp:
            json.dump(data, fp, default=lambda o: o.__dict__, indent=4)

    def load_from_json(self, filepath: str = DEFAULT_JSON_PATH) -> Data:
        """ Load data from human-readable json """
        with open(filepath, 'r', encoding='utf8') as fp:
            return Data(**json.load(fp))

    def save_to_pickle(self, data: Data,
                       filepath: str = DEFAULT_PICKLE_PATH) -> None:
        """ Serialize data into a pickle """
        with open(filepath, 'wb') as fp:
            pickle.dump(data, fp)

    def load_from_pickle(self, filepath: str = DEFAULT_PICKLE_PATH) -> Data:
        """ Load data from pickle """
        with open(filepath, 'rb') as fp:
            return pickle.load(fp)

    def save_to_markdown(self, data: Data,
                         filepath: str = DEFAULT_MARKDOWN_PATH,
                         template: str = MARKDOWN_TEMPLATE) -> None:
        """ Save data to a human-readable markdown file """
        with open(filepath, 'w', encoding='utf8') as fp:
            fp.write(template.format(playlist_section=data.playlists,
                                     album_section=data.albums,
                                     liked_section=data.liked_songs,
                                     artist_section=data.followed_artists))

""" Houses DataSerializer class """
import pickle
import json

from constants import DEFAULT_JSON_PATH, DEFAULT_PICKLE_PATH, DEFAULT_MARKDOWN_PATH, MARKDOWN_TEMPLATE
from models import Data
from logs import Logger


class DataSerializer:
    """ Serializes data into either a pickle or a human-readable format (json + markdown) """

    def __init__(self):
        self.logger = Logger()

    def save_to_json(self, data: Data,
                     filepath: str = DEFAULT_JSON_PATH) -> None:
        """ Save data to a human-readable json """
        try:
            with open(filepath, 'w', encoding='utf8') as fp:
                json.dump(data, fp, default=lambda o: o.__dict__, indent=4)
            self.logger.log("INFO", "Successfully saved data to JSON")
        except Exception as e:
            self.logger.log("WARNING", f"Failed to save to JSON: {e}")

    def load_from_json(self, filepath: str = DEFAULT_JSON_PATH) -> Data:
        """ Load data from human-readable json """
        try:
            with open(filepath, 'r', encoding='utf8') as fp:
                data = Data(**json.load(fp))
            self.logger.log("INFO", "Successfully loaded data to JSON")
            return data
        except Exception as e:
            self.logger.log("WARNING", f"Failed to load JSON: {e}")
            return None

    def save_to_pickle(self, data: Data,
                       filepath: str = DEFAULT_PICKLE_PATH) -> None:
        """ Serialize data into a pickle """
        try:
            with open(filepath, 'wb') as fp:
                pickle.dump(data, fp)
            self.logger.log("INFO", "Successfully pickled data")
        except Exception as e:
            self.logger.log("WARNING", f"Failed to pickle data: {e}")

    def load_from_pickle(self, filepath: str = DEFAULT_PICKLE_PATH) -> Data:
        """ Load data from pickle """
        try:
            with open(filepath, 'rb') as fp:
                data = pickle.load(fp)
            self.logger.log("INFO", "Successfully unpickled data")
            return data
        except Exception as e:
            self.logger.log("WARNING", f"Failed to unpickle data: {e}")
            return None

    def save_to_markdown(self, data: Data,
                         filepath: str = DEFAULT_MARKDOWN_PATH,
                         template: str = MARKDOWN_TEMPLATE) -> None:
        """ Save data to a human-readable markdown file """
        try:
            with open(filepath, 'w', encoding='utf8') as fp:
                fp.write(template.format(playlist_section=data.playlists,
                                         album_section=data.albums,
                                         liked_section=data.liked_songs,
                                         artist_section=data.followed_artists))
            self.logger.log("INFO", "Successfully saved data to markdown")
        except Exception as e:
            self.logger.log("WARNING", f"Failed to save data to markdown: {e}")

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QCheckBox
)
from PyQt6.QtCore import Qt

from constants import APP_TITLE, VERSION_NUMBER


class ExportScreen(QWidget):
    """ Prompt the user for which data to export """

    def __init__(self):
        super().__init__()

        # Window title
        self.title_label = QLabel(APP_TITLE, self)
        self.title_label.setGeometry(65, 16, 604, 48)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName('h1')

        # Content container
        self.content_widget = QWidget(self)
        self.content_widget.setGeometry(160, 190, 400, 310)

        # Content content
        self.checkbox_container = QWidget(self.content_widget)
        self.checkbox_container.setGeometry(50, 15, 302, 336)

        # Content title
        self.content_text_title = QLabel("Select which data to import to Apple Music", self.content_widget)
        self.content_text_title.setGeometry(50, 0, 300, 72)
        self.content_text_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_text_title.setObjectName('h2')
        self.content_text_title.setWordWrap(True)

        # Content checkboxes
        self.playlists_checkbox = QCheckBox("Playlists", self.checkbox_container)
        self.playlists_checkbox.setGeometry(10, 60, 150, 30)

        self.liked_checkbox = QCheckBox("Liked Songs", self.checkbox_container)
        self.liked_checkbox.setGeometry(10, 100, 150, 30)

        self.artists_checkbox = QCheckBox("Artists", self.checkbox_container)
        self.artists_checkbox.setGeometry(10, 140, 150, 30)

        # Content buttons
        self.export_data_button = QPushButton("Export Data", self.content_widget)
        self.export_data_button.setGeometry(0, 198, 400, 40)
        self.back_button = QPushButton("Back", self.content_widget)
        self.back_button.setGeometry(150, 248, 100, 40)

        # Window footer
        self.footer_label = QLabel(f"{APP_TITLE} version {VERSION_NUMBER}", self)
        self.footer_label.setGeometry(260, 667, 200, 36)
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footer_label.setObjectName('p')
        self.footer_label.setWordWrap(True)

    def get_selected_options(self) -> dict:
        """ Return which checkboxes were selected """
        return {
            "playlists": self.playlists_checkbox.isChecked(),
            "liked songs": self.liked_checkbox.isChecked(),
            "artists": self.artists_checkbox.isChecked(),
        }

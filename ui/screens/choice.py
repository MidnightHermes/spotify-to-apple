from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton
)
from PyQt6.QtCore import Qt

from constants import APP_TITLE, VERSION_NUMBER


class ChoiceScreen(QWidget):
    """ Prompt the user to either import or export data """

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
        self.content_text_title = QLabel("Import data from Spotify or export data to Apple Music?", self.content_widget)
        self.content_text_title.setGeometry(50, 0, 300, 96)
        self.content_text_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_text_title.setObjectName('h2')
        self.content_text_title.setWordWrap(True)

        # Content buttons
        self.import_button = QPushButton("Import Data", self.content_widget)
        self.import_button.setGeometry(0, 198, 175, 40)
        self.export_button = QPushButton("Export Data", self.content_widget)
        self.export_button.setGeometry(225, 198, 175, 40)

        # Window footer
        self.footer_label = QLabel(f"{APP_TITLE} version {VERSION_NUMBER}", self)
        self.footer_label.setGeometry(260, 667, 200, 36)
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footer_label.setObjectName('p')
        self.footer_label.setWordWrap(True)

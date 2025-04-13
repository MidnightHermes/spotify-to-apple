""" House the LoginScreen QWidget """
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap

from constants import APP_TITLE, VERSION_NUMBER


class LoginScreen(QWidget):
    """ LoginScreen QWidget """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Window title
        self.title_label = QLabel(APP_TITLE, self)
        self.title_label.setGeometry(65, 16, 604, 48)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName('h1')

        # Content container
        self.content_widget = QWidget(self)
        self.content_widget.setGeometry(160, 300, 400, 200)

        # Content content
        self.text_container = QWidget(self.content_widget)
        self.text_container.setGeometry(50, 0, 302, 84)

        # Content title
        self.content_text_title = QLabel("Log in with Spotify", self.text_container)
        self.content_text_title.setGeometry(44, 0, 216, 36)
        self.content_text_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_text_title.setObjectName('h2')

        # Content subtitle
        self.content_text_subtitle = QLabel("Log in with Spotify to authorize this app", self.text_container)
        self.content_text_subtitle.setGeometry(0, 30, 313, 48)
        self.content_text_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_text_subtitle.setObjectName('h4')

        # Content button
        self.login_button = QPushButton("Spotify", self.content_widget)
        self.login_button.setGeometry(0, 88, 400, 40)
        pixmap = QPixmap("./assets/Spotify_logo.png")
        scaled_pixmap = pixmap.scaled(
            20, 20,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.login_button.setIcon(QIcon(scaled_pixmap))
        self.login_button.setIconSize(QSize(20, 20))

        # Content footer
        self.subtext_label = QLabel("By clicking continue,"
                                    " you agree to our <a href=\"#\">Terms of Service</a>"
                                    " and <a href=\"#\">Privacy Policy</a>",
                                    self.content_widget)
        self.subtext_label.setGeometry(0, 132, 400, 48)
        self.subtext_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtext_label.setObjectName('p')
        self.subtext_label.setWordWrap(True)

        # Window footer
        self.footer_label = QLabel(f"{APP_TITLE} version {VERSION_NUMBER}", self)
        self.footer_label.setGeometry(260, 667, 200, 36)
        self.footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.footer_label.setObjectName('p')
        self.footer_label.setWordWrap(True)

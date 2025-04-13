from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)
from PyQt6.QtCore import Qt, QCoreApplication

from logs import Logger


class ProgressDialog(QDialog):
    """ Creates a dialog box to display progress """

    def __init__(self, parent):
        super().__init__(parent)
        self.logger = Logger()
        self.setWindowTitle("Fetching Data...")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setMinimumSize(500, 400)

        self.layout = QVBoxLayout(self)
        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        self.layout.addWidget(QLabel("Log Output:"))
        self.layout.addWidget(self.log_view)

        self.close_button = QPushButton("Close")
        self.close_button.setEnabled(False)
        self.close_button.clicked.connect(self.accept)
        self.layout.addWidget(self.close_button)

    def update_logs(self):
        """ Update the log """
        self.log_view.setText("\n".join(self.logger.get_logs()))
        self.log_view.verticalScrollBar().setValue(self.log_view.verticalScrollBar().maximum())
        self.repaint()

    def unlock(self):
        """ Unlock the popup, allowing the user to return to the main window """
        self.close_button.setEnabled(True)

from PySide6.QtWidgets import QApplication, QMainWindow
from helper_ui import Ui_MainWindow

class HelperWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
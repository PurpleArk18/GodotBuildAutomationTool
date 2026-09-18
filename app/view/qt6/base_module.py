from PySide6.QtWidgets import QWidget, QMessageBox
from controller.controller import Controller

class BaseModule(QWidget):

    name:str = ""

    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

    def show_message_dialog(self, message:str, title:str = "Title") -> None:
        self.controller.show_message_dialog(self, message, title)

    def show_question_dialog(self, message:str, title:str = "Title") -> QMessageBox.StandardButton:
        return self.controller.show_question_dialog(self, title, message)

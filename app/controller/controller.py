from model.model import Model
from PySide6.QtWidgets import QStatusBar
class Controller:

    model:Model = Model()
    statusBar:QStatusBar

    def show_status_message(self, message:str) -> None:
        self.statusBar.showMessage(message)

    def set_git_configured(self, isConfigured:bool) -> None:
        pass
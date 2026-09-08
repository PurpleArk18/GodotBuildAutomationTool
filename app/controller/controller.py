from dataclasses import asdict
from model.model import Model
from PySide6.QtWidgets import QStatusBar, QMessageBox, QWidget
import json

class Controller:

    model:Model = Model()
    statusBar:QStatusBar
    
    
    def save(self) -> None:
        with open("prefs.json", "w", encoding="utf-8") as file:
            json.dump(asdict(self.model), file, indent=4)
            
    def load(self) -> None:
        with open("prefs.json", "r") as file:
            data = json.load(file)
            self.model = Model(**data)

    def show_status_message(self, message:str) -> None:
        self.statusBar.showMessage(message)

    def show_message_dialog(self, parent:QWidget, message:str, title:str = "") -> None:
        QMessageBox.information(parent, title, message)

    def set_git_configured(self, isConfigured:bool) -> None:
        self.model.set_git_configured(isConfigured)
        
    def get_git_status(self) -> bool:
        return self.model.get_git_configured()

    def get_is_debug(self) -> bool:
        return self.model.get_is_debug()

    def set_debug(self, bIsDebug:bool) -> None:
        self.model.set_debug(bIsDebug)

    def get_user_name(self) -> str :
        return self.model.get_user_name()

    def set_user_name(self, userName:str) -> None:
        self.model.set_user_name(userName)

    def get_email(self) -> str:
        return self.model.get_email()

    def set_email(self, email:str) -> None:
        self.model.set_email(email)

    def set_current_branch(self, newBranch:str) -> None:
        self.model.set_current_branch(newBranch)

    def get_current_branch(self) -> str:
        return self.model.get_current_branch()

    def get_repo_path(self) -> str:
        return self.model.get_repo_path()

    def set_repo_path(self, newPath:str) -> None:
        self.model.set_repo_path(newPath)
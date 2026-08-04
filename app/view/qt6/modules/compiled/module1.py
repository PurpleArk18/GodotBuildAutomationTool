import subprocess
import webbrowser
from controller.controller import Controller
import utils
from view.qt6.modules.compiled.module1_ui import Ui_module1
from PySide6.QtWidgets import QWidget


class Module1(QWidget, Ui_module1):
    bDebug:bool = False
    bGitConfigured = False

    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.configure_git_button.clicked.connect(self.configure_git)
        self.checkGitButton.clicked.connect(self.check_git)
        self.debugCheckBox.toggled.connect(self.set_debug)

    def configure_git(self):
        userEmail = self.emailLineEdit.text()
        userName = self.userNameLineEdit.text()
        if (userEmail != "" and userName != ""):
            subprocess.run(["git", "config", "user.name", userName])
            subprocess.run(["git", "config", "user.email", userEmail])
            self.controller.show_status_message("Configured user name and email")
        else:
            self.controller.show_status_message("Incomplete data")
        
    def check_git(self):
        git_status = subprocess.run(["git", "--version"])
        self.bGitConfigured = git_status.returncode == 0
        message = "git is installed" if self.bGitConfigured else "git not installed"
       
        if (not self.bGitConfigured):
            webbrowser.open_new_tab("https://git-scm.com/install/")
        self.controller.show_status_message(message)
      
    def set_debug(self, debug:bool) -> None:
        bDebug = debug
        self.controller.show_status_message(f"Debug set to {bDebug}")
        
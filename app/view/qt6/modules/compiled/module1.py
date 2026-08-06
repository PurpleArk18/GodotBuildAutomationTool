import subprocess
import webbrowser
from controller.controller import Controller
import utils
from view.qt6.modules.compiled.module1_ui import Ui_gitDataRoot
from PySide6.QtWidgets import QWidget


class Module1(QWidget, Ui_gitDataRoot):
   
    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.configure_git_button.clicked.connect(self.configure_git)
        self.checkGitButton.clicked.connect(self.check_git)
        self.debugCheckBox.toggled.connect(self.set_debug)

    def configure_git(self):
        userEmail = self.email_line_edit.text()
        userName = self.user_name_line_edit.text()
        if (userEmail != "" and userName != "" ):
            if not self.controller.get_is_debug():
                subprocess.run(["git", "config", "user.name", userName])
                subprocess.run(["git", "config", "user.email", userEmail])
                self.controller.set_user_name(userName)
                self.controller.set_email(userEmail)
            self.controller.show_status_message("Configured user name and email")
        else:
            self.controller.show_status_message("Incomplete data")
        
    def check_git(self):
        git_status = subprocess.run(["git", "--version"])
        bGitConfigured = git_status.returncode == 0
        self.controller.set_git_configured(bGitConfigured)
        self.set_git_configure_elements_state(bGitConfigured)
        message = "git is installed" if bGitConfigured else "git not installed"
       
        if (not bGitConfigured):
            webbrowser.open_new_tab("https://git-scm.com/install/")
        self.controller.show_status_message(message)
      
    def set_debug(self, debug:bool) -> None:
        self.controller.set_debug(debug)
        self.controller.show_status_message(f"Debug set to {debug}")

    def set_git_configure_elements_state(self, enabled:bool) -> None:
        self.configure_git_button.setEnabled(enabled)
        self.email_line_edit.setEnabled(enabled)
        self.email_label.setEnabled(enabled)
        self.user_name_label.setEnabled(enabled)
        self.user_name_line_edit.setEnabled(enabled)
        
        
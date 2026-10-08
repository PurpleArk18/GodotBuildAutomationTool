import webbrowser
from controller.controller import Controller
from view.qt6.modules.compiled.gitModule_ui import Ui_git_module_root
from view.qt6.base_module import BaseModule



class GitModule(Ui_git_module_root, BaseModule):
   
    def __init__(self, controller:Controller):
        super().__init__(controller)
        self.configure_git_button.clicked.connect(self.configure_git)
        self.checkGitButton.clicked.connect(self.check_git)
        self.debugCheckBox.toggled.connect(self.set_debug)
        self.name = "Git"

    def configure_git(self):
        userEmail = self.email_line_edit.text()
        userName = self.user_name_line_edit.text()
        if (userEmail != "" and userName != "" ):
            if not self.controller.get_is_debug():
                self.controller.run(["git", "config", "user.name", userName], self)
                self.controller.run(["git", "config", "user.email", userEmail], self)
                self.controller.set_user_name(userName)
                self.controller.set_email(userEmail)
            self.controller.show_status_message("Configured user name and email")
        else:
            self.controller.show_status_message("Incomplete data")
        
    def check_git(self):
        git_status = self.controller.run(["git", "--version"], self)
        bGitConfigured = git_status is not None and git_status.returncode == 0
        self.controller.set_git_configured(bGitConfigured)
        self.set_git_configure_elements_state(bGitConfigured)
        message = "Git is installed" if bGitConfigured else "git not installed, would you like to install it now?"
       
        if (not bGitConfigured):
            buttons = StandardButton.Ok | StandardButton.Cancel
            button = self.controller.show_message_dialog(self, "Git status", message, buttons)
            if (button == QMessageBox.StandardButton.Ok):
                webbrowser.open_new_tab("https://git-scm.com/install/")
        else:
            self.controller.show_message_dialog(self, "Git status", message)

        
      
    def set_debug(self, debug:bool) -> None:
        self.controller.set_debug(debug)
        self.controller.show_status_message(f"Debug set to {debug}")

    def set_git_configure_elements_state(self, enabled:bool) -> None:
        self.configure_git_button.setEnabled(enabled)
        self.email_line_edit.setEnabled(enabled)
        self.email_label.setEnabled(enabled)
        self.user_name_label.setEnabled(enabled)
        self.user_name_line_edit.setEnabled(enabled)


        
        
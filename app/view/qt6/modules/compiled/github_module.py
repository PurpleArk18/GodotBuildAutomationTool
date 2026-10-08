from controller.controller import Controller
from view.qt6.modules.compiled.githubModule_ui import Ui_github_module_root
from view.qt6.base_module import BaseModule
from PySide6.QtCore import Qt

class GithubModule(Ui_github_module_root, BaseModule):
   
    def __init__(self, controller:Controller):
        super().__init__(controller)
        self.check_github_cli_button.clicked.connect(self.check_github)
        self.install_github_cli_button.clicked.connect(self.install_github)
        self.use_github_checkbox.stateChanged.connect(self.use_github_state_changed)
        self.name = "Github"

    def check_github(self) -> None:
        github_status = self.controller.run(["gh", "--version"], self)
        bGithubConfigured = github_status.returncode == 0
        message = "Github CLI is installed" if bGithubConfigured else "GitHub CLI not installed"
        self.controller.show_message_dialog(self, "Github CLI status", message)
        self.install_github_cli_button.setEnabled(bGithubConfigured)

    def install_github(self) -> None:
        if not self.controller.get_is_debug():
            self.controller.run(["winget", "install", "--id", "GitHub.cli", "--source", "winget"], self)

    def use_github_state_changed(self, newState:Qt.CheckState) -> None:
        enabled:bool = newState == Qt.CheckState.Checked.value
        self.check_github_cli_button.setEnabled(enabled)
        self.install_github_cli_button.setEnabled(enabled)


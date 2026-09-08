from controller.controller import Controller
from view.qt6.modules.compiled.githubModule_ui import Ui_github_module_root
from view.qt6.base_module import BaseModule
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
import subprocess

class GithubModule(QWidget, Ui_github_module_root, BaseModule):
   
    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.check_github_cli_button.clicked.connect(self.check_github)
        self.install_github_cli_button.clicked.connect(self.install_github)
        self.use_github_checkbox.stateChanged.connect(self.use_github_state_changed)
        self.name = "Github"

    def check_github(self) -> None:
        github_status = subprocess.run(["gh", "--version"])
        bGithubConfigured = github_status.returncode == 0
        message = "Github CLI is installed" if bGithubConfigured else "GitHub CLI not installed"
        self.controller.show_status_message(message)
        self.install_github_cli_button.setEnabled(bGithubConfigured)

    def install_github(self) -> None:
        if not self.controller.get_is_debug():
            subprocess.run(["winget", "install", "--id", "GitHub.cli", "--source", "winget"])

    def use_github_state_changed(self, newState:Qt.CheckState) -> None:
        enabled = newState == Qt.CheckState.Checked
        self.check_github_cli_button.setEnabled(enabled)
        self.install_github_cli_button.setEnabled(enabled)


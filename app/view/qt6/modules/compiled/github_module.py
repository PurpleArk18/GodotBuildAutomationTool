from controller.controller import Controller
from view.qt6.modules.compiled.githubModule_ui import Ui_github_module_root
from PySide6.QtWidgets import QWidget
import subprocess

class GithubModule(QWidget, Ui_github_module_root):
   
    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.check_github_cli_button.clicked.connect(self.check_github)

    def check_github(self) -> None:
        github_status = subprocess.run(["gh", "--version"])
        bGithubConfigured = github_status.returncode == 0
        message = "Github CLI is installed" if bGithubConfigured else "GitHub CLI not installed"
        self.controller.show_status_message(message)

    def install_github(self) -> None:
        if not self.controller.get_is_debug():
            subprocess.run(["winget", "install", "--id", "GitHub.cli", "--source", "winget"])

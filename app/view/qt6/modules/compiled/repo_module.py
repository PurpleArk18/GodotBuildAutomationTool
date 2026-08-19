from controller.controller import Controller
from view.qt6.modules.compiled.repoModule_ui import Ui_repo_module_root
from PySide6.QtWidgets import QWidget
import subprocess

class RepoModule(QWidget, Ui_repo_module_root):
   
    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.check_branches_button.clicked.connect(self.set_branch_options)

    def get_branches(self) -> list[str]:
        result = subprocess.run(["git", "branch", "-r"], capture_output=True, text=True)
        branches = result.stdout
        print(branches)
        return branches.split("\n")

    def set_branch_options(self) -> None:
        branches = self.get_branches()
        self.select_branch_comboBox.addItems(branches)

    def fork_godot(self) -> None:
        subprocess.run(["gh", "repo", "fork", "https://github.com/godotengine/godot", "--clone=True", "--remote=True"])
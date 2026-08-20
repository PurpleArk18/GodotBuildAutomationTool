from controller.controller import Controller
from view.qt6.modules.compiled.repoModule_ui import Ui_repo_module_root
from PySide6.QtWidgets import QWidget, QFileDialog
import subprocess

class RepoModule(QWidget, Ui_repo_module_root):
   
    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.check_branches_button.clicked.connect(self.set_branch_options)
        self.select_branch_comboBox.currentTextChanged.connect(self.branch_selected)
        self.select_repo_path_button.clicked.connect(self.select_repo_path)

    def get_branches(self) -> list[str]:
        result = subprocess.run(["git", "branch", "-r"], capture_output=True, text=True)
        branches = result.stdout
        print(branches)
        return branches.split("\n")

    def set_branch_options(self) -> None:
        branches = self.get_branches()
        self.select_branch_comboBox.addItems(branches)

    def branch_selected(self, newBranch:str) -> None:
        self.controller.set_current_branch(newBranch)

    def fork_godot(self) -> None:
        if not self.controller.get_is_debug():
            subprocess.run(["gh", "repo", "fork", "https://github.com/godotengine/godot", "--clone=True", "--remote=True"])

    def select_repo_path(self) -> None:
        path = QFileDialog.getExistingDirectory(self, caption="Select Repo Location", dir="", options=QFileDialog.ShowDirsOnly)
        print(path)
        if path != "" and not self.controller.get_is_debug():
            self.controller.set_repo_path(path)

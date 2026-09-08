from controller.controller import Controller
from view.qt6.modules.compiled.git_module import GitModule
from view.qt6.modules.compiled.github_module import GithubModule
from view.qt6.modules.compiled.repo_module import RepoModule
from view.qt6.modules.compiled.build_module import BuildModule
from view.qt6.modules.compiled.main_ui import Ui_MainWindow

from PySide6.QtWidgets import (QMainWindow)


class MainWindow(QMainWindow, Ui_MainWindow):
    
    modules = []

    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        controller.statusBar = self.statusbar

        self.git_module = GitModule(controller)
        self.modules.append(self.git_module)
        
        self.github_module = GithubModule(controller)
        self.modules.append(self.github_module)
       
        self.repo_module = RepoModule(controller)
        self.modules.append(self.repo_module)
       
        self.build_module = BuildModule(controller)
        self.modules.append(self.build_module)

        self.add_widgets()
       
    def add_widgets(self) -> None:
        for module in self.modules:
            self.modules_tabWidget.addTab(module, module.name)


  
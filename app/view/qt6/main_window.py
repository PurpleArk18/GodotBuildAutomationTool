from ast import Module
import subprocess
import webbrowser
import utils
from controller.controller import Controller
from view.qt6.dialog import CustomDialog
from view.qt6.modules.compiled.git_module import GitModule
from view.qt6.modules.compiled.github_module import GithubModule
from view.qt6.modules.compiled.repo_module import RepoModule
from view.qt6.modules.compiled.build_module import BuildModule
from view.qt6.modules.compiled.main_ui import Ui_MainWindow
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget)


class MainWindow(QMainWindow, Ui_MainWindow):
    

    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        controller.statusBar = self.statusbar

        self.git_module = GitModule(controller)
        self.verticalLayout_2.addWidget(self.git_module)

        self.github_module = GithubModule(controller)
        self.verticalLayout_2.addWidget(self.github_module)

        self.repo_module = RepoModule(controller)
        self.verticalLayout_2.addWidget(self.repo_module)

        self.build_module = BuildModule(controller)
        self.verticalLayout_2.addWidget(self.build_module)
  
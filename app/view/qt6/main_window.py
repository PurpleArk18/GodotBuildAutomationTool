import subprocess
import webbrowser
import utils
from view.qt6.dialog import CustomDialog
from view.qt6.modules.compiled.module1_ui import Ui_module1Main
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QMainWindow, QPushButton, QToolBar, QStatusBar, QFileDialog)


class MainWindow(QMainWindow, Ui_module1Main):
    bDebug:bool = False
    bGitConfigured = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.configure_git_button.clicked.connect(self.configure_git)
        self.checkGitButton.clicked.connect(self.check_git)
        self.debugCheckBox.toggled.connect(self.set_debug)

    def configure_git(self):
        userEmail = self.emailLineEdit.text()
        userName = self.userNameLineEdit.text()
        if (userEmail != "" and userName != ""):
            subprocess.run(["git", "config", "user.name", userName])
            subprocess.run(["git", "config", "user.email", userEmail])
            self.statusbar.showMessage("Configured user name and email")
        else:
            self.statusbar.showMessage("Incomplete data")
        
    def check_git(self):
        git_status = subprocess.run(["git", "--version"])
        self.bGitConfigured = git_status.returncode == 0
        message = "git is installed" if self.bGitConfigured else "git not installed"
        self.statusbar.showMessage(message)
        if (not self.bGitConfigured):
            webbrowser.open_new_tab("https://git-scm.com/install/")
        

    def set_debug(self, debug:bool) -> None:
        bDebug = debug
        

    # def __init__(self):
    #     super().__init__()
    #     self.setWindowTitle("Godot Build Automation in Qt6")
    #     self.setMinimumSize(QSize(650,400))

    #     toolbar = QToolBar("MainToolbar")
    #     toolbar.toggleViewAction().setEnabled(False)
    #     toolbar.setIconSize(QSize(16, 16))
    #     button_action = QAction(QIcon(utils.get_icon_path("bug.png")), "your button", self)
    #     button_action.setStatusTip("This is your button")
    #     button_action.triggered.connect(self.onMyToolBarButtonClick)
    #     toolbar.addAction(button_action)

    #     button = QPushButton("Click me")
    #     button.setCheckable(True)
    #     button.clicked.connect(self.get_filename)

    #     self.setCentralWidget(button)
    #     self.addToolBar(toolbar)
    #     self.setStatusBar(QStatusBar(self))

    #     menu = self.menuBar()
    #     file_menu = menu.addMenu("&File")
    #     file_menu.addAction(button_action)

    # def button_clicked(self, is_checked : bool):
    #     dlg = CustomDialog(self)
    #     dlg.exec()
    #     print("Clicked, ", is_checked)

    # def onMyToolBarButtonClick(self, is_checked):
    #     print("Clicked, ", is_checked)

    # def get_filename(self):
    #     initial_filter = utils.FILE_FILTERS[3] # Select one from the list.
    #     print("Filters are:", utils.filters)
    #     print("Initial filter:", initial_filter)
    #     filename, selected_filter = QFileDialog.getOpenFileName(self, filter=utils.filters, selectedFilter=initial_filter)
    #     print("Result:", filename, selected_filter)
  
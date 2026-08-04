from ast import Module
import subprocess
import webbrowser
import utils
from controller.controller import Controller
from view.qt6.dialog import CustomDialog
from view.qt6.modules.compiled.module1 import Module1
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
        module1 = Module1(controller)
        self.verticalLayout_2.addWidget(module1)

        # self.setWindowTitle("Godot Build Automation in Qt6")
        # self.setMinimumSize(QSize(650,400))

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
  
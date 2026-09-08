from controller.controller import Controller
from view.qt6.modules.compiled.buildModule_ui import Ui_build_module_root
from view.qt6.base_module import BaseModule
from PySide6.QtWidgets import QWidget

class BuildModule(QWidget, Ui_build_module_root, BaseModule):

    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.name = "Build"
        
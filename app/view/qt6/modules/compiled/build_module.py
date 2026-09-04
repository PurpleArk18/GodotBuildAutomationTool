from controller.controller import Controller
from view.qt6.modules.compiled.buildModule_ui import Ui_build_module_root
from PySide6.QtWidgets import QWidget

class BuildModule(QWidget, Ui_build_module_root):

    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

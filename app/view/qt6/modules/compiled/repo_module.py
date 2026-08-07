from controller.controller import Controller
from view.qt6.modules.compiled.repoModule_ui import Ui_repo_module_root
from PySide6.QtWidgets import QWidget


class GitModule(QWidget, Ui_repo_module_root):
   
    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
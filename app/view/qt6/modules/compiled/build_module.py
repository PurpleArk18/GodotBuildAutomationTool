from controller.controller import Controller
from view.qt6.modules.compiled.buildModule_ui import Ui_build_module_root
from view.qt6.base_module import BaseModule
from PySide6.QtWidgets import QWidget

import subprocess

class BuildModule(Ui_build_module_root, BaseModule):

    def __init__(self, controller:Controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.name = "Build"
        self.check_scons_button.clicked.connect(self.check_scons)
        self.install_scons_button.clicked.connect(self.install_scons)
        self.update_scons_button.clicked.connect(self.update_scons)
        self.build_button.clicked.connect(self.build)

    def check_scons(self):
        scons_status = subprocess.run(["scons", "--version"])
        bSconsConfigured = scons_status.returncode == 0
        message = "Scons is installed" if bGithubConfigured else "Scons not installed"
        self.controller.show_message_dialog(self, message, "Scons status")

    def install_scons(self):
        pass

    def update_scons(self):
        pass

    def build(self):
        pass

        
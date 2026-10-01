from controller.controller import Controller
from view.qt6.modules.compiled.buildModule_ui import Ui_build_module_root
from view.qt6.base_module import BaseModule
from PySide6.QtWidgets import QWidget

class BuildModule(Ui_build_module_root, BaseModule):

    build_args:list[str] = ["scons"]

    def __init__(self, controller:Controller):
        super().__init__(controller)
        self.name = "Build"
        self.check_scons_button.clicked.connect(self.check_scons)
        self.install_scons_button.clicked.connect(self.install_scons)
        self.update_scons_button.clicked.connect(self.update_scons)
        self.build_button.clicked.connect(self.build)


    def check_scons(self):
        scons_status = self.controller.run(self, ["scons", "-v"], True, True, True)
        bSconsConfigured = scons_status is not None and scons_status.returncode == 0
        message = "Scons is installed" if bSconsConfigured else "Scons not installed"
        self.controller.show_message_dialog(self, message, "Scons status")

    def install_scons(self):
        self.controller.run(["python", "-m", "pip", "install", "-scons"])

    def update_scons(self):
        self.controller.run(["python", "-m", "pip", "install", "--upgrade scons"])

    def build(self):
        self.controller.run(["scons"])

        
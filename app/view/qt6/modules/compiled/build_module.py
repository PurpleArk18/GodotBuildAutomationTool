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
        self.platform_combo_box.currentTextChanged.connect(self.platform_changed)
        self.threads_combo_box.currentIndexChanged.connect(self.threads_changed)
        self.target_combo_box.currentTextChanged.connect(self.target_changed)
        self.optimization_level_combo_box.currentTextChanged.connect(self.optimization_level_changed)
        self.dev_build_check_box.toggled.connect(self.dev_build_toggled)
        self.debug_symbols_check_box.toggled.connect(self.debug_symbols_toggled))

    def check_scons(self):
        scons_status = self.controller.run(["scons", "-v"], self, True, True, True)
        bSconsConfigured = scons_status is not None and scons_status.returncode == 0
        message = "Scons is installed" if bSconsConfigured else "Scons not installed"
        self.controller.show_message_dialog(self, "Scons status", message)
        self.get_build_platforms()

    def install_scons(self):
        self.controller.run(["python", "-m", "pip", "install", "scons"], self)

    def update_scons(self):
        self.controller.run(["python", "-m", "pip", "install", "--upgrade scons"], self)

    def build(self):
        self.controller.run(["scons"])

    def get_build_platforms(self):
        text = self.controller.run(["scons", "platform=list"], self, True, True)
        if text is not None:
            self.controller.show_message_dialog(self, "", text.stdout)

    def platform_changed(self, text:str) -> None:
        pass

    def threads_changed(self, index:int) -> None:
        pass

    def target_changed(self, text:str) -> None:
        pass

    def optimization_level_changed(self, text:str) -> None:
        pass

    def dev_build_toggled(self, checked:bool) -> None:
        pass

    def debug_symbols_toggled(self, checked:bool) -> None:
        pass




        
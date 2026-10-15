from controller.controller import Controller
from view.qt6.modules.compiled.buildModule_ui import Ui_build_module_root
from view.qt6.base_module import BaseModule
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

class BuildModule(Ui_build_module_root, BaseModule):

    build_args:dict[str,str] = {"base": "scons"}

    def __init__(self, controller:Controller):
        super().__init__(controller)
        self.name = "Build"
        self.check_scons_button.clicked.connect(self.check_scons)
        self.install_scons_button.clicked.connect(self.install_scons)
        self.update_scons_button.clicked.connect(self.update_scons)
        self.build_button.clicked.connect(self.build)
        self.platform_comboBox.currentTextChanged.connect(self.platform_changed)
        self.threads_spinBox.valueChanged.connect(self.threads_changed)
        self.target_comboBox.currentTextChanged.connect(self.target_changed)
        self.optimization_level_comboBox.currentTextChanged.connect(self.optimization_level_changed)
        self.dev_build_checkBox.stateChanged.connect(self.dev_build_toggled)
        self.debug_symbols_checkBox.stateChanged.connect(self.debug_symbols_toggled)

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
        if self.controller.get_is_debug():
            self.controller.show_message_dialog(self, "Debug build", " ".join(self.build_args.values()))
            return
        self.controller.run([arg for arg in self.build_args.values()], self)

    def get_build_platforms(self):
        text = self.controller.run(["scons", "platform=list"], self, True, True)
        if text is not None:
            self.controller.show_message_dialog(self, "", text.stdout)

    def platform_changed(self, text:str) -> None:
        key = "platform"
        self.set_build_arg(key, text)

    def threads_changed(self, index:int) -> None:
        key = "threads"
        arg = "-j{}".format(index)
        self.build_args[key] = arg

    def target_changed(self, text:str) -> None:
        key = "target"
        self.set_build_arg(key, text)

    def optimization_level_changed(self, text:str) -> None:
        pass

    def dev_build_toggled(self, checked:Qt.CheckState) -> None:
        key = "dev_build"
        value = "yes" if Qt.CheckState(checked) == Qt.CheckState.Checked else "no"
        self.set_build_arg(key, value)

    def debug_symbols_toggled(self, checked:Qt.CheckState) -> None:
        key = "debug_symbols"
        value = "yes" if Qt.CheckState(checked) == Qt.CheckState.Checked else "no"
        self.set_build_arg(key, value)

    def set_build_arg(self, key:str, value:str) -> None:
        arg = "{}={}".format(key, value)
        self.build_args[key] = arg
        self.controller.show_status_message(f"Build argument set: {arg}")

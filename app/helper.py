from helper_window import HelperWindow
import main
import utils
import subprocess
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


class Helper:
    args:dict[str,str] = {}

    currentProcess = None

    def launch(self):
        self.args["frontend"] = self.window.frontendComboBox.currentText()
        self.currentProcess = subprocess.Popen([sys.executable, "app/main.py"])
    
    def open_qt_designer(self):
        subprocess.Popen("pyside6-designer")
        
    def recompile(self):
        if (self.currentProcess != None):
            self.currentProcess.terminate()
        resource = subprocess.run(["pyside6-rcc", "app/rsc/resources.qrc", "-o", "app/resources_rc.py"])
        if resource.returncode == 0:
            self.window.statusbar.showMessage("Resources compiled correctly")

        main = subprocess.run(["pyside6-uic", "app/view/qt6/modules/ui/main.ui", "-o", "app/view/qt6/modules/compiled/main_ui.py"])
        if main.returncode == 0:
            self.window.statusbar.showMessage("Main compiled correctly")

        gitmodule = subprocess.run(["pyside6-uic", "app/view/qt6/modules/ui/gitModule.ui", "-o", "app/view/qt6/modules/compiled/gitModule_ui.py"])
        if gitmodule.returncode == 0:
            self.window.statusbar.showMessage("Git module compiled correctly")

        githubmodule = subprocess.run(["pyside6-uic", "app/view/qt6/modules/ui/githubModule.ui", "-o", "app/view/qt6/modules/compiled/githubModule_ui.py"])
        if githubmodule.returncode == 0:
            self.window.statusbar.showMessage("Github module compiled correctly")

        repomodule = subprocess.run(["pyside6-uic", "app/view/qt6/modules/ui/repoModule.ui", "-o", "app/view/qt6/modules/compiled/repoModule_ui.py"])
        if repomodule.returncode == 0:
            self.window.statusbar.showMessage("Repo module compiled correctly")

    def recompile_helper(self):
        subprocess.run(["pyside6-uic", "app/helper.ui", "-o", "app/helper_ui.py"])

    def package(self):
        pass

    def open_spec(self):
        pass

    def launch_installforge(self):
        pass

    def __init__(self):
        loader = QUiLoader()
        app = QApplication()
        self.window = HelperWindow()
        self.window.launch_button.pressed.connect(self.launch)
        self.window.open_qtdesigner_button.pressed.connect(self.open_qt_designer)
        self.window.recompile_button.pressed.connect(self.recompile)
        self.window.recompile_helper_button.pressed.connect(self.recompile_helper)
        self.window.package_button.pressed.connect(self.package)
        self.window.open_spec_file_button.pressed.connect(self.open_spec)
        self.window.launc_installforge_button.pressed.connect(self.launch_installforge)
        self.window.show()
        app.exec()

if __name__ == "__main__":
    helper = Helper()






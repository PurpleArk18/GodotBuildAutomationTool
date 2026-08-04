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
        module1 = subprocess.run(["pyside6-uic", "app/view/qt6/modules/ui/module1.ui", "-o", "app/view/qt6/modules/compiled/module1_ui.py"])
        if module1.returncode == 0:
            self.window.statusbar.showMessage("Module 1 compiled correctly")

        # self.launch()


    def recompile_helper(self):
        subprocess.run(["pyside6-uic", "app/helper.ui", "-o", "app/helper_ui.py"])

    def __init__(self):
        loader = QUiLoader()
        app = QApplication()
        self.window = HelperWindow()
        self.window.launch_button.pressed.connect(self.launch)
        self.window.open_qtdesigner_button.pressed.connect(self.open_qt_designer)
        self.window.recompile_button.pressed.connect(self.recompile)
        self.window.show()
        app.exec()

if __name__ == "__main__":
    helper = Helper()






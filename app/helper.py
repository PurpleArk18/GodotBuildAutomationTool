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
        # main.main(self.args)
    
    def open_qt_designer(self):
        subprocess.run("pyside6-designer")
        
    def recompile(self):
        if (self.currentProcess):
            self.currentProcess.terminate()
        subprocess.run(["pyside6-uic" "app/view/qt6/modules/ui/module1.ui" "-o" "app/view/qt6/modules/compiled/module1_ui.py"])
        self.launch()


    def recompile_helper(self):
        subprocess.run(["pyside6-uic" "app/helper.ui" "-o" "app/helper_ui.py"])

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
    Helper()






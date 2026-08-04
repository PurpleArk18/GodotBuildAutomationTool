import argparse
import utils
from PySide6.QtWidgets import QApplication
from tkinter import Tk
from view.qt6.main_window import MainWindow
from PySide6.QtUiTools import QUiLoader
from controller.controller import Controller

loader = QUiLoader()

def run_qt():
    # Qt6 app
    app = QApplication()
    controller = Controller()
    window = MainWindow(controller)
    window.show()
    app.exec()

def run_tkinter():
    # tkinter app
    root = Tk()
    root.title("Godot Build Automation Tool in TKinter")
    root.geometry('650x400')
    root.mainloop()

def main(args:dict[str,str]):

    if (len(args) > 1 and args["frontend"] == "-tk"):
        run_tkinter()
    else:
        run_qt()

if (__name__ == '__main__'):
    main({})
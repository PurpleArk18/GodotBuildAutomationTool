# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helper.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 40, 401, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.open_qtdesigner_button = QPushButton(self.verticalLayoutWidget)
        self.open_qtdesigner_button.setObjectName(u"open_qtdesigner_button")

        self.verticalLayout.addWidget(self.open_qtdesigner_button)

        self.recompile_button = QPushButton(self.verticalLayoutWidget)
        self.recompile_button.setObjectName(u"recompile_button")

        self.verticalLayout.addWidget(self.recompile_button)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(2)
        self.frontendComboBox = QComboBox(self.verticalLayoutWidget)
        self.frontendComboBox.addItem("")
        self.frontendComboBox.addItem("")
        self.frontendComboBox.setObjectName(u"frontendComboBox")
        self.frontendComboBox.setMaxVisibleItems(2)
        self.frontendComboBox.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.frontendComboBox.setMinimumContentsLength(0)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.frontendComboBox)

        self.frontendLabel = QLabel(self.verticalLayoutWidget)
        self.frontendLabel.setObjectName(u"frontendLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.frontendLabel)


        self.verticalLayout.addLayout(self.formLayout)

        self.launch_button = QPushButton(self.verticalLayoutWidget)
        self.launch_button.setObjectName(u"launch_button")

        self.verticalLayout.addWidget(self.launch_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_qtdesigner_button.setText(QCoreApplication.translate("MainWindow", u"Open Qt Designer", None))
        self.recompile_button.setText(QCoreApplication.translate("MainWindow", u"Recompile main", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Recompile helper", None))
        self.frontendComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"-qt6", None))
        self.frontendComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"-tkinter", None))

        self.frontendComboBox.setCurrentText("")
        self.frontendComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.frontendLabel.setText(QCoreApplication.translate("MainWindow", u"Frontend", None))
        self.launch_button.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
    # retranslateUi


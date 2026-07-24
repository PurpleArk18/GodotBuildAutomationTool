# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'module1.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

class Ui_module1Main(object):
    def setupUi(self, module1Main):
        if not module1Main.objectName():
            module1Main.setObjectName(u"module1Main")
        module1Main.resize(663, 376)
        self.centralwidget = QWidget(module1Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.emailLabel = QLabel(self.centralwidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self.centralwidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.emailLineEdit)

        self.userNameLabel = QLabel(self.centralwidget)
        self.userNameLabel.setObjectName(u"userNameLabel")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.userNameLabel)

        self.userNameLineEdit = QLineEdit(self.centralwidget)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.userNameLineEdit)

        self.debugLabel = QLabel(self.centralwidget)
        self.debugLabel.setObjectName(u"debugLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.debugLabel)

        self.debugCheckBox = QCheckBox(self.centralwidget)
        self.debugCheckBox.setObjectName(u"debugCheckBox")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.debugCheckBox)


        self.verticalLayout.addLayout(self.formLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkGitButton = QPushButton(self.centralwidget)
        self.checkGitButton.setObjectName(u"checkGitButton")

        self.horizontalLayout_2.addWidget(self.checkGitButton)

        self.configure_git_button = QPushButton(self.centralwidget)
        self.configure_git_button.setObjectName(u"configure_git_button")

        self.horizontalLayout_2.addWidget(self.configure_git_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        module1Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(module1Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 663, 33))
        module1Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(module1Main)
        self.statusbar.setObjectName(u"statusbar")
        module1Main.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(module1Main)
        self.toolBar.setObjectName(u"toolBar")
        module1Main.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(module1Main)

        QMetaObject.connectSlotsByName(module1Main)
    # setupUi

    def retranslateUi(self, module1Main):
        module1Main.setWindowTitle(QCoreApplication.translate("module1Main", u"MainWindow", None))
        self.emailLabel.setText(QCoreApplication.translate("module1Main", u"Email", None))
        self.userNameLabel.setText(QCoreApplication.translate("module1Main", u"User Name", None))
        self.debugLabel.setText(QCoreApplication.translate("module1Main", u"Debug", None))
        self.checkGitButton.setText(QCoreApplication.translate("module1Main", u"Check Git", None))
        self.configure_git_button.setText(QCoreApplication.translate("module1Main", u"Configure Git", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("module1Main", u"toolBar", None))
    # retranslateUi


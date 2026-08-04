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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_module1(object):
    def setupUi(self, module1):
        if not module1.objectName():
            module1.setObjectName(u"module1")
        module1.resize(400, 300)
        module1.setMinimumSize(QSize(200, 200))
        self.verticalLayout_2 = QVBoxLayout(module1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.emailLabel = QLabel(module1)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(module1)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.emailLineEdit)

        self.userNameLabel = QLabel(module1)
        self.userNameLabel.setObjectName(u"userNameLabel")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.userNameLabel)

        self.userNameLineEdit = QLineEdit(module1)
        self.userNameLineEdit.setObjectName(u"userNameLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.userNameLineEdit)

        self.debugLabel = QLabel(module1)
        self.debugLabel.setObjectName(u"debugLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.debugLabel)

        self.debugCheckBox = QCheckBox(module1)
        self.debugCheckBox.setObjectName(u"debugCheckBox")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.debugCheckBox)


        self.verticalLayout.addLayout(self.formLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkGitButton = QPushButton(module1)
        self.checkGitButton.setObjectName(u"checkGitButton")

        self.horizontalLayout_2.addWidget(self.checkGitButton)

        self.configure_git_button = QPushButton(module1)
        self.configure_git_button.setObjectName(u"configure_git_button")

        self.horizontalLayout_2.addWidget(self.configure_git_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(module1)

        QMetaObject.connectSlotsByName(module1)
    # setupUi

    def retranslateUi(self, module1):
        module1.setWindowTitle(QCoreApplication.translate("module1", u"Form", None))
        self.emailLabel.setText(QCoreApplication.translate("module1", u"Email", None))
        self.userNameLabel.setText(QCoreApplication.translate("module1", u"User Name", None))
        self.debugLabel.setText(QCoreApplication.translate("module1", u"Debug", None))
        self.checkGitButton.setText(QCoreApplication.translate("module1", u"Check Git", None))
        self.configure_git_button.setText(QCoreApplication.translate("module1", u"Configure Git", None))
    # retranslateUi


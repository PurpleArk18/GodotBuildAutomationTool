# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'githubModule.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_github_module_root(object):
    def setupUi(self, github_module_root):
        if not github_module_root.objectName():
            github_module_root.setObjectName(u"github_module_root")
        github_module_root.resize(401, 277)
        self.verticalLayout = QVBoxLayout(github_module_root)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.use_github_label = QLabel(github_module_root)
        self.use_github_label.setObjectName(u"use_github_label")
        self.use_github_label.setMinimumSize(QSize(120, 0))
        self.use_github_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.use_github_label)

        self.check_github_cli_button = QPushButton(github_module_root)
        self.check_github_cli_button.setObjectName(u"check_github_cli_button")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.check_github_cli_button)

        self.install_github_cli_button = QPushButton(github_module_root)
        self.install_github_cli_button.setObjectName(u"install_github_cli_button")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.install_github_cli_button)

        self.use_github_checkbox = QCheckBox(github_module_root)
        self.use_github_checkbox.setObjectName(u"use_github_checkbox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_github_checkbox.sizePolicy().hasHeightForWidth())
        self.use_github_checkbox.setSizePolicy(sizePolicy)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.use_github_checkbox)


        self.verticalLayout.addLayout(self.formLayout_3)


        self.retranslateUi(github_module_root)

        QMetaObject.connectSlotsByName(github_module_root)
    # setupUi

    def retranslateUi(self, github_module_root):
        github_module_root.setWindowTitle(QCoreApplication.translate("github_module_root", u"Form", None))
        self.use_github_label.setText(QCoreApplication.translate("github_module_root", u"Use GitHub", None))
        self.check_github_cli_button.setText(QCoreApplication.translate("github_module_root", u"Check GitHub CLI", None))
        self.install_github_cli_button.setText(QCoreApplication.translate("github_module_root", u"Install GitHub CLI", None))
    # retranslateUi


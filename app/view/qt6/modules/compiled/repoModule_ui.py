# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'repoModule.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_repo_module_root(object):
    def setupUi(self, repo_module_root):
        if not repo_module_root.objectName():
            repo_module_root.setObjectName(u"repo_module_root")
        repo_module_root.resize(422, 144)
        self.verticalLayout = QVBoxLayout(repo_module_root)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.check_branches_button = QPushButton(repo_module_root)
        self.check_branches_button.setObjectName(u"check_branches_button")

        self.verticalLayout.addWidget(self.check_branches_button)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.branchesLabel = QLabel(repo_module_root)
        self.branchesLabel.setObjectName(u"branchesLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.branchesLabel)

        self.select_branch_comboBox = QComboBox(repo_module_root)
        self.select_branch_comboBox.setObjectName(u"select_branch_comboBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.select_branch_comboBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.checkout_branch_button = QPushButton(repo_module_root)
        self.checkout_branch_button.setObjectName(u"checkout_branch_button")

        self.verticalLayout.addWidget(self.checkout_branch_button)

        self.fork_godot_button = QPushButton(repo_module_root)
        self.fork_godot_button.setObjectName(u"fork_godot_button")

        self.verticalLayout.addWidget(self.fork_godot_button)

        self.select_repo_path_button = QPushButton(repo_module_root)
        self.select_repo_path_button.setObjectName(u"select_repo_path_button")

        self.verticalLayout.addWidget(self.select_repo_path_button)


        self.retranslateUi(repo_module_root)

        QMetaObject.connectSlotsByName(repo_module_root)
    # setupUi

    def retranslateUi(self, repo_module_root):
        repo_module_root.setWindowTitle(QCoreApplication.translate("repo_module_root", u"Form", None))
        self.check_branches_button.setText(QCoreApplication.translate("repo_module_root", u"Check Branches", None))
        self.branchesLabel.setText(QCoreApplication.translate("repo_module_root", u"Branches", None))
        self.checkout_branch_button.setText(QCoreApplication.translate("repo_module_root", u"Checkout Branch", None))
        self.fork_godot_button.setText(QCoreApplication.translate("repo_module_root", u"Fork Godot", None))
        self.select_repo_path_button.setText(QCoreApplication.translate("repo_module_root", u"Select Repo Location", None))
    # retranslateUi


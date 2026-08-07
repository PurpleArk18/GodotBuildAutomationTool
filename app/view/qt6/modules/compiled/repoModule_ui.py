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
    QSizePolicy, QWidget)

class Ui_repo_module_root(object):
    def setupUi(self, repo_module_root):
        if not repo_module_root.objectName():
            repo_module_root.setObjectName(u"repo_module_root")
        repo_module_root.resize(400, 300)
        self.formLayout = QFormLayout(repo_module_root)
        self.formLayout.setObjectName(u"formLayout")
        self.branchesLabel = QLabel(repo_module_root)
        self.branchesLabel.setObjectName(u"branchesLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.branchesLabel)

        self.branchesComboBox = QComboBox(repo_module_root)
        self.branchesComboBox.setObjectName(u"branchesComboBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.branchesComboBox)


        self.retranslateUi(repo_module_root)

        QMetaObject.connectSlotsByName(repo_module_root)
    # setupUi

    def retranslateUi(self, repo_module_root):
        repo_module_root.setWindowTitle(QCoreApplication.translate("repo_module_root", u"Form", None))
        self.branchesLabel.setText(QCoreApplication.translate("repo_module_root", u"Branches", None))
    # retranslateUi


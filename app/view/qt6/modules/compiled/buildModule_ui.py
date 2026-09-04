# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buildModule.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_build_module_root(object):
    def setupUi(self, build_module_root):
        if not build_module_root.objectName():
            build_module_root.setObjectName(u"build_module_root")
        build_module_root.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(build_module_root)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.check_scons_button = QPushButton(build_module_root)
        self.check_scons_button.setObjectName(u"check_scons_button")

        self.verticalLayout_2.addWidget(self.check_scons_button)

        self.install_scons_button = QPushButton(build_module_root)
        self.install_scons_button.setObjectName(u"install_scons_button")

        self.verticalLayout_2.addWidget(self.install_scons_button)

        self.update_scons_button = QPushButton(build_module_root)
        self.update_scons_button.setObjectName(u"update_scons_button")

        self.verticalLayout_2.addWidget(self.update_scons_button)

        self.build_button = QPushButton(build_module_root)
        self.build_button.setObjectName(u"build_button")

        self.verticalLayout_2.addWidget(self.build_button)


        self.retranslateUi(build_module_root)

        QMetaObject.connectSlotsByName(build_module_root)
    # setupUi

    def retranslateUi(self, build_module_root):
        build_module_root.setWindowTitle(QCoreApplication.translate("build_module_root", u"Form", None))
        self.check_scons_button.setText(QCoreApplication.translate("build_module_root", u"Check Scons", None))
        self.install_scons_button.setText(QCoreApplication.translate("build_module_root", u"Install Scons", None))
        self.update_scons_button.setText(QCoreApplication.translate("build_module_root", u"PushButton", None))
        self.build_button.setText(QCoreApplication.translate("build_module_root", u"Build", None))
    # retranslateUi


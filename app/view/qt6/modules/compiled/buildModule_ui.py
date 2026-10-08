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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_build_module_root(object):
    def setupUi(self, build_module_root):
        if not build_module_root.objectName():
            build_module_root.setObjectName(u"build_module_root")
        build_module_root.resize(606, 284)
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

        self.line = QFrame(build_module_root)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label = QLabel(build_module_root)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.optimization_level_label = QLabel(build_module_root)
        self.optimization_level_label.setObjectName(u"optimization_level_label")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.optimization_level_label)

        self.optimization_level_comboBox = QComboBox(build_module_root)
        self.optimization_level_comboBox.addItem("")
        self.optimization_level_comboBox.addItem("")
        self.optimization_level_comboBox.addItem("")
        self.optimization_level_comboBox.addItem("")
        self.optimization_level_comboBox.addItem("")
        self.optimization_level_comboBox.addItem("")
        self.optimization_level_comboBox.setObjectName(u"optimization_level_comboBox")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.optimization_level_comboBox)


        self.gridLayout.addLayout(self.formLayout_4, 1, 1, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.threads_label = QLabel(build_module_root)
        self.threads_label.setObjectName(u"threads_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.threads_label)

        self.threads_spinBox = QSpinBox(build_module_root)
        self.threads_spinBox.setObjectName(u"threads_spinBox")
        self.threads_spinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.threads_spinBox.setValue(1)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.threads_spinBox)


        self.gridLayout.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.debug_symbols_checkBox = QCheckBox(build_module_root)
        self.debug_symbols_checkBox.setObjectName(u"debug_symbols_checkBox")

        self.gridLayout.addWidget(self.debug_symbols_checkBox, 2, 1, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.target_label = QLabel(build_module_root)
        self.target_label.setObjectName(u"target_label")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.target_label)

        self.target_comboBox = QComboBox(build_module_root)
        self.target_comboBox.addItem("")
        self.target_comboBox.addItem("")
        self.target_comboBox.addItem("")
        self.target_comboBox.setObjectName(u"target_comboBox")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.target_comboBox)


        self.gridLayout.addLayout(self.formLayout_3, 2, 0, 1, 1)

        self.dev_build_checkBox = QCheckBox(build_module_root)
        self.dev_build_checkBox.setObjectName(u"dev_build_checkBox")

        self.gridLayout.addWidget(self.dev_build_checkBox, 0, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.platformLabel = QLabel(build_module_root)
        self.platformLabel.setObjectName(u"platformLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.platformLabel)

        self.platform_comboBox = QComboBox(build_module_root)
        self.platform_comboBox.addItem("")
        self.platform_comboBox.addItem("")
        self.platform_comboBox.addItem("")
        self.platform_comboBox.addItem("")
        self.platform_comboBox.addItem("")
        self.platform_comboBox.addItem("")
        self.platform_comboBox.setObjectName(u"platform_comboBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.platform_comboBox)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

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
        self.update_scons_button.setText(QCoreApplication.translate("build_module_root", u"Update Scons", None))
        self.label.setText(QCoreApplication.translate("build_module_root", u"Command Line Options", None))
        self.optimization_level_label.setText(QCoreApplication.translate("build_module_root", u"Optimization Level", None))
        self.optimization_level_comboBox.setItemText(0, QCoreApplication.translate("build_module_root", u"speed_trace", None))
        self.optimization_level_comboBox.setItemText(1, QCoreApplication.translate("build_module_root", u"speed", None))
        self.optimization_level_comboBox.setItemText(2, QCoreApplication.translate("build_module_root", u"size", None))
        self.optimization_level_comboBox.setItemText(3, QCoreApplication.translate("build_module_root", u"size_extra", None))
        self.optimization_level_comboBox.setItemText(4, QCoreApplication.translate("build_module_root", u"debug", None))
        self.optimization_level_comboBox.setItemText(5, QCoreApplication.translate("build_module_root", u"none", None))

        self.threads_label.setText(QCoreApplication.translate("build_module_root", u"Threads", None))
        self.debug_symbols_checkBox.setText(QCoreApplication.translate("build_module_root", u"Debug Symbols", None))
        self.target_label.setText(QCoreApplication.translate("build_module_root", u"Target", None))
        self.target_comboBox.setItemText(0, QCoreApplication.translate("build_module_root", u"editor", None))
        self.target_comboBox.setItemText(1, QCoreApplication.translate("build_module_root", u"template_debug", None))
        self.target_comboBox.setItemText(2, QCoreApplication.translate("build_module_root", u"template_release", None))

        self.target_comboBox.setCurrentText("")
        self.target_comboBox.setPlaceholderText(QCoreApplication.translate("build_module_root", u"target", None))
        self.dev_build_checkBox.setText(QCoreApplication.translate("build_module_root", u"Dev Build", None))
        self.platformLabel.setText(QCoreApplication.translate("build_module_root", u"Platform", None))
        self.platform_comboBox.setItemText(0, QCoreApplication.translate("build_module_root", u"windows", None))
        self.platform_comboBox.setItemText(1, QCoreApplication.translate("build_module_root", u"ios", None))
        self.platform_comboBox.setItemText(2, QCoreApplication.translate("build_module_root", u"linuxbsd", None))
        self.platform_comboBox.setItemText(3, QCoreApplication.translate("build_module_root", u"macos", None))
        self.platform_comboBox.setItemText(4, QCoreApplication.translate("build_module_root", u"android", None))
        self.platform_comboBox.setItemText(5, QCoreApplication.translate("build_module_root", u"web", None))

        self.build_button.setText(QCoreApplication.translate("build_module_root", u"Build", None))
    # retranslateUi


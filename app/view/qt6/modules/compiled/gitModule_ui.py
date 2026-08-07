# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gitModule.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_git_module_root(object):
    def setupUi(self, git_module_root):
        if not git_module_root.objectName():
            git_module_root.setObjectName(u"git_module_root")
        git_module_root.resize(400, 205)
        git_module_root.setMinimumSize(QSize(200, 200))
        self.verticalLayout_2 = QVBoxLayout(git_module_root)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.debugLayout = QFormLayout()
        self.debugLayout.setObjectName(u"debugLayout")
        self.debugLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.debugLayout.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)
        self.debugLayout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.debugLabel = QLabel(git_module_root)
        self.debugLabel.setObjectName(u"debugLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debugLabel.sizePolicy().hasHeightForWidth())
        self.debugLabel.setSizePolicy(sizePolicy)
        self.debugLabel.setMinimumSize(QSize(100, 20))
        self.debugLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.debugLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.debugLabel)

        self.debugCheckBox = QCheckBox(git_module_root)
        self.debugCheckBox.setObjectName(u"debugCheckBox")
        self.debugCheckBox.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.debugCheckBox.sizePolicy().hasHeightForWidth())
        self.debugCheckBox.setSizePolicy(sizePolicy1)
        self.debugCheckBox.setMinimumSize(QSize(100, 0))
        self.debugCheckBox.setChecked(True)
        self.debugCheckBox.setTristate(False)

        self.debugLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.debugCheckBox)


        self.verticalLayout_2.addLayout(self.debugLayout)

        self.checkGitButton = QPushButton(git_module_root)
        self.checkGitButton.setObjectName(u"checkGitButton")

        self.verticalLayout_2.addWidget(self.checkGitButton)

        self.line = QFrame(git_module_root)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.git_config_layout = QVBoxLayout()
        self.git_config_layout.setObjectName(u"git_config_layout")
        self.git_data_layout = QFormLayout()
        self.git_data_layout.setObjectName(u"git_data_layout")
        self.email_label = QLabel(git_module_root)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.email_label.sizePolicy().hasHeightForWidth())
        self.email_label.setSizePolicy(sizePolicy2)
        self.email_label.setMinimumSize(QSize(100, 0))
        self.email_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.git_data_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.email_label)

        self.email_line_edit = QLineEdit(git_module_root)
        self.email_line_edit.setObjectName(u"email_line_edit")
        self.email_line_edit.setEnabled(False)

        self.git_data_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.email_line_edit)

        self.user_name_label = QLabel(git_module_root)
        self.user_name_label.setObjectName(u"user_name_label")
        self.user_name_label.setEnabled(False)
        self.user_name_label.setMinimumSize(QSize(100, 0))
        self.user_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.git_data_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.user_name_label)

        self.user_name_line_edit = QLineEdit(git_module_root)
        self.user_name_line_edit.setObjectName(u"user_name_line_edit")
        self.user_name_line_edit.setEnabled(False)

        self.git_data_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.user_name_line_edit)


        self.git_config_layout.addLayout(self.git_data_layout)

        self.configure_git_button = QPushButton(git_module_root)
        self.configure_git_button.setObjectName(u"configure_git_button")
        self.configure_git_button.setEnabled(False)

        self.git_config_layout.addWidget(self.configure_git_button)


        self.verticalLayout_2.addLayout(self.git_config_layout)

        self.line_2 = QFrame(git_module_root)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)


        self.retranslateUi(git_module_root)

        QMetaObject.connectSlotsByName(git_module_root)
    # setupUi

    def retranslateUi(self, git_module_root):
        git_module_root.setWindowTitle(QCoreApplication.translate("git_module_root", u"Form", None))
        self.debugLabel.setText(QCoreApplication.translate("git_module_root", u"Debug Mode", None))
        self.checkGitButton.setText(QCoreApplication.translate("git_module_root", u"Check Git Status", None))
        self.email_label.setText(QCoreApplication.translate("git_module_root", u"Email", None))
        self.user_name_label.setText(QCoreApplication.translate("git_module_root", u"User Name", None))
        self.configure_git_button.setText(QCoreApplication.translate("git_module_root", u"Configure Git User", None))
    # retranslateUi


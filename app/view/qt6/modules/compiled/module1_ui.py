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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_gitDataRoot(object):
    def setupUi(self, gitDataRoot):
        if not gitDataRoot.objectName():
            gitDataRoot.setObjectName(u"gitDataRoot")
        gitDataRoot.resize(400, 200)
        gitDataRoot.setMinimumSize(QSize(200, 200))
        self.verticalLayout_2 = QVBoxLayout(gitDataRoot)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.debugLabel = QLabel(gitDataRoot)
        self.debugLabel.setObjectName(u"debugLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debugLabel.sizePolicy().hasHeightForWidth())
        self.debugLabel.setSizePolicy(sizePolicy)
        self.debugLabel.setMinimumSize(QSize(100, 20))
        self.debugLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.debugLabel)

        self.debugCheckBox = QCheckBox(gitDataRoot)
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

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.debugCheckBox)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.checkGitButton = QPushButton(gitDataRoot)
        self.checkGitButton.setObjectName(u"checkGitButton")

        self.verticalLayout_2.addWidget(self.checkGitButton)

        self.line = QFrame(gitDataRoot)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.email_label = QLabel(gitDataRoot)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.email_label.sizePolicy().hasHeightForWidth())
        self.email_label.setSizePolicy(sizePolicy2)
        self.email_label.setMinimumSize(QSize(100, 0))
        self.email_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.email_label)

        self.email_line_edit = QLineEdit(gitDataRoot)
        self.email_line_edit.setObjectName(u"email_line_edit")
        self.email_line_edit.setEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.email_line_edit)

        self.user_name_label = QLabel(gitDataRoot)
        self.user_name_label.setObjectName(u"user_name_label")
        self.user_name_label.setEnabled(False)
        self.user_name_label.setMinimumSize(QSize(100, 0))
        self.user_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.user_name_label)

        self.user_name_line_edit = QLineEdit(gitDataRoot)
        self.user_name_line_edit.setObjectName(u"user_name_line_edit")
        self.user_name_line_edit.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.user_name_line_edit)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.configure_git_button = QPushButton(gitDataRoot)
        self.configure_git_button.setObjectName(u"configure_git_button")
        self.configure_git_button.setEnabled(False)

        self.verticalLayout.addWidget(self.configure_git_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.branchesLabel = QLabel(gitDataRoot)
        self.branchesLabel.setObjectName(u"branchesLabel")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.branchesLabel)

        self.branchesComboBox = QComboBox(gitDataRoot)
        self.branchesComboBox.setObjectName(u"branchesComboBox")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.branchesComboBox)


        self.verticalLayout_2.addLayout(self.formLayout_3)


        self.retranslateUi(gitDataRoot)

        QMetaObject.connectSlotsByName(gitDataRoot)
    # setupUi

    def retranslateUi(self, gitDataRoot):
        gitDataRoot.setWindowTitle(QCoreApplication.translate("gitDataRoot", u"Form", None))
        self.debugLabel.setText(QCoreApplication.translate("gitDataRoot", u"Debug Mode", None))
        self.checkGitButton.setText(QCoreApplication.translate("gitDataRoot", u"Check Git Status", None))
        self.email_label.setText(QCoreApplication.translate("gitDataRoot", u"Email", None))
        self.user_name_label.setText(QCoreApplication.translate("gitDataRoot", u"User Name", None))
        self.configure_git_button.setText(QCoreApplication.translate("gitDataRoot", u"Configure Git User", None))
        self.branchesLabel.setText(QCoreApplication.translate("gitDataRoot", u"Branches", None))
    # retranslateUi


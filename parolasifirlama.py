# Form implementation generated from reading ui file 'parolasifirlama.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class parolasifirlama(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 586)
        Form.setStyleSheet("QWidget#Form{background-color: rgb(62, 158, 132);\n"
"border:none;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.parolasifirlamawidget = QtWidgets.QWidget(parent=Form)
        self.parolasifirlamawidget.setObjectName("parolasifirlamawidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.parolasifirlamawidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(parent=self.parolasifirlamawidget)
        self.groupBox.setStyleSheet("QGroupBox#groupBox{\n"
"    background-image: url(:/images/lblackwolf_Make_a_169_simple_and_transparent_background_with_ve_366a338a-9c89-4586-8cab-ff21b2a2a80e-removebg-preview.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"background-color: rgb(62, 158, 132);\n"
"border:none;\n"
"\n"
"}\n"
"QGroupBox{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(500, 0))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 27, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(500, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 116))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 84, 87);\n"
"margin:20 75 35 75px;\n"
"border-top-right-radius:15px 15px;\n"
"border-bottom-left-radius:15px 15px;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(0, 150, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(500, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(800, 16777215))
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 255,0);\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, 2)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 66))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(255, 255, 255,200);\n"
"border-top-left-radius:10px 10px;\n"
"border-bottom-right-radius:10px 10px;\n"
"margin-left:40px;\n"
"margin-right:40px;\n"
"margin-top:20px;")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(500, 0))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(500, 0))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"QPushButton#pushButton_3{\n"
"background-color: rgba(255, 255, 255,255);\n"
"margin:0 150 0 150px;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 255));\n"
"background-color: rgb(143, 209, 102);\n"
"border-top-right-radius:15px 15px;\n"
"border-bottom-left-radius:15px 15px;\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"background-color: rgba(255, 255, 255,255);\n"
"margin-left:150px;\n"
"margin-right:150px;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 255));\n"
"background-color: rgb(217, 217, 217);\n"
"border-top-right-radius:15px 15px;\n"
"border-bottom-left-radius:15px 15px;\n"
"padding-bottom:5px;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.widget_5)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.verticalLayout_2.addWidget(self.parolasifirlamawidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PAROLA SIFIRLAMA"))
        self.lineEdit.setPlaceholderText(_translate("Form", "E-posta Adresi /  Kullanıcı Adı"))
        self.pushButton_3.setText(_translate("Form", "GÖNDER"))

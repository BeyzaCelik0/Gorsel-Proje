# Form implementation generated from reading ui file 'randevu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class randevu(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(458, 518)
        Form.setMaximumSize(QtCore.QSize(458, 638))
        Form.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(parent=Form)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 150))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_2.setStyleSheet("border-image: url(:/images/cikis.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_5.setMinimumSize(QtCore.QSize(300, 100))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(300, 100))
        self.label.setMaximumSize(QtCore.QSize(99999, 100))
        self.label.setStyleSheet("background-color: rgb(200, 0, 0);\n"
"border-radius: 15px;\n"
"color:white;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_3.addWidget(self.widget_5)
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox.setMinimumSize(QtCore.QSize(440, 350))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_3.addItem(spacerItem1)
        self.widget_3 = QtWidgets.QWidget(parent=self.groupBox)
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color: rgba(255, 255, 255,200);\n"
"border-radius:15px;\n"
"\n"
"\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(parent=self.widget_3)
        self.comboBox.setStyleSheet("background-color: rgba(207, 207, 207,70);\n"
"color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(parent=self.groupBox)
        self.widget_4.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(255, 255, 255);")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setStyleSheet("background-color: rgba(255, 255, 255,200);\n"
"border-radius:15px;\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.widget_4)
        self.dateEdit.setStyleSheet("background-color: rgba(207, 207, 207,70);\n"
"color: rgb(0, 0, 0);")
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.verticalLayout_3.addWidget(self.widget_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_3.addItem(spacerItem2)
        self.widget_7 = QtWidgets.QWidget(parent=self.groupBox)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 75))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color: rgb(200, 0, 0);\n"
"border-radius: 15px;\n"
"color:white;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"background-color: rgb(130, 130, 130);\n"
"border-radius:15px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.widget_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.groupBox, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "RANDEVU AL"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Diyetisyen"))
        self.comboBox.setItemText(0, _translate("Form", "a"))
        self.comboBox.setItemText(1, _translate("Form", "b"))
        self.comboBox.setItemText(2, _translate("Form", "c"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Tarih"))
        self.pushButton.setText(_translate("Form", "Randevu Ara"))

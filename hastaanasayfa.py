# Form implementation generated from reading ui file 'beyzaanasayfa.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class hastaanasayfa(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(818, 587)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.widget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 47)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(70, 70))
        self.widget_4.setMaximumSize(QtCore.QSize(70, 70))
        self.widget_4.setSizeIncrement(QtCore.QSize(70, 70))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_2.setStyleSheet("border-image: url(:/profil/profil.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(400, 150))
        self.pushButton.setMaximumSize(QtCore.QSize(400, 150))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color: rgba(75, 75, 75,255);\n"
"border-radius: 15px;\n"
"color:white;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color: rgba(75, 75, 75,220);\n"
"border-radius: 15px;\n"
"color:white;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"background-color: rgba(75, 75, 75,215);\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(400, 150))
        self.pushButton_4.setMaximumSize(QtCore.QSize(400, 150))
        self.pushButton_4.setStyleSheet("\n"
"QPushButton#pushButton_4{\n"
"background-color: rgba(0, 177, 177,255);\n"
"border-radius: 15px;\n"
"color:white;\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"background-color: rgba(0, 177, 177,215);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"background-color: rgba(0, 177, 177,200);\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(400, 150))
        self.pushButton_5.setMaximumSize(QtCore.QSize(400, 150))
        self.pushButton_5.setStyleSheet("\n"
"QPushButton#pushButton_5{\n"
"background-color: rgba(200, 0, 0,255);\n"
"border-radius: 15px;\n"
"color:white;\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
"background-color: rgba(200, 0, 0,215);\n"
"border-radius: 15px;\n"
"color:white;\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"background-color: rgba(200, 0, 0,200);\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.widget_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.widget_3)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableView = QtWidgets.QTableView(parent=self.tab_3)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 371, 521))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableView_2 = QtWidgets.QTableView(parent=self.tab_4)
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 561, 591))
        self.tableView_2.setObjectName("tableView_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Hesaplamalarım"))
        self.pushButton_4.setText(_translate("Form", "Diyetlerim"))
        self.pushButton_5.setText(_translate("Form", "Randevu Al"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Randevularım"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Geçmiş Randevularım"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(523, 503)
        app_icon = QtGui.QIcon()
        app_icon.addFile('static/16.png', QtCore.QSize(16, 16))
        app_icon.addFile('static/24.png', QtCore.QSize(24, 24))
        app_icon.addFile('static/32.png', QtCore.QSize(32, 32))
        app_icon.addFile('static/32.png', QtCore.QSize(48, 48))
        app_icon.addFile('static/256.png', QtCore.QSize(256, 256))
        MainWindow.setWindowIcon(app_icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 9, 501, 481))
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 12, 471, 431))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_zipname = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_zipname.setEnabled(False)
        self.checkBox_zipname.setObjectName("checkBox_zipname")
        self.gridLayout_3.addWidget(self.checkBox_zipname, 11, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 6, 0, 1, 1)
        self.checkBox_zipfiles = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_zipfiles.setObjectName("checkBox_zipfiles")
        self.gridLayout_3.addWidget(self.checkBox_zipfiles, 9, 0, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_3.addWidget(self.pushButton_start, 13, 0, 1, 1)
        self.lineEdit_zipname = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_zipname.setEnabled(False)
        self.lineEdit_zipname.setObjectName("lineEdit_zipname")
        self.gridLayout_3.addWidget(self.lineEdit_zipname, 12, 0, 1, 1)
        self.checkBox_email = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_email.setTristate(False)
        self.checkBox_email.setObjectName("checkBox_email")
        self.gridLayout_3.addWidget(self.checkBox_email, 10, 0, 1, 1)
        self.lineEdit_testsuitetorun = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_testsuitetorun.setObjectName("lineEdit_testsuitetorun")
        self.gridLayout_3.addWidget(self.lineEdit_testsuitetorun, 3, 0, 1, 1)
        self.lineEdit_projectxml = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_projectxml.setObjectName("lineEdit_projectxml")
        self.gridLayout_3.addWidget(self.lineEdit_projectxml, 5, 0, 1, 1)
        self.lineEdit_outputpath = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_outputpath.setObjectName("lineEdit_outputpath")
        self.gridLayout_3.addWidget(self.lineEdit_outputpath, 7, 0, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout_3.addWidget(self.pushButton_exit, 14, 0, 1, 1)
        self.lineEdit_testrunnerbat = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_testrunnerbat.setObjectName("lineEdit_testrunnerbat")
        self.gridLayout_3.addWidget(self.lineEdit_testrunnerbat, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)
        self.checkBox_xml = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_xml.setObjectName("checkBox_xml")
        self.gridLayout_3.addWidget(self.checkBox_xml, 8, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 471, 431))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 6, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 4, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 8, 0, 1, 1)
        self.lineEdit_toemail = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_toemail.setObjectName("lineEdit_toemail")
        self.gridLayout_4.addWidget(self.lineEdit_toemail, 3, 0, 1, 1)
        self.lineEdit_fromemail = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_fromemail.setObjectName("lineEdit_fromemail")
        self.gridLayout_4.addWidget(self.lineEdit_fromemail, 1, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout_4.addWidget(self.lineEdit_password, 5, 0, 1, 1)
        self.lineEdit_smtpserver = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_smtpserver.setObjectName("lineEdit_smtpserver")
        self.gridLayout_4.addWidget(self.lineEdit_smtpserver, 7, 0, 1, 1)
        self.lineEdit_smtpport = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_smtpport.setObjectName("lineEdit_smtpport")
        self.gridLayout_4.addWidget(self.lineEdit_smtpport, 9, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SoapUI Report Generator"))
        self.checkBox_zipname.setText(_translate("MainWindow", "Cutom zip name"))
        self.label_13.setText(_translate("MainWindow", "Raport Output path"))
        self.checkBox_zipfiles.setText(_translate("MainWindow", "Pack test results into a zipfile"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.lineEdit_zipname.setText(_translate("MainWindow", "Name scheme \"name.zip\""))
        self.checkBox_email.setText(_translate("MainWindow", "Send Email with attached results"))
        self.lineEdit_testsuitetorun.setText(_translate("MainWindow", "CountryInfoServiceSoapBinding12 TestSuite"))
        self.lineEdit_projectxml.setText(_translate("MainWindow", "C:\\Users\\Daniel\\Desktop\\SOAPUIInzynier\\CountryInfoService-soapui-project.xml"))
        self.lineEdit_outputpath.setText(_translate("MainWindow", "C:\\Users\\Daniel\\Desktop\\reports"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.lineEdit_testrunnerbat.setText(_translate("MainWindow", "C:\\Program Files (x86)\\SmartBear\\SoapUI-5.4.0\\bin\\testrunner.bat"))
        self.label_14.setText(_translate("MainWindow", "Path to  TestRunner.bat location"))
        self.label_11.setText(_translate("MainWindow", "Name of the TestSuite to run"))
        self.label_12.setText(_translate("MainWindow", "Path to project .xml created in SOAP UI"))
        self.checkBox_xml.setText(_translate("MainWindow", "Export all data to XML"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.label_19.setText(_translate("MainWindow", "SMTP server"))
        self.label_18.setText(_translate("MainWindow", "Password"))
        self.label_17.setText(_translate("MainWindow", "To email"))
        self.label_16.setText(_translate("MainWindow", "From email"))
        self.label_20.setText(_translate("MainWindow", "SMTP port"))
        self.lineEdit_toemail.setText(_translate("MainWindow", "kasprzak.szkola@gmail.com"))
        self.lineEdit_fromemail.setText(_translate("MainWindow", "koszalinsoapuitest@gmail.com"))
        self.lineEdit_password.setText(_translate("MainWindow", "politechnika1"))
        self.lineEdit_smtpserver.setText(_translate("MainWindow", "smtp.gmail.com"))
        self.lineEdit_smtpport.setText(_translate("MainWindow", "465"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Email Settings"))



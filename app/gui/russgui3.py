# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'russgui03.ui'
#
# Created: Sat May 03 23:44:10 2014
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(801, 590)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(620, 550, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(420, 40, 361, 391))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 560, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 440, 81, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 191, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 20, 113, 20))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(70, 80, 111, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 40, 113, 20))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 60, 113, 20))
        self.lineEdit_6.setText(_fromUtf8(""))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(450, 10, 51, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 440, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(690, 440, 81, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(690, 470, 81, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 290, 161, 271))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 180, 141, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.textEdit_2 = QtGui.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(310, 510, 251, 71))
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.textEdit_2.setAutoFillBackground(False)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(400, 490, 51, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.buttonBox, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        Dialog.setTabOrder(self.lineEdit_4, self.lineEdit_6)
        Dialog.setTabOrder(self.lineEdit_6, self.pushButton)
        Dialog.setTabOrder(self.pushButton, self.lineEdit)
        Dialog.setTabOrder(self.lineEdit, self.pushButton_2)
        Dialog.setTabOrder(self.pushButton_2, self.textEdit)
        Dialog.setTabOrder(self.textEdit, self.pushButton_3)
        Dialog.setTabOrder(self.pushButton_3, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.pushButton_5)
        Dialog.setTabOrder(self.pushButton_5, self.pushButton_6)
        Dialog.setTabOrder(self.pushButton_6, self.pushButton_7)
        Dialog.setTabOrder(self.pushButton_7, self.pushButton_4)
        Dialog.setTabOrder(self.pushButton_4, self.textEdit_2)
        Dialog.setTabOrder(self.textEdit_2, self.tableWidget)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_3.setText(_translate("Dialog", "3Add2DBlist", None))
        self.pushButton_4.setText(_translate("Dialog", "4 update DBlist", None))
        self.groupBox.setTitle(_translate("Dialog", "Add Manually", None))
        self.label_3.setText(_translate("Dialog", "Voc-DE", None))
        self.pushButton.setText(_translate("Dialog", "1Add Manu", None))
        self.label_5.setText(_translate("Dialog", "Type", None))
        self.label_4.setText(_translate("Dialog", "Voc-RU", None))
        self.label_7.setText(_translate("Dialog", "Kontext", None))
        self.label_6.setText(_translate("Dialog", "Voc List", None))
        self.pushButton_5.setText(_translate("Dialog", "5DeleteEntry", None))
        self.pushButton_6.setText(_translate("Dialog", "mk DB backup", None))
        self.pushButton_7.setText(_translate("Dialog", "load DB backup", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Add from file", None))
        self.pushButton_2.setText(_translate("Dialog", "2Add from file", None))
        self.lineEdit.setText(_translate("Dialog", "input.txt", None))
        self.label_8.setText(_translate("Dialog", "InfoBox", None))


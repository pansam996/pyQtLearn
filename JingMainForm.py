# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JingMainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(400, 300)
        self.word_label = QtWidgets.QLabel(MainForm)
        self.word_label.setGeometry(QtCore.QRect(70, 40, 161, 31))
        self.word_label.setTextFormat(QtCore.Qt.AutoText)
        self.word_label.setObjectName("word_label")
        self.bottom_openNewForm = QtWidgets.QPushButton(MainForm)
        self.bottom_openNewForm.setGeometry(QtCore.QRect(70, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bottom_openNewForm.setFont(font)
        self.bottom_openNewForm.setObjectName("bottom_openNewForm")
        self.bottom_inForm2_addLabel = QtWidgets.QPushButton(MainForm)
        self.bottom_inForm2_addLabel.setGeometry(QtCore.QRect(70, 140, 171, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bottom_inForm2_addLabel.setFont(font)
        self.bottom_inForm2_addLabel.setAutoDefault(False)
        self.bottom_inForm2_addLabel.setObjectName("bottom_inForm2_addLabel")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "JingMainForm"))
        self.word_label.setText(_translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">測試文字</span></p></body></html>"))
        self.bottom_openNewForm.setText(_translate("MainForm", "開啟新視窗"))
        self.bottom_inForm2_addLabel.setText(_translate("MainForm", "在新視窗顯示文字"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

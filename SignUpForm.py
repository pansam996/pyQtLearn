# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signUpForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpForm(object):
    def setupUi(self, SignUpForm):
        SignUpForm.setObjectName("SignUpForm")
        SignUpForm.resize(426, 368)
        self.label = QtWidgets.QLabel(SignUpForm)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(SignUpForm)
        self.splitter.setGeometry(QtCore.QRect(20, 50, 121, 301))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setTabletTracking(False)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setTabletTracking(False)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setTabletTracking(False)
        self.pushButton_4.setAcceptDrops(False)
        self.pushButton_4.setAutoFillBackground(True)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_date = QtWidgets.QLabel(SignUpForm)
        self.label_date.setGeometry(QtCore.QRect(160, 60, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.label_date_change = QtWidgets.QLabel(SignUpForm)
        self.label_date_change.setEnabled(False)
        self.label_date_change.setVisible(False)
        self.label_date_change.setGeometry(QtCore.QRect(240, 60, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_date_change.setFont(font)
        self.label_date_change.setAutoFillBackground(False)
        self.label_date_change.setScaledContents(False)
        self.label_date_change.setObjectName("label_date_change")
        self.label_session_change = QtWidgets.QLabel(SignUpForm)
        self.label_session_change.setEnabled(False)
        self.label_session_change.setVisible(False)
        self.label_session_change.setGeometry(QtCore.QRect(240, 90, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_session_change.setFont(font)
        self.label_session_change.setObjectName("label_session_change")
        self.label_session = QtWidgets.QLabel(SignUpForm)
        self.label_session.setGeometry(QtCore.QRect(160, 90, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_session.setFont(font)
        self.label_session.setObjectName("label_session")
        self.label_height = QtWidgets.QLabel(SignUpForm)
        self.label_height.setGeometry(QtCore.QRect(160, 120, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_height.setFont(font)
        self.label_height.setObjectName("label_height")
        self.label_height_change = QtWidgets.QLabel(SignUpForm)
        self.label_height_change.setEnabled(False)
        self.label_height_change.setVisible(False)
        self.label_height_change.setGeometry(QtCore.QRect(240, 120, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_height_change.setFont(font)
        self.label_height_change.setObjectName("label_height_change")
        self.label_openNum_change = QtWidgets.QLabel(SignUpForm)
        self.label_openNum_change.setEnabled(False)
        self.label_openNum_change.setVisible(False)
        self.label_openNum_change.setGeometry(QtCore.QRect(240, 150, 61, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_openNum_change.setFont(font)
        self.label_openNum_change.setObjectName("label_openNum_change")
        self.label_openNum = QtWidgets.QLabel(SignUpForm)
        self.label_openNum.setGeometry(QtCore.QRect(160, 150, 61, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_openNum.setFont(font)
        self.label_openNum.setObjectName("label_openNum")
        self.label_alreadyBookNum = QtWidgets.QLabel(SignUpForm)
        self.label_alreadyBookNum.setGeometry(QtCore.QRect(160, 180, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_alreadyBookNum.setFont(font)
        self.label_alreadyBookNum.setObjectName("label_alreadyBookNum")
        self.label_AlreadyBookNumChange = QtWidgets.QLabel(SignUpForm)
        self.label_AlreadyBookNumChange.setEnabled(False)
        self.label_AlreadyBookNumChange.setVisible(False)
        self.label_AlreadyBookNumChange.setGeometry(QtCore.QRect(240, 180, 61, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_AlreadyBookNumChange.setFont(font)
        self.label_AlreadyBookNumChange.setObjectName("label_AlreadyBookNumChange")
        self.label_fee_change = QtWidgets.QLabel(SignUpForm)
        self.label_fee_change.setEnabled(False)
        self.label_fee_change.setVisible(False)
        self.label_fee_change.setGeometry(QtCore.QRect(240, 210, 61, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_fee_change.setFont(font)
        self.label_fee_change.setObjectName("label_fee_change")
        self.label_fee = QtWidgets.QLabel(SignUpForm)
        self.label_fee.setGeometry(QtCore.QRect(160, 210, 51, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_fee.setFont(font)
        self.label_fee.setObjectName("label_fee")
        self.label_session_time_change = QtWidgets.QLabel(SignUpForm)
        self.label_session_time_change.setEnabled(False)
        self.label_session_time_change.setVisible(False)
        self.label_session_time_change.setGeometry(QtCore.QRect(300, 90, 111, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_session_time_change.setFont(font)
        self.label_session_time_change.setObjectName("label_session_time_change")
        self.lineEdit_SignInName = QtWidgets.QLineEdit(SignUpForm)
        self.lineEdit_SignInName.setGeometry(QtCore.QRect(322, 280, 81, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.lineEdit_SignInName.setFont(font)
        self.lineEdit_SignInName.setText("")
        self.lineEdit_SignInName.setObjectName("lineEdit_SignInName")
        self.lineEdit_phoneNum = QtWidgets.QLineEdit(SignUpForm)
        self.lineEdit_phoneNum.setGeometry(QtCore.QRect(322, 330, 81, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.lineEdit_phoneNum.setFont(font)
        self.lineEdit_phoneNum.setText("")
        self.lineEdit_phoneNum.setObjectName("lineEdit_phoneNum")
        self.radioButton_boy = QtWidgets.QRadioButton(SignUpForm)
        self.radioButton_boy.setGeometry(QtCore.QRect(290, 305, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.radioButton_boy.setFont(font)
        self.radioButton_boy.setObjectName("radioButton_boy")
        self.radioButton_girl = QtWidgets.QRadioButton(SignUpForm)
        self.radioButton_girl.setGeometry(QtCore.QRect(340, 305, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.radioButton_girl.setFont(font)
        self.radioButton_girl.setObjectName("radioButton_girl")
        self.label_SignIn_name = QtWidgets.QLabel(SignUpForm)
        self.label_SignIn_name.setGeometry(QtCore.QRect(290, 280, 31, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_SignIn_name.setFont(font)
        self.label_SignIn_name.setObjectName("label_SignIn_name")
        self.label_phone = QtWidgets.QLabel(SignUpForm)
        self.label_phone.setGeometry(QtCore.QRect(290, 330, 31, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.pushButton_SignIn = QtWidgets.QPushButton(SignUpForm)
        self.pushButton_SignIn.setGeometry(QtCore.QRect(160, 280, 111, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SignIn.setFont(font)
        self.pushButton_SignIn.setObjectName("pushButton_SignIn")
        self.label_bookIsSuccess = QtWidgets.QLabel(SignUpForm)
        self.label_bookIsSuccess.setEnabled(False)
        self.label_bookIsSuccess.setVisible(False)
        self.label_bookIsSuccess.setGeometry(QtCore.QRect(310, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_bookIsSuccess.setFont(font)
        self.label_bookIsSuccess.setObjectName("label_bookIsSuccess")

        self.retranslateUi(SignUpForm)
        QtCore.QMetaObject.connectSlotsByName(SignUpForm)

    def retranslateUi(self, SignUpForm):
        _translate = QtCore.QCoreApplication.translate
        SignUpForm.setWindowTitle(_translate("SignUpForm", "SignUpForm"))
        self.label.setText(_translate("SignUpForm", "TextLabel"))
        self.pushButton.setText(_translate("SignUpForm", "早上場"))
        self.pushButton_2.setText(_translate("SignUpForm", "下午場"))
        self.pushButton_3.setText(_translate("SignUpForm", "晚上場"))
        self.pushButton_4.setText(_translate("SignUpForm", "宵夜場"))
        self.label_date.setText(_translate("SignUpForm", "日期："))
        self.label_date_change.setText(_translate("SignUpForm", "日期"))
        self.label_session_change.setText(_translate("SignUpForm", "早上場"))
        self.label_session.setText(_translate("SignUpForm", "場次："))
        self.label_height.setText(_translate("SignUpForm", "網高："))
        self.label_height_change.setText(_translate("SignUpForm", "243男網"))
        self.label_openNum_change.setText(_translate("SignUpForm", "18"))
        self.label_openNum.setText(_translate("SignUpForm", "開放人數："))
        self.label_alreadyBookNum.setText(_translate("SignUpForm", "已報名人數："))
        self.label_AlreadyBookNumChange.setText(_translate("SignUpForm", "0"))
        self.label_fee_change.setText(_translate("SignUpForm", "150"))
        self.label_fee.setText(_translate("SignUpForm", "價格："))
        self.label_session_time_change.setText(_translate("SignUpForm", "0800 - 1200"))
        self.radioButton_boy.setText(_translate("SignUpForm", "男"))
        self.radioButton_girl.setText(_translate("SignUpForm", "女"))
        self.label_SignIn_name.setText(_translate("SignUpForm", "姓名"))
        self.label_phone.setText(_translate("SignUpForm", "電話"))
        self.pushButton_SignIn.setText(_translate("SignUpForm", "報名"))
        self.label_bookIsSuccess.setText(_translate("SignUpForm", "報名成功!!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpForm = QtWidgets.QWidget()
    ui = Ui_SignUpForm()
    ui.setupUi(SignUpForm)
    SignUpForm.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\1\Downloads\untitled.ui'
#
# Created: Wed Feb  3 22:25:48 2021
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(815, 459)
        Dialog.setMouseTracking(True)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-visual-studio-25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: #2B2B2B;\n"
"")
        Dialog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 30, 41, 441))
        self.widget.setStyleSheet("background-color: #212121;")
        self.widget.setObjectName("widget")
        self.pushButton_10 = QtGui.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 0, 41, 61))
        self.pushButton_10.setStyleSheet("color: #BFBFBF;")
        self.pushButton_10.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_10.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons8-search-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setAutoDefault(False)
        self.pushButton_10.setDefault(False)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_9 = QtGui.QPushButton(self.widget)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 60, 41, 61))
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_9.setStyleSheet("color: #BFBFBF;")
        self.pushButton_9.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons8-file-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtGui.QPushButton(self.widget)
        self.pushButton_11.setGeometry(QtCore.QRect(0, 320, 41, 61))
        self.pushButton_11.setStyleSheet("color: #BFBFBF;")
        self.pushButton_11.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons8-contacts-26.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtGui.QPushButton(self.widget)
        self.pushButton_12.setGeometry(QtCore.QRect(0, 380, 41, 61))
        self.pushButton_12.setStyleSheet("color: #BFBFBF;")
        self.pushButton_12.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons8-settings-25.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon4)
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setDefault(False)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 811, 31))
        self.frame.setStyleSheet("background-color: #1E1E1E;")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons8-visual-studio-25.png"))
        self.label.setObjectName("label")
        self.pushButton_8 = QtGui.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 0, 51, 31))
        self.pushButton_8.setStyleSheet("float: right;\n"
"margin-right: 3%;\n"
"margin-top: 5px;\n"
"padding: 5px 9px;\n"
"font-size: 1.2em;\n"
"-moz-border-radius: 5px;\n"
"-webkit-border-radius: 5px;\n"
"text-shadow:#454545 0 0 2px;\n"
"border-bottom: 4px solid rgba(217, 101, 80, 1);\n"
"background: #2B2B2B;\n"
"color: white;\n"
"font-family: \'Roboto Slab\', serif;")
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_5 = QtGui.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 0, 41, 31))
        self.pushButton_5.setStyleSheet("float: right;\n"
"margin-right: 3%;\n"
"margin-top: 5px;\n"
"padding: 5px 9px;\n"
"font-size: 1.2em;\n"
"-moz-border-radius: 5px;\n"
"-webkit-border-radius: 5px;\n"
"text-shadow:#454545 0 0 2px;\n"
"border-bottom: 4px solid rgba(217, 101, 80, 1);\n"
"background: #2B2B2B;\n"
"color: white;\n"
"font-family: \'Roboto Slab\', serif;")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 0, 41, 31))
        self.pushButton.setStyleSheet("float: right;\n"
"margin-right: 3%;\n"
"margin-top: 5px;\n"
"padding: 5px 9px;\n"
"font-size: 1.2em;\n"
"-moz-border-radius: 5px;\n"
"-webkit-border-radius: 5px;\n"
"text-shadow:#454545 0 0 2px;\n"
"border-bottom: 4px solid rgba(217, 101, 80, 1);\n"
"background: #2B2B2B;\n"
"color: white;\n"
"font-family: \'Roboto Slab\', serif;")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 0, 41, 31))
        self.pushButton_2.setStyleSheet("float: right;\n"
"margin-right: 3%;\n"
"margin-top: 5px;\n"
"padding: 5px 9px;\n"
"font-size: 1.2em;\n"
"-moz-border-radius: 5px;\n"
"-webkit-border-radius: 5px;\n"
"text-shadow:#454545 0 0 2px;\n"
"border-bottom: 4px solid rgba(217, 101, 80, 1);\n"
"background: #2B2B2B;\n"
"color: white;\n"
"font-family: \'Roboto Slab\', serif;")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 0, 71, 31))
        self.pushButton_3.setStyleSheet("float: right;\n"
"margin-right: 3%;\n"
"margin-top: 5px;\n"
"padding: 5px 9px;\n"
"font-size: 1.2em;\n"
"-moz-border-radius: 5px;\n"
"-webkit-border-radius: 5px;\n"
"text-shadow:#454545 0 0 2px;\n"
"border-bottom: 4px solid rgba(217, 101, 80, 1);\n"
"background: #2B2B2B;\n"
"color: white;\n"
"font-family: \'Roboto Slab\', serif;")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 0, 51, 31))
        self.pushButton_4.setStyleSheet("float: right;\n"
"margin-right: 3%;\n"
"margin-top: 5px;\n"
"padding: 5px 9px;\n"
"font-size: 1.2em;\n"
"-moz-border-radius: 5px;\n"
"-webkit-border-radius: 5px;\n"
"text-shadow:#454545 0 0 2px;\n"
"border-bottom: 4px solid rgba(217, 101, 80, 1);\n"
"background: #2B2B2B;\n"
"color: white;\n"
"font-family: \'Roboto Slab\', serif;")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 0, 51, 31))
        self.pushButton_6.setMouseTracking(True)
        self.pushButton_6.setStyleSheet("float: right;\n"
"margin-right: 3%;\n"
"margin-top: 5px;\n"
"padding: 5px 9px;\n"
"font-size: 1.2em;\n"
"-moz-border-radius: 5px;\n"
"-webkit-border-radius: 5px;\n"
"text-shadow:#454545 0 0 2px;\n"
"border-bottom: 4px solid rgba(217, 101, 80, 1);\n"
"background: #2B2B2B;\n"
"color: white;\n"
"font-family: \'Roboto Slab\', serif;")
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtGui.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 0, 71, 31))
        self.pushButton_7.setStyleSheet("float: right;\n"
"margin-right: 3%;\n"
"margin-top: 5px;\n"
"padding: 5px 9px;\n"
"font-size: 1.2em;\n"
"-moz-border-radius: 5px;\n"
"-webkit-border-radius: 5px;\n"
"text-shadow:#454545 0 0 2px;\n"
"border-bottom: 4px solid rgba(217, 101, 80, 1);\n"
"background: #2B2B2B;\n"
"color: white;\n"
"font-family: \'Roboto Slab\', serif;")
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Visual Studio Code", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Dialog", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Dialog", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Dialog", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Dialog", "Terminal", None, QtGui.QApplication.UnicodeUTF8))
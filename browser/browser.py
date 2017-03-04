# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def backward(self):
        self.webView.backward()
    def forward(self):
        self.webView.forward()
    def refresh(self):
        self.webView.refresh()
    def addressbar(self):
        print("Address")
    def home(self):
        self.webView.load(QtCore.QUrl("https://www.google.com"))
    def search(self):
        url=self.ln_addressbar.text()
        self.webView.load(QtCore.QUrl(url))
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(890, 568)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tb_backward = QtGui.QToolButton(self.centralwidget)
        self.tb_backward.setGeometry(QtCore.QRect(0, 10, 41, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_backward.setIcon(icon)
        self.tb_backward.setObjectName(_fromUtf8("tb_backward"))
        self.tb_backward.clicked.connect(self.backward)
        self.tb_refresh = QtGui.QToolButton(self.centralwidget)
        self.tb_refresh.setGeometry(QtCore.QRect(50, 10, 41, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icon/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_refresh.setIcon(icon1)
        self.tb_refresh.setObjectName(_fromUtf8("tb_refresh"))
        self.tb_refresh.clicked.connect(self.refresh)
        self.tb_forward = QtGui.QToolButton(self.centralwidget)
        self.tb_forward.setGeometry(QtCore.QRect(100, 10, 41, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icon/forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_forward.setIcon(icon2)
        self.tb_forward.setObjectName(_fromUtf8("tb_forward"))
        self.tb_forward.clicked.connect(self.forward)
        self.tb_search = QtGui.QToolButton(self.centralwidget)
        self.tb_search.setGeometry(QtCore.QRect(800, 10, 41, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icon/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_search.setIcon(icon3)
        self.tb_search.setObjectName(_fromUtf8("tb_search"))
        self.tb_search.clicked.connect(self.search)
        self.ln_addressbar = QtGui.QLineEdit(self.centralwidget)
        self.ln_addressbar.setGeometry(QtCore.QRect(200, 10, 591, 31))
        self.ln_addressbar.setObjectName(_fromUtf8("ln_addressbar"))
        self.tb_search.clicked.connect(self.search)
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(-10, 50, 851, 511))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.tb_home = QtGui.QToolButton(self.centralwidget)
        self.tb_home.setGeometry(QtCore.QRect(150, 10, 41, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icon/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_home.setIcon(icon4)
        self.tb_home.setObjectName(_fromUtf8("tb_home"))
        self.tb_home.clicked.connect(self.home)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tb_backward.setText(_translate("MainWindow", "...", None))
        self.tb_refresh.setText(_translate("MainWindow", "...", None))
        self.tb_forward.setText(_translate("MainWindow", "...", None))
        self.tb_search.setText(_translate("MainWindow", "...", None))
        self.tb_home.setText(_translate("MainWindow", "...", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-
import sys
from serial_control import SerialControl
from lqr_gui import LQRMainWindow
from PyQt6.QtCore import (QCoreApplication, QMetaObject, QRect, QObject, QThread, pyqtSignal)
from PyQt6.QtGui import (QAction)
from PyQt6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QStatusBar, QWidget, QDialog, QLineEdit, QGroupBox)


class SerialMainWindow(object):
    def __init__(self, serial):
        self.serial = serial
        self.window = QMainWindow()
        self.dialog = QDialog()
        # self.LQRWindow = LQRMainWindow(self.serial)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(418, 214)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout_2 = QAction(MainWindow)
        self.actionAbout_2.setObjectName(u"actionAbout_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.connect_test(MainWindow))

        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(lambda: self.refreshPorts())

        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.lineEdit_7 = QLineEdit(self.widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(70, 120, 31, 22))
        self.comboBox_3 = QComboBox(self.widget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(70, 240, 91, 23))
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 60, 31, 22))
        self.lineEdit_9 = QLineEdit(self.widget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(150, 120, 31, 22))
        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(110, 90, 31, 22))
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 60, 31, 22))
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 220, 58, 15))
        self.lineEdit_10 = QLineEdit(self.widget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(70, 170, 111, 22))
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 10, 201, 201))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 150, 21, 16))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 40, 21, 16))
        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(150, 90, 31, 22))
        self.lineEdit_8 = QLineEdit(self.widget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(110, 120, 31, 22))
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(70, 90, 31, 22))
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(150, 60, 31, 22))
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(250, 10, 451, 261))
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 30, 58, 15))

        self.gridLayout.addWidget(self.widget, 4, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1057, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionAbout_2)
        self.widget.hide()
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Serial Connection", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"How to use?", None))
        self.actionAbout_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:16pt;\">Baud rate</span></p></body></html>",
                                                        None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p><span style=\" font-size:16pt;\">Available ports</span></p></body></html>",
                                                      None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"31250", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"38400", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"57600", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"74880", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"115200", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Posisi 1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Posisi 2", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Posisi 3", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Set Point", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Parameter Q dan R", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output sistem", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Nilai K", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

        # initial port listing
        self.serial.serial_com_list()
        self.comboBox.addItems(self.serial.coms)

    # manual port refresh
    def refreshPorts(self):
        self.serial.serial_com_list()
        self.comboBox.clear()
        self.comboBox.addItems(self.serial.coms)

    def connect_test(self, MainWindow):
        condition = self.pushButton_2.text()
        if condition == "Connect":
            self.connectPort(MainWindow)
        elif condition == "Disconnect":
            self.closePort(MainWindow)

    def connectPort(self, MainWindow):
        self.selected_port = self.comboBox.currentText()
        try:
            self.serial.serial_connect(self.selected_port)
            self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
            MainWindow.resize(1057, 473)
            self.widget.show()
            self.runLongTask()
        except:
            self.dialog.show()

    def closePort(self, MainWindow):
        self.serial.serial_close()
        self.window.close()
        self.widget.hide()
        MainWindow.resize(418, 214)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Connect", None))

    def update_value(self, data):
        self.label_9.setText(QCoreApplication.translate("MainWindow", f"{data}", None))

    def runLongTask(self):

        self.thread = QThread()

        self.worker = Worker(self.serial)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.update_value)

        self.thread.start()


class Worker(QObject):
    def __init__(self, serial):
        super().__init__()
        self.status = True
        self.serialLQR = serial

    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        while self.status:
            data = self.serialLQR.serial_sync()
            if data:
                self.progress.emit(int(data))
                if int(data) == 4:
                    self.status = False
        self.finished.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    windows = SerialMainWindow(SerialControl())
    windows.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())

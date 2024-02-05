# -*- coding: utf-8 -*-
import sys
import serial.tools.list_ports
from scratch import Ui_MainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QLineEdit, QStatusBar, QWidget, QGroupBox)

class SerialService:
    def serialOptionMenu(self):
        self.ports = serial.tools.list_ports.comports()
        self.coms = [com[0] for com in self.ports]


class SerialMainWindow(object):
    def __init__(self):
        super().__init__()
        self.serial = SerialService()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(418, 214)
        self.actionQUit = QAction(MainWindow)
        self.actionQUit.setObjectName(u"actionQUit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout_2 = QAction(MainWindow)
        self.actionAbout_2.setObjectName(u"actionAbout_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

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

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.connectPort())

        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 418, 22))
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
        self.menuFile.addAction(self.actionQUit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionAbout_2)

        self.retranslateUi(MainWindow)
        # self.pushButton_2.clicked.connect(MainWindow.show)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Serial Connection", None))
        self.actionQUit.setText(QCoreApplication.translate("MainWindow", u"QUit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"How to use?", None))
        self.actionAbout_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:16pt;\">Baud "
                                                        u"rate</span></p></body></html>",
                                                        None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p><span style=\" "
                                                      u"font-size:16pt;\">Available ports</span></p></body></html>",
                                                      None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton.setToolTip("Refresh the available COM list")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"31250", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"38400", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"57600", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"74880", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"115200", None))
        self.comboBox_2.setToolTip("Select baud rate make sure it's the same as the microcontroller")

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton_2.setToolTip("Connect to the microcontroller")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))

        self.serial.serialOptionMenu()
        self.comboBox.addItems(self.serial.coms)

    def refreshPorts(self):
        self.serial.serialOptionMenu()
        self.comboBox.clear()
        self.comboBox.addItems(self.serial.coms)

    def connectPort(self):
        self.secondWindow = QMainWindow()
        self.LQRWindow = Ui_MainWindow()
        self.LQRWindow.setupUi(self.secondWindow)
        self.secondWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    windows = SerialMainWindow()
    windows.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())

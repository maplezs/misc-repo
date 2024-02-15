import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from serial_conn_gui import SerialMainWindow
from serial_control import SerialControl

if __name__ == "__main__":
    app = QApplication(sys.argv)
    serial = SerialControl()
    mainWindow = QMainWindow()
    windows = SerialMainWindow(serial)
    windows.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())

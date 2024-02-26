from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow
from PySide6.QtCore import Qt
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowFlags(window.windowFlags() & Qt.CustomizeWindowHint)
    window.setWindowFlags(window.windowFlags() & ~Qt.WindowMinMaxButtonsHint)
    window.show()

    # Connect the application quit method to the MainWindow's destroyed signal
    app.aboutToQuit.connect(window.close)

    sys.exit(app.exec())
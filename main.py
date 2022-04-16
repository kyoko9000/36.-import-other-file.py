import sys
# pip install pyqt5
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

from program1 import program
from program2 import program2, sub_program2
from program3.program3 import program3, sub_program3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.Button_start.clicked.connect(self.load_program)

    def load_program(self):
        a = program()
        a.sub_program_1()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

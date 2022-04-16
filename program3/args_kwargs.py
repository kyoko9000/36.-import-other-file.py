import sys
# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


def show_pic(*args, **kwargs):
    print(args)
    print(kwargs)
    if len(kwargs) > 0:
        index1 = kwargs['index1']
        print(index1)
        index2 = kwargs['index2']
        print(index2)
        index3 = kwargs['index3']
        print(index3)
    elif len(args) > 0:
        index4 = args[0]
        print(index4)


def link_pics():
    show_pic(index1=2, index2=4, index3=6)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.Button_start.clicked.connect(link_pics)
        self.uic.Button_next.clicked.connect(self.next_pic)
        self.uic.Button_back.clicked.connect(self.back_pic)
        self.i = 0

    def next_pic(self):
        if self.i < 5:
            self.i += 1
            print(self.i)
            show_pic(self.i)

    def back_pic(self):
        if self.i > 0:
            self.i -= 1
            print(self.i)
            show_pic(self.i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

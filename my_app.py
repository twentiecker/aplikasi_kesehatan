# write here a code for the main app and the first screen
from PyQt5.QtCore import Qt  # alignment
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()    

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        # init object
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)

        # init main layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)

        # set main layout
        self.setLayout(self.layout)
    
    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        print('screen kedua')
        self.hide()
        self.tw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()
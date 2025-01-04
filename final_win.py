# write here a code for the third app
from PyQt5.QtCore import Qt  # alignment
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        # init object
        self.label_index = QLabel(txt_index)
        self.label_perform = QLabel(txt_workheart)
        
        # init main layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_index, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label_perform, alignment=Qt.AlignCenter)
        
        # set main layout
        self.setLayout(self.layout)
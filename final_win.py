# write here a code for the third app
from PyQt5.QtCore import Qt  # alignment
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.results()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        # init object
        self.label_index = QLabel(txt_index + str(self.index))
        self.label_perform = QLabel(txt_workheart + self.results())
        
        # init main layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_index, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.label_perform, alignment=Qt.AlignCenter)
        
        # set main layout
        self.setLayout(self.layout)
    
    def results(self):
        self.index = (4 * (self.exp.p1 + self.exp.p2 + self.exp.p3) - 200) / 10
        if self.exp.age >= 15:
            if self.index >= 15:
                return text_res1
            elif self.index >= 11 and self.index < 15:
                return text_res2
            elif self.index >= 6 and self.index < 11:
                return text_res3
            elif self.index >= 0.5 and self.index < 6:
                return text_res4
            elif self.index < 0.5:
                return text_res5
        # sebagai tugas untuk melakukan proses seleksi hasil dari indeks rufier
        elif self.exp.age >= 13 and self.exp.age < 15: 
            # TO DO 
            if self.index >= 15:
                return text_res1
            elif self.index >= 11 and self.index < 15:
                return text_res2
            elif self.index >= 6 and self.index < 11:
                return text_res3
            elif self.index >= 0.5 and self.index < 6:
                return text_res4
            elif self.index < 0.5:
                return text_res5
        elif self.exp.age >= 15:
            if self.index >= 15:
                return text_res1
            elif self.index >= 11 and self.index < 15:
                return text_res2
            elif self.index >= 6 and self.index < 11:
                return text_res3
            elif self.index >= 0.5 and self.index < 6:
                return text_res4
            elif self.index < 0.5:
                return text_res5
        elif self.exp.age >= 15:
            if self.index >= 15:
                return text_res1
            elif self.index >= 11 and self.index < 15:
                return text_res2
            elif self.index >= 6 and self.index < 11:
                return text_res3
            elif self.index >= 0.5 and self.index < 6:
                return text_res4
            elif self.index < 0.5:
                return text_res5
        elif self.exp.age >= 15:
            if self.index >= 15:
                return text_res1
            elif self.index >= 11 and self.index < 15:
                return text_res2
            elif self.index >= 6 and self.index < 11:
                return text_res3
            elif self.index >= 0.5 and self.index < 6:
                return text_res4
            elif self.index < 0.5:
                return text_res5

# write a code for the second app
from PyQt5.QtCore import Qt, QTime, QTimer  # alignment
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, p1, p2, p3):
        self.age = int(age)
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        
class TestWin(QWidget):
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
        # init object widget
        # Qlabel
        self.label_name = QLabel(txt_name)
        self.label_umur = QLabel(txt_age)
        self.label_ins1 = QLabel(txt_test1)
        self.label_ins2 = QLabel(txt_test2)
        self.label_ins3 = QLabel(txt_test3)
        self.label_timer = QLabel(txt_timer)
        self.label_timer.setStyleSheet('font-family: Times; color: rgb(0,0,0); font-size: 36px; font-weight: bold')
        # Qlineedit
        self.edit_name = QLineEdit(txt_hintname)
        self.edit_age = QLineEdit(txt_hintage)
        self.edit_tes1 = QLineEdit(txt_hinttest1)
        self.edit_tes2 = QLineEdit(txt_hinttest2)
        self.edit_tes3 = QLineEdit(txt_hinttest3)
        # Qpushbutton
        self.button_test1 = QPushButton(txt_starttest1)
        self.button_test2 = QPushButton(txt_starttest2)
        self.button_test3 = QPushButton(txt_starttest3)
        self.button_next = QPushButton(txt_sendresults)

        # init main layout
        # layout kiri
        self.layout_kiri = QVBoxLayout()
        self.layout_kiri.addWidget(self.label_name, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.edit_name, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.label_umur, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.edit_age, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.label_ins1, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.button_test1, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.edit_tes1, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.label_ins2, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.button_test2, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.label_ins3, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.button_test3, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.edit_tes2, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.edit_tes3, alignment=Qt.AlignLeft)
        self.layout_kiri.addWidget(self.button_next, alignment=Qt.AlignCenter)        

        # layout utama
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.layout_kiri)
        self.layout.addWidget(self.label_timer)        

        # set main layout
        self.setLayout(self.layout)

    def connects(self):
        self.button_next.clicked.connect(self.next_click)
        self.button_test1.clicked.connect(self.timer_test)
        self.button_test2.clicked.connect(self.timer_sits)
        self.button_test3.clicked.connect(self.timer_final)

    def next_click(self):
        print('screen ketiga')
        self.hide()
        self.experiment = Experiment(self.edit_age.text(), self.edit_tes1.text(), self.edit_tes2.text(), self.edit_tes3.text())
        self.fw = FinalWin(self.experiment) # pindah layar ketiga

    def timer_test(self): # button test1
        self.time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    
    def timer1Event(self):
        self.label_timer.setText(self.time.toString("hh:mm:ss"))
        self.label_timer.setStyleSheet('font-family: Times; color: rgb(0,0,0); font-size: 36px; font-weight: bold')
        self.time = self.time.addSecs(-1)
        if self.time.toString("hh:mm:ss") == '00:00:00':
            self.timer.stop()
    
    def timer_sits(self): # button test2
        self.time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer2Event(self):
        self.label_timer.setText(self.time.toString("hh:mm:ss"))
        self.label_timer.setStyleSheet('font-family: Times; color: rgb(0,0,0); font-size: 36px; font-weight: bold')
        self.time = self.time.addSecs(-1)
        if self.time.toString("hh:mm:ss") == '00:00:00':
            self.timer.stop()
    
    def timer_final(self): # button test3
        self.time = QTime(0, 1, 00)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    
    def timer3Event(self):
        self.label_timer.setText(self.time.toString("hh:mm:ss"))
        
        if self.time.toString("hh:mm:ss") == '00:01:00':
            self.label_timer.setStyleSheet('font-family: Times; color: rgb(0,255,0); font-size: 36px; font-weight: bold')
        elif self.time.toString("hh:mm:ss") == '00:00:45':
            self.label_timer.setStyleSheet('font-family: Times; color: rgb(0,0,0); font-size: 36px; font-weight: bold')
        elif self.time.toString("hh:mm:ss") == '00:00:15':
            self.label_timer.setStyleSheet('font-family: Times; color: rgb(0,255,0); font-size: 36px; font-weight: bold')
        
        self.time = self.time.addSecs(-1)
        if self.time.toString("hh:mm:ss") == '00:00:00':
            self.timer.stop()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup

app = QApplication([])
window = QWidget()
window.resize(650, 400)
btn_OK = QPushButton("Ответить")
lb_q = QLabel("Сколько будет 1000-7")

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('69')
rbtn_2 = QRadioButton('-1007')
rbtn_3 = QRadioButton('-993')
rbtn_4 = QRadioButton('993')

ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rbtn_1)
ButtonGroup.addButton(rbtn_2)
ButtonGroup.addButton(rbtn_3)
ButtonGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

ResultGroupBox = QGroupBox("Результат ответов:")
layout_line2 = QVBoxLayout()
ResultGroupBox.setLayout(layout_line2)
tf = QLabel("Правильно/Неправильно")
res = QLabel("Ответ:")
layout_line2.addWidget(tf, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_line2.addWidget(res, alignment=(Qt.AlignCenter), stretch=2)
ResultGroupBox.setLayout(layout_line2)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_q, alignment=(Qt.AlignCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(ResultGroupBox)
ResultGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=3)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)

def ok():
    RadioGroupBox.hide()
    ResultGroupBox.show()
    btn_OK.setText("Следущий вопрос")

def show_question():
    RadioGroupBox.show()
    ResultGroupBox.hide()
    btn_OK.setText("Ответить")
    ButtonGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    ButtonGroup.setExclusive(True)
    lb_q.setText("Сколько будет 12*5-10+6")
    rbtn_1.setText("36")
    rbtn_2.setText("84")
    rbtn_3.setText("56")
    rbtn_4.setText("12")

def test():
    if 'Ответить' == btn_OK.text():
        ok()
    else:
        show_question()

btn_OK.clicked.connect(test)

window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()
app.exec_()

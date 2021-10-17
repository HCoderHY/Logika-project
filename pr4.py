from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel

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

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_q, alignment=(Qt.AlignCenter))
layout_line2.addWidget(RadioGroupBox)
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
	rbtn_1.hide()
	rbtn_2.hide()
	rbtn_3.hide()
	rbtn_4.hide()
	RadioGroupBox.hide()
	ResultGroupBox = QGroupBox("Результат ответов")
	layout_line2.addWidget(ResultGroupBox)

btn_OK.clicked.connect(ok)

window.setLayout(layout_card)
window.show()
app.exec_()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
import sys

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
res = QLabel()
layout_line2.addWidget(tf, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_line2.addWidget(res, alignment=(Qt.AlignCenter), stretch=2)
ResultGroupBox.setLayout(layout_line2)
StatisticsGroupBox = QGroupBox("Статистика опроса:")
layout_line4 = QVBoxLayout()
StatisticsGroupBox.setLayout(layout_line4)
tf2 = QLabel("Результат")
res2 = QLabel()
layout_line4.addWidget(tf2, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_line4.addWidget(res2, alignment=(Qt.AlignCenter), stretch=2)
StatisticsGroupBox.setLayout(layout_line4)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_q, alignment=(Qt.AlignCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(ResultGroupBox)
layout_line2.addWidget(StatisticsGroupBox)
ResultGroupBox.hide()
StatisticsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=3)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
ia = 0
grade = 0
def true_variant():
    global grade
    if lb_q.text() == "Сколько будет 1000-7":
        variant = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
        if variant[3].isChecked():
            tf.setText("Правильно")
            res.setText(variant[3].text())
            grade += 50
        else:
            tf.setText("Неправильно")
            res.setText(f"Правильный ответ: {variant[3].text()}")
    elif lb_q.text() == "Сколько будет 12*5-10+6":
        variant = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
        if variant[2].isChecked():
            tf.setText("Правильно")
            res.setText(variant[2].text())
            grade += 50
        else:
            tf.setText("Неправильно")
            res.setText(f"Правильный ответ: {variant[2].text()}")
    elif lb_q.text() == "В Америке говорят на ...":
        variant = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
        if variant[3].isChecked():
            tf.setText("Правильно")
            res.setText(variant[3].text())
            grade += 50
        else:
            tf.setText("Неправильно")
            res.setText(f"Правильный ответ: {variant[3].text()}")
    elif lb_q.text() == "Сколько будет 150+150+200":
        variant = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
        if variant[0].isChecked():
            tf.setText("Правильно")
            res.setText(variant[0].text())
            grade += 50
        else:
            tf.setText("Неправильно")
            res.setText(f"Правильный ответ: {variant[0].text()}")

def ok():
    true_variant()
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
    if lb_q.text() == "Сколько будет 1000-7":
        lb_q.setText("Сколько будет 12*5-10+6")
        rbtn_1.setText("36")
        rbtn_2.setText("84")
        rbtn_3.setText("56")
        rbtn_4.setText("12")
    elif lb_q.text() == "Сколько будет 12*5-10+6":
        lb_q.setText("В Америке говорят на ...")
        rbtn_1.setText("Армянском")
        rbtn_2.setText("Американском")
        rbtn_3.setText("Китайском")
        rbtn_4.setText("Англиском")
    elif lb_q.text() == "В Америке говорят на ...":
        lb_q.setText("Сколько будет 150+150+200")
        rbtn_1.setText("500")
        rbtn_2.setText("250")
        rbtn_3.setText("300")
        rbtn_4.setText("100")

def statistics():
    global grade
    RadioGroupBox.hide()
    ResultGroupBox.hide()
    StatisticsGroupBox.show()
    lb_q.setText("-Опрос Окончен-")
    btn_OK.setText("Закрыть Программу")
    res2.setText(f"Ваш бал {str(grade)}/200")


def test():
    global ia
    if 'Ответить' == btn_OK.text():
        ok()
    else:
        show_question()

    if ia == 7:
        statistics() 
    elif ia == 6:
        btn_OK.setText("Стастистика")
    elif ia == 8:
        exit()
    ia += 1

btn_OK.clicked.connect(test)

window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()
app.exec_()

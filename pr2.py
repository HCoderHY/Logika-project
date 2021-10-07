import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
def gener():
    win_num = random.randint(0,99)
    winner.setText(str(win_num))
    text.setText("Подебитель:")
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Определить победителя")
button = QPushButton("Сгенерировать")
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel("?")
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)
main_win.resize(400, 150)
button.clicked.connect(gener)
main_win.show()
app.exec_()

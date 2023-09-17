import string
import random 
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
        QApplication, QWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox,
        QPushButton, QLabel, QListView, QFormLayout)

app = QApplication([])

# СТВОРЕННЯ ГОЛОВНОГО ВІКНА
window = QWidget()
width = 600
height = 500
window.resize(width, height)
window.move(300, 300)
window.setWindowTitle('NIGA')


button = QPushButton('Згенерувати пароль')
label1 = QLabel('Пароль')
label2 = QLabel('')

def cl():
    label2.setText(str(list[a]))
#Розташування по лайаути


v1 = QVBoxLayout()
v1.addWidget(label1)
v1.addWidget(label2)
v1.addWidget(button)

window.setLayout(v1)

def a():
    n = 'qwertyuiop[]asdfghjkl;\zxcvnm,./1234567890-='
    v = 16
    password = ''
    for a in n:
        password += random.choice(n)
    label2.setText(password)

button.clicked.connect(a)    


window.show()
app.exec_()
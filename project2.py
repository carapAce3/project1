from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
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







#Створення віджетів
button1 = QPushButton('Нове питання')
button2 = QPushButton('Видалити питання')
button3 = QPushButton('Почати тренування')

text = QListView()


line1 = QLineEdit('')
line2 = QLineEdit('')
line3 = QLineEdit('')
line4 = QLineEdit('')
line5 = QLineEdit('')

form = QFormLayout()
form.addRow('Питання: ', line1)
form.addRow('Правильна вдповідь: ', line2)
form.addRow('Неправильна відповідь №1: ', line3)
form.addRow('Неправильна відповідь №2: ', line4)
form.addRow('Неправильна відповідь №3: ', line5)



h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
v1 = QVBoxLayout()

h1.addWidget(text)
h1.addLayout(form)
h2.addWidget(button1)
h2.addWidget(button2)
h3.addWidget(button3)

v1.addLayout(h1)
v1.addLayout(h2)
v1.addLayout(h3)
window.setLayout(v1)







window.show()
app.exec_()
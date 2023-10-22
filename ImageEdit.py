from PIL import Image, ImageFilter
import json
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QListWidget,
        QPushButton, QLabel, QWidget,
        QHBoxLayout, QVBoxLayout,)



app = QApplication([])
app.setStyle('Fusion')

window = QWidget()
width = 900
height = 600
window.resize(width, height)
window.move(250, 50)
window.setWindowTitle('NIGA')



with Image.open('ElGatooo.jpg') as o:
    print('Розмір: ', o.size)
    print('Формат: ', o.format)
    print('Тип: ', o.mode)
    o.show()
    photo2 = o.convert('L')
    photo2.show()
    photo3 = o.filter(ImageFilter.BLUR)
    photo3.show()
    photo4 = o.transpose(Image.ROTATE_180)
    photo4.show()
    photo4.save('gray.jpg')

Folder = QPushButton("Папка")
Left = QPushButton("Вліво")
Right = QPushButton("Вправо")
Mirror = QPushButton("Дзеркало")
Sharpness = QPushButton("Різкість")
Black_n_White = QPushButton("Ч/Б")

Picture = QLabel('Картинка')

H1 = QHBoxLayout()
V1 = QVBoxLayout()
H2 = QHBoxLayout()
V2 = QVBoxLayout()

H1.addWidget()
H1.addWidget()
V1.addWidget()
V1.addWidget()
V1.addWidget()
V1.addWidget()
H2.addLayout(V1)
V2.addLayout()
V2.addLayout()

window.show()
app.exec_()
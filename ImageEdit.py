import os
from PIL import Image, ImageFilter
import json
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QListWidget,
        QPushButton, QLabel, QWidget,
        QHBoxLayout, QVBoxLayout,
        QFileDialog)



app = QApplication([])
app.setStyle('Fusion')

window = QWidget()
width = 900
height = 600
window.resize(width, height)
window.move(250, 50)
window.setWindowTitle('NIGA')



#with Image.open('ElGatooo.jpg') as o:
    #print('Розмір: ', o.size)
    #print('Формат: ', o.format)
    #print('Тип: ', o.mode)
    #o.show()
    #photo2 = o.convert('L')
    #photo2.show()
    #photo3 = o.filter(ImageFilter.BLUR)
    #photo3.show()
    #photo4 = o.transpose(Image.ROTATE_180)
    #photo4.show()
    #photo4.save('gray.jpg')

Folder = QPushButton("Папка")
Left = QPushButton("Вліво")
Right = QPushButton("Вправо")
Mirror = QPushButton("Дзеркало")
Sharpness = QPushButton("Різкість")
B_n_W = QPushButton("Ч/Б")

Picture = QLabel('Картинка')

list1 = QListWidget()

H1 = QHBoxLayout()
V1 = QVBoxLayout()
H2 = QHBoxLayout()
V2 = QVBoxLayout()

V1.addWidget(Folder)
V1.addWidget(list1)
V2.addWidget(Picture)
V2.addLayout(H1)


H1.addWidget(Left)
H1.addWidget(Right)
H1.addWidget(Mirror)
H1.addWidget(Sharpness)
H1.addWidget(B_n_W)
H2.addLayout(V1)
H2.addLayout(V2)

Folder.setStyleSheet("background-color : red ")
Left.setStyleSheet("background-color : blue ")
Right.setStyleSheet("background-color : blue ")
Sharpness.setStyleSheet("background-color : blue ")
Mirror.setStyleSheet("background-color : blue ")
B_n_W.setStyleSheet("background-color : blue ")


def choise_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory() # Получаємо шлях з обраної папки

def filter(files, extensions):
    result = []
    for f in files:
        for e in extensions:
            if f.endswith(e):
                result.append(f)
    return result


def show_files():
    extensions = ['jpeg', 'png', 'svg', 'jpg']
    choise_workdir()
    filenames = filter(os.listdir(workdir), extensions) # Витягуємо файли з вказаного шляху
    list1.clear()
    for f in filenames:
        list1.addItem(f)
Folder.clicked.connect(show_files)



window.setLayout(H2)
window.show()
app.exec_()
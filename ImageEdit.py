import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap # оптимізована для показу на екрані картинка
 
from PIL import Image


from PIL import ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   GaussianBlur, UnsharpMask)


app = QApplication([])
app.setStyle('Fusion')

window = QWidget()
width = 1000
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
Contour = QPushButton("Контур")
MinFilter = QPushButton("Фільтер")


Picture = QLabel('Картинка')

list1 = QListWidget()

H1 = QHBoxLayout()
V1 = QVBoxLayout()
H2 = QHBoxLayout()
V2 = QVBoxLayout()
H1.addWidget(Left)
H1.addWidget(Right)
H1.addWidget(Mirror)
H1.addWidget(Sharpness)
H1.addWidget(B_n_W)
H1.addWidget(Contour)
H1.addWidget(MinFilter)

V1.addWidget(Folder)
V1.addWidget(list1)

V2.addWidget(Picture)
V2.addLayout(H1)

H2.addLayout(V1,stretch=1)
H2.addLayout(V2,stretch=5)

Folder.setStyleSheet("background-color : red ")
Left.setStyleSheet("background-color : purple ")
Right.setStyleSheet("background-color : blue ")
Sharpness.setStyleSheet("background-color : blue ")
Contour.setStyleSheet("background-color : blue ")
Mirror.setStyleSheet("background-color : purple ")
MinFilter.setStyleSheet("background-color : purple ")
B_n_W.setStyleSheet("background-color : purple ")
list1.setStyleSheet("background-color : grey ")


def choise_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory() #Отримаємо шлях з обраної папки

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

class ImageProcessor():
   def __init__(self):
       self.image = None
       self.dir = None
       self.filename = None
       self.save_dir = "Modified/"
 
   def loadImage(self, filename):
       ''' під час завантаження запам'ятовуємо шлях та ім'я файлу '''
       self.filename = filename
       fullname = os.path.join(workdir, filename)
       self.image = Image.open(fullname)
 
   def saveImage(self):
       ''' зберігає копію файлу у підпапці '''
       path = os.path.join(workdir, self.save_dir)
       if not(os.path.exists(path) or os.path.isdir(path)):
           os.mkdir(path)
       fullname = os.path.join(path, self.filename)
 
       self.image.save(fullname)
    ###############
   def do_bw(self):
       self.image = self.image.convert("L")
       self.saveImage()
       image_path = os.path.join(workdir, self.save_dir, self.filename)
       self.showImage(image_path)

    
   def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)


   def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

   def do_blure(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

   def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

   def do_contour(self):
        self.image = self.image.filter (ImageFilter.CONTOUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)


   def do_MinFilter(self):
        self.image = self.image.filter(ImageFilter.MinFilter(3))
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)   


    ##################################
   def showImage(self, path):
       Picture.hide()
       pixmapimage = QPixmap(path)
       w, h = Picture.width(), Picture.height()
       pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
       Picture.setPixmap(pixmapimage)
       Picture.show()
 
def showChosenImage():
   if list1.currentRow() >= 0:
       filename = list1.currentItem().text()
       workimage.loadImage(filename)
       workimage.showImage(os.path.join(workdir, workimage.filename))
 
workimage = ImageProcessor() #поточне робоче зображення для роботи
list1.currentRowChanged.connect(showChosenImage)
 
B_n_W.clicked.connect(workimage.do_bw)
Right.clicked.connect(workimage.do_right)
Left.clicked.connect(workimage.do_left)
Sharpness.clicked.connect(workimage.do_blure)
Mirror.clicked.connect(workimage.do_mirror)
Contour.clicked.connect(workimage.do_contour)
MinFilter.clicked.connect(workimage.do_MinFilter)

window.setLayout(H2)
window.show()
app.exec_()
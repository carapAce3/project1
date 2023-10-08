import json
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QListWidget,
        QPushButton, QLabel, QLineEdit,
        QTextEdit, QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QInputDialog)

app = QApplication([])
app.setStyle('Fusion')

window = QWidget()
width = 900
height = 600
window.resize(width, height)
window.move(250, 50)
window.setWindowTitle('NIGA')



btn_add = QPushButton('Створити замітку')
btn_del = QPushButton('Видалити замітку')
btn_save = QPushButton('Зберегти замітку')
btn_add_to = QPushButton('Додати до замітки')
btn_open = QPushButton('Відкрити від замітки')
btn_search = QPushButton('Шукати замітки по тегу')

list_notes = QLabel('Список заміток')
list_tag = QLabel('Список тегів')

edit_text = QTextEdit()
edit_line = QLineEdit()
edit_line.setPlaceholderText('Введіть тег...')

list_notes_widget = QListWidget()
list_tag_widget = QListWidget()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()

layoutV1.addWidget(edit_text)
layoutH1.addWidget(btn_add)
layoutH1.addWidget(btn_del)
layoutH2.addWidget(btn_add_to)
layoutH2.addWidget(btn_open)
layoutV2.addWidget(list_notes)
layoutV2.addWidget(list_notes_widget)
layoutV2.addLayout(layoutH1)
layoutV2.addWidget(btn_save)
layoutV2.addWidget(list_tag)
layoutV2.addWidget(list_tag_widget)
layoutV2.addWidget(edit_line)
layoutV2.addLayout(layoutH2)
layoutV2.addWidget(btn_search)
layoutH3.addLayout(layoutV1)
layoutH3.addLayout(layoutV2)
window.setLayout(layoutH3)

def show_notes():
    key = list_notes_widget.selectedItems()[0].text()
    edit_text.setText(notes[key]['текст'])

def add_notes():
    dialog, ok = QInputDialog.getText(window, 'Додати замітку', "Назва замітки") 
    if dialog and ok != '':
        notes[dialog] = {'текст':"", "теги":[]}
        list_notes_widget.addItem(dialog)


def save_notes():
    if list_notes_widget.selectedItems():
        key = list_notes_widget.selectedItems()[0].text()
        notes[key]['текст'] = edit_text.toPlainText()
        with open('f.json', 'w') as file:
            json.dump(notes, file)


def del_notes():
    if list_notes_widget.selectedItems():
        key = list_notes_widget.selectedItems()[0].text()
        del notes[key]
        edit_text.clear()
        list_notes_widget.clear()
        list_notes_widget.addItems(notes)
        with open('f.json', 'w') as file:
            json.dump(notes, file)




list_notes_widget.itemClicked.connect(show_notes)
btn_add.clicked.connect(add_notes)
btn_save.clicked.connect(save_notes)
btn_del.clicked.connect(del_notes)


list_notes_widget.itemClicked.connect(show_notes)
with open('f.json', 'r') as file:
    notes = json.load(file)
list_notes_widget.addItems(notes)


list_notes.setStyleSheet("background-color: blue")
btn_add.setStyleSheet("background-color : pink ")
btn_save.setStyleSheet("background-color: pink;")
btn_del.setStyleSheet("background-color: pink;")
btn_add_to.setStyleSheet("background-color: red;")
btn_open.setStyleSheet("background-color: red;")
btn_search.setStyleSheet("background-color: red;")
list_notes_widget.setStyleSheet("background-color: Aliceblue;")
list_tag_widget.setStyleSheet("background-color: Aliceblue;")
list_tag.setStyleSheet("background-color: blue;")

window.show()
app.exec_()

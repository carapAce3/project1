from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QListWidget,
        QPushButton, QLabel, QLineEdit,
        QTextEdit, QApplication, QWidget,
        QHBoxLayout, QVBoxLayout)

app = QApplication([])


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
edit_line = QLineEdit('Введіть тег...')

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

window.show()
app.exec_()
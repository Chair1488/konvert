from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
import requests, json

def result_konvert():
    p = requests.get(f"https://v6.exchangerate-api.com/v6/key/pair/{a_box.text()}/{b_box.text()}/{c_box.text()}").json()
    result.setText("Результат: " + str(p["conversion_result"]))

app = QApplication([])
mw = QWidget()

mw.setWindowTitle("Валюта")
mw.resize(300, 500)
mw.move(250, 250)
line = QVBoxLayout()

a_lable = QLabel("Из какой валюты конвертировать")
a_box = QLineEdit()
b_lable = QLabel("В какой валюты конвертировать")
b_box = QLineEdit()
c_lable = QLabel("Сумма")
c_box = QLineEdit()
button = QPushButton("Конвертировать")
result = QLabel("Результат:")

line.addWidget(a_lable, alignment=Qt.AlignCenter)
line.addWidget(a_box, alignment=Qt.AlignCenter)
line.addWidget(b_lable, alignment=Qt.AlignCenter)
line.addWidget(b_box, alignment=Qt.AlignCenter)
line.addWidget(c_lable, alignment=Qt.AlignCenter)
line.addWidget(c_box, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
line.addWidget(result, alignment=Qt.AlignCenter)
mw.setLayout(line)

button.clicked.connect(result_konvert)

mw.show()
app.exec_()

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout,QWidget,QLineEdit
from datetime import datetime
from dateutil.relativedelta import relativedelta

def on_click():
    data=input_field.text()
    birth_date = datetime.strptime(data, f"%d.%m.%Y")
    current_date = datetime.now()
    if birth_date>birth_date:
        label.setText("Invalid date") 
    difference = relativedelta(current_date, birth_date)
    years = difference.years
    months = difference.months
    days = difference.days
    if years==0 and months==0 and days==0:
        label.setText("yeni dogulub")
    else:
        label.setText(f"Age: {years} years, {months} months, {days} days")


app=QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Numane progran")
window.resize(400,300)

label=QLabel()

input_field=QLineEdit()
button=QPushButton("Click me")

layout=QVBoxLayout()


layout.addWidget(input_field,alignment=Qt.AlignCenter)
layout.addWidget(label,alignment=Qt.AlignCenter)
layout.addWidget(button,alignment=Qt.AlignCenter)

# central_widget=QWidget()
# central_widget.setLayout(layout)
# window.setLayout(layout)

window.setLayout(layout)

button.clicked.connect(on_click)

window.show()

app.exec()


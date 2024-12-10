import sys
from PySide6.QtWidgets import QApplication ,QMainWindow , QLabel , QPushButton , QSpinBox ,QVBoxLayout , QWidget
from PySide6.QtCore import Qt;


class MyClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinbox Example")
        self.resize(600,400)
        central_widget=QWidget()
        layout=QVBoxLayout()
        self.spinbox=QSpinBox(self)
        self.spinbox.setRange(1,12)
        self.spinbox.setValue(1)
        self.spinbox.setSuffix("mounth")
        self.welcome_label=QLabel("Please select mounth")
        self.button=QPushButton("Click me")
        self.button.clicked.connect(self.on_clicked)
        self.result_label=QLabel(self)

        layout.addWidget(self.welcome_label,alignment=Qt.AlignCenter)
        layout.addWidget(self.spinbox,alignment=Qt.AlignCenter)
        layout.addWidget(self.button,alignment=Qt.AlignCenter)
        layout.addWidget(self.result_label,alignment=Qt.AlignCenter)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_clicked(self):
        value= self.spinbox.value()
        current_mounth=11
        if current_mounth>value:
            self.result_label.setText(f"Your selection is{value},your selection is next mounth")
        elif current_mounth>value:
            self.result_label.setText(f"Your selection is{value},your selection is next mounth")
        else:
            self.result_label.setText(f"Your selection is{value},your selection is current mounth")
    
def main():
    app=QApplication()
    window=MyClass()

    window.show()
    app.exec()

if __name__ =="__main__":
    main()







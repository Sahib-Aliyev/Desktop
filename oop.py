import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout,QWidget,QLineEdit

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Enter usename and password")
        self.username_field=QLineEdit(self)
        self.username_field.setPlaceholderText('Username')
        self.password_field=QLineEdit(self)
        self.password_field.setPlaceholderText('Password')
        self.password_field.setEchoMode(QLineEdit.Password)
        
        self.password_field.textChanged.connect(self.on_password_change)

        self.button= QPushButton("Login")
        self.button.setEnabled(False)
        self.button.clicked.connect(self.on_click)
    

        layout=QVBoxLayout()
        layout.addWidget(self.button,alignment=Qt.AlignCenter)
        layout.addWidget(self.label,alignment=Qt.AlignCenter)
        layout.addWidget(self.username_field,alignment=Qt.AlignCenter)
        layout.addWidget(self.password_field,alignment=Qt.AlignCenter)

        layout.addStretch(10)

        self.setLayout(layout)
        self.resize(600,400)
        self.setWindowTitle("OOP example program")

    def on_click(self):
        username=self.username_field.text()
        password=self.password_field.text()
        self.label.setText(f"Username:{username} , Password:{password}")
    def on_password_change(self):
        password=self.password_field.text()
        if len(password)<3:
            self.button.setEnabled(False)
            self.label.setText("Password is short")
        else:
            self.button.setEnabled(True)
            self.label.setText("Password is good enough")
def main():
    app=QApplication(sys.argv)
    window=MyWindow()
    window.show()
    sys.exit(app.exec())

main()

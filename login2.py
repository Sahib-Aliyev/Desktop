from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QStackedWidget, QPushButton, QLineEdit, QLabel, 
    QCheckBox, QMessageBox
)
from PySide6.QtCore import Qt
import sys
import json

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.stacked_widget = QStackedWidget()

        self.login_widget = QWidget()
        login_layout = QVBoxLayout()

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.textChanged.connect(self.on_password_change)

        self.is_admin = QCheckBox("Login as Admin")
        self.button = QPushButton("Login")
        self.button.clicked.connect(self.on_click)
        self.button.setEnabled(False)

        login_layout.addWidget(self.username)
        login_layout.addWidget(self.password)
        login_layout.addWidget(self.is_admin)
        login_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        login_layout.addStretch(10)
        self.login_widget.setLayout(login_layout)

        self.result_widget = QWidget()
        self.label = QLabel()
        result_layout = QVBoxLayout()
        result_layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.result_widget.setLayout(result_layout)

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.result_widget)
        self.setCentralWidget(self.stacked_widget)

    def on_click(self):
        username = self.username.text()
        password = self.password.text()
        is_admin = self.is_admin.isChecked()

        try:
            with open("db.json", mode="r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Database file not found.")
            return

        for user in data:
            if user['username'] == username and user["password"] == password:
                if (is_admin and user["is_admin"] == "True") or (not is_admin and user["is_admin"] == "False"):
                    if is_admin:
                        self.label.setText(f"Welcome, {user['username']}. You logged in as admin.")
                    else:
                        self.label.setText(f"Welcome, {user['username']}. You logged in as user.")
                    self.stacked_widget.setCurrentWidget(self.result_widget)
                    return
                else:
                    QMessageBox.critical(self, "Login Failed", "Invalid role.")
                    return

        QMessageBox.critical(self, "Login Failed", "Invalid username or password.")

    def on_password_change(self):
        password = self.password.text()
        if len(password) < 5:
            self.button.setEnabled(False)
            self.label.setText("Password is too short.")
        else:
            self.button.setEnabled(True)
            self.label.setText("Password is strong enough.")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

main()

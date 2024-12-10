import sys
from PySide6.QtWidgets import QApplication ,QMainWindow , QLabel , QPushButton , QProgressBar ,QVBoxLayout , QWidget
from PySide6.QtCore import Qt , QTimer


class MyClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressbarExample")
        self.resize(600,400)
        central_widget=QWidget()
        layout=QVBoxLayout()
        self.progress_bar= QProgressBar(self)
        self.progress_bar.setRange(0,100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.button = QPushButton("Start task",self)
        self.button.clicked.connect(self.start_task)

        self.label=QLabel()

        layout=QVBoxLayout()

        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        layout.addStretch(10)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_percentage)
        self.progress_value =0

    def start_task(self):
        self.button.setEnabled(False)
        self.timer.start(500)
    
    def update_percentage(self):
        self.progress_value+=20
        self.progress_bar.setValue(self.progress_value)
        if self.progress_value>=100:
            self.timer.stop()
            self.setEnabled(True)
            self.label.setText("Downloading is complated")
def main():
    app=QApplication()
    window=MyClass()

    window.show()
    app.exec()

if __name__ =="__main__":
    main()








import sys
from PySide6.QtWidgets import QApplication ,QMainWindow , QLabel , QPushButton , QTableWidget ,QVBoxLayout , QWidget ,QTableWidgetItem
from PySide6.QtCore import Qt , QTimer

class MyClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget Example")
        self.resize(600,400)
        central_widget=QWidget()
        layout=QVBoxLayout()

        self.table_widget=QTableWidget()
        self.table_widget.setRowCount(2)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['name','surname'])
        self.table_widget.setVerticalHeaderLabels(['1','2'])
        self.table_widget.setEditTriggers(QTableWidget.AllEditTriggers)
        self.button =QPushButton("Submit")
        self.button.clicked.connect(self.show_submit_data)

        self.label = QLabel()

        layout=QVBoxLayout()

        layout.addWidget(self.table_widget)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_submit_data(self):
        values=[]
        number_of_rows = self.table_widget.rowCount()
        number_of_colums =self.table_widget.columnCount()
        for row in range(number_of_rows):
            full_row_text=[]
            for column in range (number_of_colums):
                item=self.table_widget.item(row,column)
                if item:
                    item_text=item.text()
                    full_row_text.append(item_text.capitalize())
            values.append(" ".join (full_row_text))
            self.label.setText("\n".join(values))
def main():
    app=QApplication()
    window=MyClass()

    window.show()
    app.exec()

if __name__ =="__main__":
    main()









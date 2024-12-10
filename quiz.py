from PySide6.QtWidgets import *
from PySide6.QtCore import Qt ,QTimer
import sys


class MyClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressbarExample")
        self.resize(600,400)
        central_widget=QWidget()
        layout=QVBoxLayout()
        self.progress_bar= QProgressBar(self)
        self.progress_bar.setRange(0,60)
        self.progress_bar.setValue(60)
        self.progress_bar.setTextVisible(True)
        self.button = QPushButton("Submit",self)
        self.button.clicked.connect(self.on_click)

        self.question_1 = QLineEdit(self)
        self.question_1.setPlaceholderText("I ci sualın cavabını daxil edin")

        self.combo_1= QComboBox()
        self.combo_1.addItem("Python")
        self.combo_1.addItem("Java")
        self.combo_1.addItem("PHP")
        self.combo_2= QComboBox()
        self.combo_2.addItem("qoyun")
        self.combo_2.addItem("toyuq")
        self.combo_2.addItem("ilan")

        self.question_checkbox_1_1= QCheckBox("Nil")
        self.question_checkbox_1_2= QCheckBox("Volqa")
        self.question_checkbox_1_3= QCheckBox("Baykal")
        self.question_checkbox_2_1=QCheckBox("Ispaniya ")
        self.question_checkbox_2_2=QCheckBox("Argentina ")
        self.question_checkbox_2_3=QCheckBox("Cin ")



        self.label=QLabel("Imtahan basladi.Ugurlar")
        self.label_1=QLabel("2 ci dunya muharibesi ne vaxt bas verib?")
        self.label_2=QLabel("En yaxsi proqramlasdirma dili hansidi?")
        self.label_3=QLabel("Hansi heyvan 4 ayaqlidir?")
        self.label_4=QLabel("Hansi caydir?")
        self.label_5=QLabel("Hansi olke avropada yerlesir?")
        self.label_result=QLabel("")

        

        
        layout=QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label_1)
        layout.addWidget(self.question_1)
        layout.addWidget(self.label_2)
        layout.addWidget(self.combo_1)
        layout.addWidget(self.label_3)
        layout.addWidget(self.combo_2)
        layout.addWidget(self.label_4)
        layout.addWidget(self.question_checkbox_1_1)
        layout.addWidget(self.question_checkbox_1_2)
        layout.addWidget(self.question_checkbox_1_3)
        layout.addWidget(self.label_5)
        layout.addWidget(self.question_checkbox_2_1)
        layout.addWidget(self.question_checkbox_2_2)
        layout.addWidget(self.question_checkbox_2_3)
        self.progress_value = 60


        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button)
        layout.addWidget(self.label_result)
        layout.addStretch(10)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)


    def start_task(self):
        self.button.setEnabled(True)
    


    def on_click(self):
        self.timer.stop()
        self.checking_results()
        self.button.setEnabled(False)
        
    def update_progress(self):
        self.progress_value -= 1
        self.progress_bar.setValue(self.progress_value)
        self.progress_bar.setFormat(f"{self.progress_value} saniye")
        if self.progress_value <=0:
            self.timer.stop()
            self.button.setEnabled(False)
            self.label.setText("Imtahan bitdi")
            self.checking_results()

    
    def checking_results(self):
        ans=[]
        answer_1=self.question_1.text()
        answer_2=self.combo_1.currentText()
        answer_3=self.combo_2.currentText()
        if answer_1=="1939":
            ans.append(1)
        else:
            ans.append(0)
        if answer_2 == "Python":
            ans.append(1)
        else:
            ans.append(0)
        if answer_3 == "qoyun":
            ans.append(1)
        else:
            ans.append(0)
        if self.question_checkbox_1_1.isChecked() and self.question_checkbox_1_2.isChecked():
            ans.append(1)
        else:
            ans.append(0)
        if self.question_checkbox_2_1.isChecked() :
            ans.append(1)
        else:
            ans.append(0)
        if ans.count(1)==0:
            self.label_result.setText("Duzgun cavab vermemisiz")
        elif ans.count(1)>3:
            self.label_result.setText(f"Siz {ans.count(1)} suala duzgun cavab verdiz.Uddunuz")
        elif ans.count(1)<=3:
            self.label_result.setText(f"Siz {ans.count(1)} suala duzgun cavab verdiz.Uduzdunuz")

def main():
    app=QApplication()
    window=MyClass()

    window.show()
    app.exec()

if __name__ =="__main__":
    main()








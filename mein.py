from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QApplication
from password import Ui_MainWinow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWinow()
        self.ui.setpUi(self)

app = QApplication([])
window = Widget()
def generation():
    digital = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter =['g', 'l', 'm']




btn.OK.clicked.connect(generation)
window.show()
app.exec_()

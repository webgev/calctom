import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

import helper
import calc

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Розничный калькулятор Тома'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 340
        self.initUI()
    
    def initUI(self):
        """ Инициализация интерфейса """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        self.initUICount()
        self.initUIPrice()
        self.initUIState()
        self.initUITotal()
        
        self.button = QtWidgets.QPushButton('Рассчитать', self)
        self.button.move(220, 60)
        
        self.button.clicked.connect(self.on_click)
        self.show()
    
    def initUICount(self):
        label = QtWidgets.QLabel(self)
        label.move(20, 20)
        label.setText("Количество:")
        
        self.textbox_count = QtWidgets.QLineEdit(self)
        self.textbox_count.move(100, 20)
        self.textbox_count.resize(100,30)
       
       
    def initUIPrice(self):
        label = QtWidgets.QLabel(self)
        label.move(20, 60)
        label.setText("Цена:")
        
        self.textbox_price = QtWidgets.QLineEdit(self)
        self.textbox_price.move(100, 60)
        self.textbox_price.resize(100,30)
        
    def initUIState(self):
        label = QtWidgets.QLabel(self)
        label.move(20, 100)
        label.setText("Штат:")
        
        self.combobox_state = QtWidgets.QComboBox(self)
        self.combobox_state.addItem("")
        for value in helper.STATE.keys():
            self.combobox_state.addItem(value.upper())
        self.combobox_state.move(100, 100)
    
    def initUITotal(self):
        newfont = QtGui.QFont("", 8, QtGui.QFont.Bold) 
        self.label_total = QtWidgets.QLabel(self)
        self.label_total.move(20, 160)
        self.label_total.resize(300, 20)
        self.label_total.setFont(newfont)
        
        self.label_dicount_total = QtWidgets.QLabel(self)
        self.label_dicount_total.move(20, 190)
        self.label_dicount_total.resize(300, 20)
        self.label_dicount_total.setFont(newfont)
    
    def on_click(self):
        count = self.textbox_count.text() 
        price = self.textbox_price.text() 
        state = self.combobox_state.currentText() 
        try:
            total, dicount_total = calc.calc(count, price, state)
            self.label_total.setText( "С налогом: " + str(total))
            self.label_dicount_total.setText("Без налога, со скидкой: " + str(dicount_total))
        except Exception as ex:
            QtWidgets.QMessageBox.question(self, 'Ошибка', str(ex), QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
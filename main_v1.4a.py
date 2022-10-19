import sys
import pandas, csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QVBoxLayout

col_list = ["meat"]
csv_file = pandas.read_csv('sheets/legacy_sheets/meats.csv', usecols=col_list)
print(csv_file)
# print(type(csv_file))

x = 0 
the_list = []
for i in range (0,3):
    the_list.append(csv_file.iloc[x, 0])
    x+= 1
y = len(the_list)

class Window(QMainWindow): 
     
    def __init__(self):
        super().__init__()

        first_check = 0

        # Select Ingredients Label
        self.wlabel = QLabel(self)
        self.wlabel.move(20, 44)
        self.wlabel.resize(120, 30)
        self.wlabel.setText("Select Ingredient: ")

        # Select Ingredients Label
        self.ylabel = QLabel(self)
        self.ylabel.move(20, 104)
        self.ylabel.resize(120, 30)
        self.ylabel.setText("Select Ingredient: ")

        # Ingredient Display
        self.qlabel = QLabel(self)
        self.qlabel.move(270,50)

        # Ingredient Display
        self.zlabel = QLabel(self)
        self.zlabel.move(270,110)
        

        z = 0
        self.combo = QComboBox(self)
        self.combo.addItem('')

        self.mumbo = QComboBox(self)
        self.mumbo.addItem('')
        for i in range (0,y):
            self.combo.addItem(the_list[z])
            self.mumbo.addItem(the_list[z])
            z += 1

        self.combo.move(150, 44)       
        self.combo.activated[str].connect(self.onChanged)
        # self.combo.currentTextChanged.connect(self.remove_list)

        self.mumbo.move(150, 104)       
        self.mumbo.activated[str].connect(self.onChanged_2)
        # self.mumbo.currentTextChanged.connect(self.remove_list_2)

          
        # Non-Necessary edits
        # Window Size
        self.setGeometry(50,50,400,200)
        # Window Title
        self.setWindowTitle("Sandwich Wizard")
        # Make it appear on the window
        self.show()
        
        

    # for when the drop boxes are interacted with  
    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        

    def onChanged_2(self, text):
        self.zlabel.setText(text)
        self.zlabel.adjustSize()

    # to stop duplicate ingredients
    def remove_list(self, text):
        global index
        index = self.mumbo.findText(text)
        self.mumbo.removeItem(index)

    def remove_list_2(self, text):
        global index_2
        index_2 = self.combo.findText(text)
        self.combo.removeItem(index_2)

    # to re-add the removed items
    def append_list(self):
        pass

    def append_list_2(self):
        self.combo.addItem("venison")
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
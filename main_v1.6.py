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


bread_csv = pandas.read_csv('sheets/legacy_sheets/breads.csv')
print(bread_csv)

x = 0 
bread_list = []
for i in range (0,3):
    bread_list.append(bread_csv.iloc[x, 0])
    x+= 1
y_2 = len(bread_list)

'''
y = 0
z = 1 
white = []
for i in range (0,4):
    white.append(bread_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
sourdough = []
for i in range (0,4):
    sourdough.append(bread_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
wheatmeal = []
for i in range (0,4):
    wheatmeal.append(bread_csv.iloc[y, z])
    z+= 1
'''
y = len(the_list)

class Window(QMainWindow): 
     
    def __init__(self):
        super().__init__()
        # Select Ingredients Label
        self.wlabel = QLabel(self)
        self.wlabel.move(20, 104)
        self.wlabel.resize(120, 30)
        self.wlabel.setText("Select Ingredient: ")

        # Select Ingredients Label
        self.bread_select = QLabel(self)
        self.bread_select.move(20, 44)
        self.bread_select.resize(120, 30)
        self.bread_select.setText("Select Ingredient: ")

        # Ingredient Display
        self.qlabel = QLabel(self)
        self.qlabel.move(270,110)

        # Ingredient Display
        self.bread_label = QLabel(self)
        self.bread_label.move(270,50)
        

        z = 0
        self.combo = QComboBox(self)
        self.combo.addItem('')
        
        for i in range (0,y):
            self.combo.addItem(the_list[z])
            z += 1

        z = 0
        self.breado = QComboBox(self)
        self.breado.addItem('')

        for i in range (0,y_2):
            self.breado.addItem(bread_list[z])
            z += 1

        self.combo.move(150, 104)       
        self.combo.activated[str].connect(self.onChanged)

        self.breado.move(150, 44)       
        self.breado.activated[str].connect(self.onChanged_bread)
        
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

    def onChanged_bread(self, text):
        self.bread_label.setText(text)
        self.bread_label.adjustSize()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

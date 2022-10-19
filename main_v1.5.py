import sys
import pandas, csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QVBoxLayout

col_list = ["bread"]
csv_file = pandas.read_csv('sheets/breads.csv', usecols=col_list)
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
        self.wlabel.move(50, 44)
        self.wlabel.resize(120, 30)
        self.wlabel.setText("Select Bread Type: ")

        # Ingredient Display
        self.qlabel = QLabel(self)
        self.qlabel.move(270,50)

        # Combo Box
        z = 0
        self.combo = QComboBox(self)
        self.combo.addItem('')

        # add the ingredients to the combo box
        for i in range (0,y):
            self.combo.addItem(the_list[z])
            z += 1

        self.combo.move(150, 44)
        self.combo.activated[str].connect(self.onChanged)
          
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
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

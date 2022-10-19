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
wholegrain = []
for i in range (0,4):
    wholegrain.append(bread_csv.iloc[y, z])
    z+= 1

y = len(the_list)

class Window(QMainWindow): 
     
    def __init__(self):
        super().__init__()

        # Select Ingredients Label
        self.bread_select = QLabel(self)
        self.bread_select.move(20, 44)
        self.bread_select.resize(120, 30)
        self.bread_select.setText("Select Bread Type: ")

        # Ingredient Display
        self.bread_label = QLabel(self)
        self.bread_label.move(270,50)

        # Calories Label
        self.calories_label = QLabel(self)
        self.calories_label.move(20, 101)
        self.calories_label.resize(120, 30)
        self.calories_label.setText("Calories: ")

        # Calories Display
        self.calories_counter = QLabel(self)
        self.calories_counter.move(90,110)

        # Prices Label
        self.price_label = QLabel(self)
        self.price_label.move(160, 100)
        self.price_label.resize(120, 30)
        self.price_label.setText("Price: ")

        # Prices Display
        self.price_counter = QLabel(self)
        self.price_counter.move(230,109)

        # Nutrition Label
        self.nut_label = QLabel(self)
        self.nut_label.move(20, 131)
        self.nut_label.resize(120, 30)
        self.nut_label.setText("Nutrition: ")

        # Nutrition Display
        self.nut_counter = QLabel(self)
        self.nut_counter.move(90,140)

        # Yum Label
        self.yum_label = QLabel(self)
        self.yum_label.move(160, 131)
        self.yum_label.resize(120, 30)
        self.yum_label.setText("Yum: ")

        # Yum Display
        self.yum_counter = QLabel(self)
        self.yum_counter.move(230,140)

        z = 0
        self.breado = QComboBox(self)
        self.breado.addItem('')

        for i in range (0,y_2):
            self.breado.addItem(bread_list[z])
            z += 1


        self.breado.move(150, 44)
        self.breado.currentTextChanged.connect(self.onChanged_bread)
        
        # Non-Necessary edits
        # Window Size
        self.setGeometry(50,50,400,200)
        # Window Title
        self.setWindowTitle("Sandwich Wizard")
        # Make it appear on the window
        self.show()
        
        

    # for when the drop boxes are interacted with  

    def onChanged_bread(self, text):
        print(text)
        if text == "white":
            self.calories_counter.setText(str(white[0]))
            self.calories_counter.adjustSize()
            self.price_counter.setText(str(white[1]))
            self.price_counter.adjustSize()
            self.nut_counter.setText(str(white[2]))
            self.nut_counter.adjustSize()
            self.yum_counter.setText(str(white[3]))
            self.yum_counter.adjustSize()
        elif text == "sourdough":
            self.calories_counter.setText(str(sourdough[0]))
            self.calories_counter.adjustSize()
            self.price_counter.setText(str(sourdough[1]))
            self.price_counter.adjustSize()
            self.nut_counter.setText(str(sourdough[2]))
            self.nut_counter.adjustSize()
            self.yum_counter.setText(str(sourdough[3]))
            self.yum_counter.adjustSize()
        else:
            self.calories_counter.setText(str(wholegrain[0]))
            self.calories_counter.adjustSize()
            self.price_counter.setText(str(wholegrain[1]))
            self.price_counter.adjustSize()
            self.nut_counter.setText(str(wholegrain[2]))
            self.nut_counter.adjustSize()
            self.yum_counter.setText(str(wholegrain[3]))
            self.yum_counter.adjustSize()

        self.bread_label.setText(text)
        self.bread_label.adjustSize()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

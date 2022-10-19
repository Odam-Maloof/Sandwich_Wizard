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

csv_file_2 = pandas.read_csv('sheets/legacy_sheets/meats.csv')
print(csv_file_2)

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

y = 0
z = 1
beef = []
for i in range (0,4):
    beef.append(csv_file_2.iloc[y, z])
    z+= 1

y += 1
z = 1 
chicken = []
for i in range (0,4):
    chicken.append(csv_file_2.iloc[y, z])
    z+= 1

y += 1
z = 1 
lamb = []
for i in range (0,4):
    lamb.append(csv_file_2.iloc[y, z])
    z+= 1

y = len(the_list)

# declare the variables for the summative process
global calorie_1
calorie_1 = str(0)

global calorie_2
calorie_2 = str(0)

global price_1
price_1 = str(0)

global price_2
price_2 = str(0)

global nut_1
nut_1 = str(0)

global nut_2
nut_2 = str(0)

global yum_1
yum_1 = str(0)

global yum_2
yum_2 = str(0)

class Window(QMainWindow): 
     
    def __init__(self):
        super().__init__()


        # Select Bread Label
        self.bread_select = QLabel(self)
        self.bread_select.move(20, 44)
        self.bread_select.resize(120, 30)
        self.bread_select.setText("Select Bread Type: ")

        # Bread Display
        self.bread_label = QLabel(self)
        self.bread_label.move(270,50)

        # Select Ingredients Label
        self.ingred_select = QLabel(self)
        self.ingred_select.move(20, 94)
        self.ingred_select.resize(120, 30)
        self.ingred_select.setText("Select Ingredient: ")

        # Ingredient Display
        self.ingred_label = QLabel(self)
        self.ingred_label.move(270,100)

        # Calories Label
        self.calories_label = QLabel(self)
        self.calories_label.move(20, 201)
        self.calories_label.resize(120, 30)
        self.calories_label.setText("Calories: ")

        # Calories Display
        self.calories_counter = QLabel(self)
        self.calories_counter.move(90,210)

        # Prices Label
        self.price_label = QLabel(self)
        self.price_label.move(160, 200)
        self.price_label.resize(120, 30)
        self.price_label.setText("Price: ")

        # Prices Display
        self.price_counter = QLabel(self)
        self.price_counter.move(230,209)

        # Nutrition Label
        self.nut_label = QLabel(self)
        self.nut_label.move(20, 231)
        self.nut_label.resize(120, 30)
        self.nut_label.setText("Nutrition: ")

        # Nutrition Display
        self.nut_counter = QLabel(self)
        self.nut_counter.move(90,240)

        # Yum Label
        self.yum_label = QLabel(self)
        self.yum_label.move(160, 231)
        self.yum_label.resize(120, 30)
        self.yum_label.setText("Yum: ")

        # Yum Display
        self.yum_counter = QLabel(self)
        self.yum_counter.move(230,240)

        # evaluate button
        button = QPushButton('Evaluate', self)
        button.move(80,150)
        button.clicked.connect(self.total_sums)

        z = 0
        # add the bread box
        self.breado = QComboBox(self)
        self.breado.addItem('')

        # add the ingredient box
        self.combo = QComboBox(self)
        self.combo.addItem('')


        for i in range (0,y_2):
            self.breado.addItem(bread_list[z])
            self.combo.addItem(the_list[z])
            z += 1


        self.breado.move(150, 44)
        self.breado.activated[str].connect(self.onChanged_bread)

        self.combo.move(150, 94) 
        self.combo.activated[str].connect(self.onChanged_standard)

        
        # Non-Necessary edits
        # Window Size
        self.setGeometry(50,50,400,300)
        # Window Title
        self.setWindowTitle("Sandwich Wizard")
        # Make it appear on the window
        self.show()
        
        

    # for when the drop boxes are interacted with  

    def onChanged_standard(self, text):
        print(text)
        global calorie_1
        calorie_1 = str(text)

        global price_1
        price_1 = str(text)

        global nut_1
        nut_1 = str(text)

        global yum_1
        yum_1 = str(text)

        self.ingred_label.setText(text)
        self.ingred_label.adjustSize()

    def onChanged_bread(self, text):
        print(text)
        global calorie_2
        calorie_2 = str(text)

        global price_2
        price_2 = str(text)

        global nut_2
        nut_2 = str(text)

        global yum_2
        yum_2 = str(text)
        
        self.bread_label.setText(text)
        self.bread_label.adjustSize()

    def total_sums(self, text):
        g = 0
        # calories
        # convert calorie 1
        check = calorie_1
   
        if check == "beef":
            check = beef[g]
        elif check == "chicken":
            check = chicken[g]
        elif check == "lamb":
            check = lamb[g]
        else:
            check = 0


        # convert calorie 2
        check_2 = calorie_2

        if check_2 == "white":
            check_2 = white[g]
        elif check_2 == "sourdough":
            check_2 = sourdough[g]
        elif check_2 == "wholegrain":
            check_2 = wholegrain[g]
        else:
            check_2 = 0

        
        calories_overall = check + check_2
        self.calories_counter.setText(str(calories_overall))
        self.calories_counter.adjustSize()

        g += 1
        # prices
        # convert price 1
        check = price_1
   
        if check == "beef":
            check = beef[g]
        elif check == "chicken":
            check = chicken[g]
        elif check == "lamb":
            check = lamb[g]
        else:
            check = 0


        # convert calorie 2
        check_2 = price_2

        if check_2 == "white":
            check_2 = white[g]
        elif check_2 == "sourdough":
            check_2 = sourdough[g]
        elif check_2 == "wholegrain":
            check_2 = wholegrain[g]
        else:
            check_2 = 0

        
        price_overall = check + check_2
        self.price_counter.setText(str(price_overall))
        self.price_counter.adjustSize()

        g += 1
        # nutrition
        # convert nut 1
        check = nut_1
   
        if check == "beef":
            check = beef[g]
        elif check == "chicken":
            check = chicken[g]
        elif check == "lamb":
            check = lamb[g]
        else:
            check = 0


        # convert nut 2
        check_2 = nut_2

        if check_2 == "white":
            check_2 = white[g]
        elif check_2 == "sourdough":
            check_2 = sourdough[g]
        elif check_2 == "wholegrain":
            check_2 = wholegrain[g]
        else:
            check_2 = 0

        
        nut_overall = (check + check_2)/2
        self.nut_counter.setText(str(nut_overall))
        self.nut_counter.adjustSize()

        g += 1
        # yum
        # convert yum 1
        check = yum_1
   
        if check == "beef":
            check = beef[g]
        elif check == "chicken":
            check = chicken[g]
        elif check == "lamb":
            check = lamb[g]
        else:
            check = 0


        # convert yum 2
        check_2 = yum_2

        if check_2 == "white":
            check_2 = white[g]
        elif check_2 == "sourdough":
            check_2 = sourdough[g]
        elif check_2 == "wholegrain":
            check_2 = wholegrain[g]
        else:
            check_2 = 0

        
        yum_overall = (check + check_2)/2
        self.yum_counter.setText(str(yum_overall))
        self.yum_counter.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

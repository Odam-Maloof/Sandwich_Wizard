import sys
import pandas, csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QVBoxLayout


# import the csv file for the meats
meat_csv = pandas.read_csv('sheets/meats.csv')
print(meat_csv)

# turn the csv file into a list for the drop downs
x = 0 
meat_list = []
for i in range (0,3):
    meat_list.append(meat_csv.iloc[x, 0])
    x+= 1
y_meat = len(meat_list)
# import the csv file for the breads
bread_csv = pandas.read_csv('sheets/breads.csv')
print(bread_csv)

# turn the csv file into a list for the drop downs
x = 0
bread_list = []
for i in range (0,3):
    bread_list.append(bread_csv.iloc[x, 0])
    x+= 1
y_bread = len(bread_list)

# import the csv file for the cheeses
cheese_csv = pandas.read_csv('sheets/cheeses.csv')
print(cheese_csv)

# turn the csv file into a list for the drop downs
x = 0
cheese_list = []
for i in range (0,3):
    cheese_list.append(cheese_csv.iloc[x, 0])
    x+= 1
y_cheese = len(cheese_list)

# import the csv file for the sauces
sauce_csv = pandas.read_csv('sheets/sauces.csv')
print(sauce_csv)

# turn the csv file into a list for the drop downs
x = 0
sauce_list = []
for i in range (0,3):
    sauce_list.append(sauce_csv.iloc[x, 0])
    x+= 1
y_sauce = len(sauce_list)

# import the csv file for the salads
salad_csv = pandas.read_csv('sheets/salads.csv')
print(salad_csv)

# turn the csv file into a list for the drop downs
x = 0
salad_list = []
for i in range (0,6):
    salad_list.append(salad_csv.iloc[x, 0])
    x+= 1
y_salad = len(salad_list)

# import the csv file for the salads
extra_csv = pandas.read_csv('sheets/extras.csv')
print(extra_csv)

# turn the csv file into a list for the drop downs
x = 0
extra_list = []
for i in range (0,6):
    extra_list.append(extra_csv.iloc[x, 0])
    x+= 1
y_extra = len(extra_list)

# the lists of calories, and other values for bread
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

# the lists of calories, and other values for meat

y = 0
z = 1
beef = []
for i in range (0,4):
    beef.append(meat_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
chicken = []
for i in range (0,4):
    chicken.append(meat_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
lamb = []
for i in range (0,4):
    lamb.append(meat_csv.iloc[y, z])
    z+= 1

# the lists of calories, and other values for cheese

y = 0
z = 1
edam = []
for i in range (0,4):
    edam.append(cheese_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
colby = []
for i in range (0,4):
    colby.append(cheese_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
cheddar = []
for i in range (0,4):
    cheddar.append(cheese_csv.iloc[y, z])
    z+= 1

# the lists of calories, and other values for sauce

y = 0
z = 1
ranch = []
for i in range (0,4):
    ranch.append(sauce_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
mayo = []
for i in range (0,4):
    mayo.append(sauce_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
ketchup = []
for i in range (0,4):
    ketchup.append(sauce_csv.iloc[y, z])
    z+= 1

# the lists of calories, and other values for salad

y = 0
z = 1
lettuce = []
for i in range (0,4):
    lettuce.append(salad_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
cucumber = []
for i in range (0,4):
    cucumber.append(salad_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
onion = []
for i in range (0,4):
    onion.append(salad_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
capsicum = []
for i in range (0,4):
    capsicum.append(salad_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
carrot = []
for i in range (0,4):
    carrot.append(salad_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
olive = []
for i in range (0,4):
    olive.append(salad_csv.iloc[y, z])
    z+= 1

# the lists of calories, and other values for extras

y = 0
z = 1
bacon = []
for i in range (0,4):
    bacon.append(extra_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
pink_sauce = []
for i in range (0,4):
    pink_sauce.append(extra_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
paprika = []
for i in range (0,4):
    paprika.append(extra_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
salt_pepper = []
for i in range (0,4):
    salt_pepper.append(extra_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
pepper = []
for i in range (0,4):
    pepper.append(extra_csv.iloc[y, z])
    z+= 1

y += 1
z = 1 
salt = []
for i in range (0,4):
    salt.append(extra_csv.iloc[y, z])
    z+= 1

checker = ["once"]

# declare the variables for the summative process
global calorie_1, calorie_2, calorie_3, calorie_4, calorie_5, calorie_6, calorie_7, calorie_8, calorie_9, calorie_10
calorie_1 = str(0)
calorie_2 = str(0)
calorie_3 = str(0)
calorie_4 = str(0)
calorie_5 = str(0)
calorie_6 = str(0)
calorie_7 = str(0)
calorie_8 = str(0)
calorie_9 = str(0)
calorie_10 = str(0)

global price_1, price_2, price_3, price_4, price_5, price_6, price_7, price_8, price_9, price_10
price_1 = str(0)
price_2 = str(0)
price_3 = str(0)
price_4 = str(0)
price_5 = str(0)
price_6 = str(0)
price_7 = str(0)
price_8 = str(0)
price_9 = str(0)
price_10 = str(0)

global nut_1, nut_2, nut_3, nut_4, nut_5, nut_6, nut_7, nut_8, nut_9, nut_10
nut_1 = str(0)
nut_2 = str(0)
nut_3 = str(0)
nut_4 = str(0)
nut_5 = str(0)
nut_6 = str(0)
nut_7 = str(0)
nut_8 = str(0)
nut_9 = str(0)
nut_10 = str(0)


global yum_1, yum_2, yum_3, yum_4, yum_5, yum_6, yum_7, yum_8, yum_9, yum_10
yum_1 = str(0)
yum_2 = str(0)
yum_3 = str(0)
yum_4 = str(0)
yum_5 = str(0)
yum_6 = str(0)
yum_7 = str(0)
yum_8 = str(0)
yum_9 = str(0)
yum_10 = str(0)

class Window(QMainWindow): 
    def __init__(self):
        super().__init__()
        

        # Select Bread Label
        self.bread_select = QLabel(self)
        self.bread_select.move(20, 44)
        self.bread_select.resize(120, 30)
        self.bread_select.setText("Select Bread Type: ")

        # Select Meat Label
        self.meat_select = QLabel(self)
        self.meat_select.move(20, 94)
        self.meat_select.resize(120, 30)
        self.meat_select.setText("Select Meat: ")

        # Select Cheese Label
        self.cheese_select = QLabel(self)
        self.cheese_select.move(20, 144)
        self.cheese_select.resize(120, 30)
        self.cheese_select.setText("Select Cheese: ")

        # Select Sauce Label
        self.sauce_select = QLabel(self)
        self.sauce_select.move(20, 194)
        self.sauce_select.resize(120, 30)
        self.sauce_select.setText("Choose a sauce: ")

        # Select Salad Label 1
        self.salad_select_1 = QLabel(self)
        self.salad_select_1.move(20, 244)
        self.salad_select_1.resize(120, 30)
        self.salad_select_1.setText("Choose salad 1: ")

        # Select Salad Label 2
        self.salad_select_2 = QLabel(self)
        self.salad_select_2.move(20, 294)
        self.salad_select_2.resize(120, 30)
        self.salad_select_2.setText("Choose salad 2: ")

        # Select Salad Label 3
        self.salad_select_3 = QLabel(self)
        self.salad_select_3.move(20, 344)
        self.salad_select_3.resize(120, 30)
        self.salad_select_3.setText("Choose salad 3: ")

        # Select Extra Label 1
        self.extra_select_1 = QLabel(self)
        self.extra_select_1.move(20, 394)
        self.extra_select_1.resize(120, 30)
        self.extra_select_1.setText("Choose extra 1: ")

        # Select Extra Label 2
        self.extra_select_2 = QLabel(self)
        self.extra_select_2.move(20, 444)
        self.extra_select_2.resize(120, 30)
        self.extra_select_2.setText("Choose extra 2: ")

        # Select Extra Label 3
        self.extra_select_3 = QLabel(self)
        self.extra_select_3.move(20, 494)
        self.extra_select_3.resize(120, 30)
        self.extra_select_3.setText("Choose extra 3: ")

        # Calories Label
        self.calories_label = QLabel(self)
        self.calories_label.move(20, 601)
        self.calories_label.resize(120, 30)
        self.calories_label.setText("Calories: ")

        # Calories Display
        self.calories_counter = QLabel(self)
        self.calories_counter.move(90,609)

        # Prices Label
        self.price_label = QLabel(self)
        self.price_label.move(160, 600)
        self.price_label.resize(120, 30)
        self.price_label.setText("Price: ")

        # Prices Display
        self.price_counter = QLabel(self)
        self.price_counter.move(230,609)

        # Nutrition Label
        self.nut_label = QLabel(self)
        self.nut_label.move(20, 631)
        self.nut_label.resize(120, 30)
        self.nut_label.setText("Nutrition: ")

        # Nutrition Display
        self.nut_counter = QLabel(self)
        self.nut_counter.move(90,640)

        # Yum Label
        self.yum_label = QLabel(self)
        self.yum_label.move(160, 631)
        self.yum_label.resize(120, 30)
        self.yum_label.setText("Yum: ")

        # Yum Display
        self.yum_counter = QLabel(self)
        self.yum_counter.move(230,640)

        # evaluate button
        button = QPushButton('Evaluate', self)
        button.move(80,550)
        button.clicked.connect(self.total_sums)

        # add the bread box
        self.breado = QComboBox(self)
        self.breado.addItem('')
        self.breado.move(150, 44)

        # add the meat box
        self.meato = QComboBox(self)
        self.meato.addItem('')
        self.meato.move(150, 94)

        # add the cheese box
        self.cheeto = QComboBox(self)
        self.cheeto.addItem('')
        self.cheeto.move(150, 144) 

        # add the sauce box
        self.saucedo = QComboBox(self)
        self.saucedo.addItem('')
        self.saucedo.move(150, 194) 

        # add the first salad box
        self.salado_1 = QComboBox(self)
        self.salado_1.addItem('')
        self.salado_1.move(150, 244)

        # add the second salad box
        self.salado_2 = QComboBox(self)
        self.salado_2.addItem('')
        self.salado_2.move(150, 294)

        # add the third salad box
        self.salado_3 = QComboBox(self)
        self.salado_3.addItem('')
        self.salado_3.move(150, 344)

        # add the first extras box
        self.extro_1 = QComboBox(self)
        self.extro_1.addItem('')
        self.extro_1.move(150, 394)

        # add the second extras box
        self.extro_2 = QComboBox(self)
        self.extro_2.addItem('')
        self.extro_2.move(150, 444)

        # add the third extras box
        self.extro_3 = QComboBox(self)
        self.extro_3.addItem('')
        self.extro_3.move(150, 494)

        z = 0
        for i in range (0,y_meat):
            self.breado.addItem(bread_list[z])
            self.meato.addItem(meat_list[z])
            self.cheeto.addItem(cheese_list[z])
            self.saucedo.addItem(sauce_list[z])
            z += 1
        z = 0
        for i in range (0,y_salad):
            self.salado_1.addItem(salad_list[z])
            self.salado_2.addItem(salad_list[z])
            self.salado_3.addItem(salad_list[z])
            self.extro_1.addItem(extra_list[z])
            self.extro_2.addItem(extra_list[z])
            self.extro_3.addItem(extra_list[z])
            z += 1

        # the on activation commands for each of the combo boxes
        self.breado.activated[str].connect(self.onChanged_bread)         
        self.meato.activated[str].connect(self.onChanged_meat)
        self.cheeto.activated[str].connect(self.onChanged_cheese)
        self.saucedo.activated[str].connect(self.onChanged_sauce)
        self.salado_1.activated[str].connect(self.onChanged_salad_1)
        self.salado_2.activated[str].connect(self.onChanged_salad_2)
        self.salado_3.activated[str].connect(self.onChanged_salad_3)
        self.extro_1.activated[str].connect(self.onChanged_extra_1)
        self.extro_2.activated[str].connect(self.onChanged_extra_2)
        self.extro_3.activated[str].connect(self.onChanged_extra_3)

        
        # Non-Necessary edits
        # Window Size
        self.setGeometry(50,50,280,800)
        # Window Title
        self.setWindowTitle("Sandwich Wizard")
        # Make it appear on the window
        self.show()
        
        

    # for when the drop boxes are interacted with  

    def onChanged_meat(self, text):
        print(text)
        global calorie_1, price_1, nut_1, yum_1
        calorie_1 = str(text)
        price_1 = str(text)
        nut_1 = str(text)
        yum_1 = str(text)

    def onChanged_bread(self, text):
        print(text)
        global calorie_2, price_2, nut_2, yum_2
        calorie_2 = str(text)
        price_2 = str(text)
        nut_2 = str(text)
        yum_2 = str(text)

    def onChanged_cheese(self, text):
        print(text)
        global calorie_3, price_3, nut_3, yum_3
        calorie_3 = str(text)
        price_3 = str(text)
        nut_3 = str(text)
        yum_3 = str(text)

    def onChanged_sauce(self, text):
        print(text)
        global calorie_4, price_4, nut_4, yum_4
        calorie_4 = str(text)
        price_4 = str(text)
        nut_4 = str(text)
        yum_4 = str(text)

    def onChanged_salad_1(self, text):
        print(text)
        global calorie_5, price_5, nut_5, yum_5
        calorie_5 = str(text)
        price_5 = str(text)
        nut_5 = str(text)
        yum_5 = str(text)
        '''
        if text != '':
            removal_1 = self.salado_2.findText(text)
            self.salado_2.removeItem(removal_1)
            removal_2 = self.salado_3.findText(text)
            self.salado_3.removeItem(removal_2)      
        else:
            pass
        '''
    def onChanged_salad_2(self, text):
        print(text)
        global calorie_6, price_6, nut_6, yum_6
        calorie_6 = str(text)
        price_6 = str(text)
        nut_6 = str(text)
        yum_6 = str(text)
        '''
        if text != '':
            salad_2_previous_text = text
            removal_1 = self.salado_1.findText(text)
            self.salado_1.removeItem(removal_1)
            removal_2 = self.salado_3.findText(text)
            self.salado_3.removeItem(removal_2)
        else:
            pass
        if len(checker) != 1:
            self.salado_1.addItem(salad_2_previous_text)
            self.salado_3.addItem(salad_2_previous_text)
        else:
            checker.append("twice")
        '''

            


    def onChanged_salad_3(self, text):
        print(text)
        global calorie_7, price_7, nut_7, yum_7
        calorie_7 = str(text)
        price_7 = str(text)
        nut_7 = str(text)
        yum_7 = str(text)
        '''
        if text != '':
            removal_1 = self.salado_1.findText(text)
            self.salado_1.removeItem(removal_1)
            removal_2 = self.salado_2.findText(text)
            self.salado_2.removeItem(removal_2)
        else:
            pass
        '''

    def onChanged_extra_1(self, text):
        print(text)
        global calorie_8, price_8, nut_8, yum_8
        calorie_8 = str(text)
        price_8 = str(text)
        nut_8 = str(text)
        yum_8 = str(text)

    def onChanged_extra_2(self, text):
        print(text)
        global calorie_9, price_9, nut_9, yum_9
        calorie_9 = str(text)
        price_9 = str(text)
        nut_9 = str(text)
        yum_9 = str(text)

    def onChanged_extra_3(self, text):
        print(text)
        global calorie_10, price_10, nut_10, yum_10
        calorie_10 = str(text)
        price_10 = str(text)
        nut_10 = str(text)
        yum_10 = str(text)
    

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

        # convert calorie 3
        check_3 = calorie_3

        if check_3 == "edam":
            check_3 = edam[g]
        elif check_3 == "colby":
            check_3 = colby[g]
        elif check_3 == "cheddar":
            check_3 = cheddar[g]
        else:
            check_3 = 0

        # convert calorie 4
        check_4 = calorie_4

        if check_4 == "ranch":
            check_4 = ranch[g]
        elif check_4 == "mayo":
            check_4 = mayo[g]
        elif check_4 == "ketchup":
            check_4 = ketchup[g]
        else:
            check_4 = 0

        # convert calorie 5
        check_5 = calorie_5

        if check_5 == "lettuce":
            check_5 = lettuce[g]
        elif check_5 == "cucumber":
            check_5 = cucumber[g]
        elif check_5 == "onion":
            check_5 = onion[g]
        elif check_5 == "capsicum":
            check_5 = capsicum[g]
        elif check_5 == "carrot":
            check_5 = carrot[g]
        elif check_5 == "olive":
            check_5 = olive[g]
        else:
            check_5 = 0

        # convert calorie 6
        check_6 = calorie_6

        if check_6 == "lettuce":
            check_6 = lettuce[g]
        elif check_6 == "cucumber":
            check_6 = cucumber[g]
        elif check_6 == "onion":
            check_6 = onion[g]
        elif check_6 == "capsicum":
            check_6 = capsicum[g]
        elif check_6 == "carrot":
            check_6 = carrot[g]
        elif check_6 == "olive":
            check_6 = olive[g]
        else:
            check_6 = 0

        # convert calorie 7
        check_7 = calorie_7

        if check_7 == "lettuce":
            check_7 = lettuce[g]
        elif check_7 == "cucumber":
            check_7 = cucumber[g]
        elif check_7 == "onion":
            check_7 = onion[g]
        elif check_7 == "capsicum":
            check_7 = capsicum[g]
        elif check_7 == "carrot":
            check_7 = carrot[g]
        elif check_7 == "olive":
            check_7 = olive[g]
        else:
            check_7 = 0

        # convert calorie 8
        check_8 = calorie_8

        if check_8 == "bacon":
            check_8 = bacon[g]
        elif check_8 == "pink sauce":
            check_8 = pink_sauce[g]
        elif check_8 == "paprika":
            check_8 = paprika[g]
        elif check_8 == "salt & pepper":
            check_8 = salt_pepper[g]
        elif check_8 == "pepper":
            check_8 = pepper[g]
        elif check_8 == "salt":
            check_8 = salt[g]
        else:
            check_8 = 0

        # convert calorie 9
        check_9 = calorie_9

        if check_9 == "bacon":
            check_9 = bacon[g]
        elif check_9 == "pink sauce":
            check_9 = pink_sauce[g]
        elif check_9 == "paprika":
            check_9 = paprika[g]
        elif check_9 == "salt & pepper":
            check_9 = salt_pepper[g]
        elif check_9 == "pepper":
            check_9 = pepper[g]
        elif check_9 == "salt":
            check_9 = salt[g]
        else:
            check_9 = 0

        # convert calorie 10
        check_10 = calorie_10

        if check_10 == "bacon":
            check_10 = bacon[g]
        elif check_10 == "pink sauce":
            check_10 = pink_sauce[g]
        elif check_10 == "paprika":
            check_10 = paprika[g]
        elif check_10 == "salt & pepper":
            check_10 = salt_pepper[g]
        elif check_10 == "pepper":
            check_10 = pepper[g]
        elif check_10 == "salt":
            check_10 = salt[g]
        else:
            check_10 = 0
        
        calories_overall = check + check_2 + check_3 + check_4 + check_5 + check_6 + check_7 + check_8 + check_9 + check_10
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


        # convert price 2
        check_2 = price_2

        if check_2 == "white":
            check_2 = white[g]
        elif check_2 == "sourdough":
            check_2 = sourdough[g]
        elif check_2 == "wholegrain":
            check_2 = wholegrain[g]
        else:
            check_2 = 0

        # convert price 3
        check_3 = price_3

        if check_3 == "edam":
            check_3 = edam[g]
        elif check_3 == "colby":
            check_3 = colby[g]
        elif check_3 == "cheddar":
            check_3 = cheddar[g]
        else:
            check_3 = 0

        # convert price 4
        check_4 = price_4

        if check_4 == "ranch":
            check_4 = ranch[g]
        elif check_4 == "mayo":
            check_4 = mayo[g]
        elif check_4 == "ketchup":
            check_4 = ketchup[g]
        else:
            check_4 = 0

        # convert price 5
        check_5 = price_5

        if check_5 == "lettuce":
            check_5 = lettuce[g]
        elif check_5 == "cucumber":
            check_5 = cucumber[g]
        elif check_5 == "onion":
            check_5 = onion[g]
        elif check_5 == "capsicum":
            check_5 = capsicum[g]
        elif check_5 == "carrot":
            check_5 = carrot[g]
        elif check_5 == "olive":
            check_5 = olive[g]
        else:
            check_5 = 0

        # convert price 6
        check_6 = price_6

        if check_6 == "lettuce":
            check_6 = lettuce[g]
        elif check_6 == "cucumber":
            check_6 = cucumber[g]
        elif check_6 == "onion":
            check_6 = onion[g]
        elif check_6 == "capsicum":
            check_6 = capsicum[g]
        elif check_6 == "carrot":
            check_6 = carrot[g]
        elif check_6 == "olive":
            check_6 = olive[g]
        else:
            check_6 = 0

        # convert price 7
        check_7 = price_7

        if check_7 == "lettuce":
            check_7 = lettuce[g]
        elif check_7 == "cucumber":
            check_7 = cucumber[g]
        elif check_7 == "onion":
            check_7 = onion[g]
        elif check_7 == "capsicum":
            check_7 = capsicum[g]
        elif check_7 == "carrot":
            check_7 = carrot[g]
        elif check_7 == "olive":
            check_7 = olive[g]
        else:
            check_7 = 0

        # convert price 8
        check_8 = price_8

        if check_8 == "bacon":
            check_8 = bacon[g]
        elif check_8 == "pink sauce":
            check_8 = pink_sauce[g]
        elif check_8 == "paprika":
            check_8 = paprika[g]
        elif check_8 == "salt & pepper":
            check_8 = salt_pepper[g]
        elif check_8 == "pepper":
            check_8 = pepper[g]
        elif check_8 == "salt":
            check_8 = salt[g]
        else:
            check_8 = 0

        # convert price 9
        check_9 = price_9

        if check_9 == "bacon":
            check_9 = bacon[g]
        elif check_9 == "pink sauce":
            check_9 = pink_sauce[g]
        elif check_9 == "paprika":
            check_9 = paprika[g]
        elif check_9 == "salt & pepper":
            check_9 = salt_pepper[g]
        elif check_9 == "pepper":
            check_9 = pepper[g]
        elif check_9 == "salt":
            check_9 = salt[g]
        else:
            check_9 = 0

        # convert price 10
        check_10 = price_10

        if check_10 == "bacon":
            check_10 = bacon[g]
        elif check_10 == "pink sauce":
            check_10 = pink_sauce[g]
        elif check_10 == "paprika":
            check_10 = paprika[g]
        elif check_10 == "salt & pepper":
            check_10 = salt_pepper[g]
        elif check_10 == "pepper":
            check_10 = pepper[g]
        elif check_10 == "salt":
            check_10 = salt[g]
        else:
            check_10 = 0

        price_overall = check + check_2 + check_3 + check_4 + check_5 + check_6 + check_7 + check_8 + check_9 + check_10
        price_overall = str(round(price_overall, 2))
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

        # convert nut 3
        check_3 = nut_3

        if check_3 == "edam":
            check_3 = edam[g]
        elif check_3 == "colby":
            check_3 = colby[g]
        elif check_3 == "cheddar":
            check_3 = cheddar[g]
        else:
            check_3 = 0

        # convert nut 4
        check_4 = nut_4

        if check_4 == "ranch":
            check_4 = ranch[g]
        elif check_4 == "mayo":
            check_4 = mayo[g]
        elif check_4 == "ketchup":
            check_4 = ketchup[g]
        else:
            check_4 = 0

        # convert nut 5
        check_5 = nut_5

        if check_5 == "lettuce":
            check_5 = lettuce[g]
        elif check_5 == "cucumber":
            check_5 = cucumber[g]
        elif check_5 == "onion":
            check_5 = onion[g]
        elif check_5 == "capsicum":
            check_5 = capsicum[g]
        elif check_5 == "carrot":
            check_5 = carrot[g]
        elif check_5 == "olive":
            check_5 = olive[g]
        else:
            check_5 = 0

        # convert nut 6
        check_6 = nut_6

        if check_6 == "lettuce":
            check_6 = lettuce[g]
        elif check_6 == "cucumber":
            check_6 = cucumber[g]
        elif check_6 == "onion":
            check_6 = onion[g]
        elif check_6 == "capsicum":
            check_6 = capsicum[g]
        elif check_6 == "carrot":
            check_6 = carrot[g]
        elif check_6 == "olive":
            check_6 = olive[g]
        else:
            check_6 = 0

        # convert nut 7
        check_7 = nut_7

        if check_7 == "lettuce":
            check_7 = lettuce[g]
        elif check_7 == "cucumber":
            check_7 = cucumber[g]
        elif check_7 == "onion":
            check_7 = onion[g]
        elif check_7 == "capsicum":
            check_7 = capsicum[g]
        elif check_7 == "carrot":
            check_7 = carrot[g]
        elif check_7 == "olive":
            check_7 = olive[g]
        else:
            check_7 = 0

        # convert nut 8
        check_8 = nut_8

        if check_8 == "bacon":
            check_8 = bacon[g]
        elif check_8 == "pink sauce":
            check_8 = pink_sauce[g]
        elif check_8 == "paprika":
            check_8 = paprika[g]
        elif check_8 == "salt & pepper":
            check_8 = salt_pepper[g]
        elif check_8 == "pepper":
            check_8 = pepper[g]
        elif check_8 == "salt":
            check_8 = salt[g]
        else:
            check_8 = 0

        # convert nut 9
        check_9 = nut_9

        if check_9 == "bacon":
            check_9 = bacon[g]
        elif check_9 == "pink sauce":
            check_9 = pink_sauce[g]
        elif check_9 == "paprika":
            check_9 = paprika[g]
        elif check_9 == "salt & pepper":
            check_9 = salt_pepper[g]
        elif check_9 == "pepper":
            check_9 = pepper[g]
        elif check_9 == "salt":
            check_9 = salt[g]
        else:
            check_9 = 0

        # convert nut 10
        check_10 = nut_10

        if check_10 == "bacon":
            check_10 = bacon[g]
        elif check_10 == "pink sauce":
            check_10 = pink_sauce[g]
        elif check_10 == "paprika":
            check_10 = paprika[g]
        elif check_10 == "salt & pepper":
            check_10 = salt_pepper[g]
        elif check_10 == "pepper":
            check_10 = pepper[g]
        elif check_10 == "salt":
            check_10 = salt[g]
        else:
            check_10 = 0
        
        nut_overall = (check + check_2 + check_3 + check_4 + check_5 + check_6 + check_7 + check_8 + check_9 + check_10)/10
        nut_overall = str(round(nut_overall, 2))
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

        # convert yum 3
        check_3 = yum_3

        if check_3 == "edam":
            check_3 = edam[g]
        elif check_3 == "colby":
            check_3 = colby[g]
        elif check_3 == "cheddar":
            check_3 = cheddar[g]
        else:
            check_3 = 0

        # convert yum 4
        check_4 = yum_4

        if check_4 == "ranch":
            check_4 = ranch[g]
        elif check_4 == "mayo":
            check_4 = mayo[g]
        elif check_4 == "ketchup":
            check_4 = ketchup[g]
        else:
            check_4 = 0

        # convert yum 5
        check_5 = yum_5

        if check_5 == "lettuce":
            check_5 = lettuce[g]
        elif check_5 == "cucumber":
            check_5 = cucumber[g]
        elif check_5 == "onion":
            check_5 = onion[g]
        elif check_5 == "capsicum":
            check_5 = capsicum[g]
        elif check_5 == "carrot":
            check_5 = carrot[g]
        elif check_5 == "olive":
            check_5 = olive[g]
        else:
            check_5 = 0

        # convert yum 6
        check_6 = yum_6

        if check_6 == "lettuce":
            check_6 = lettuce[g]
        elif check_6 == "cucumber":
            check_6 = cucumber[g]
        elif check_6 == "onion":
            check_6 = onion[g]
        elif check_6 == "capsicum":
            check_6 = capsicum[g]
        elif check_6 == "carrot":
            check_6 = carrot[g]
        elif check_6 == "olive":
            check_6 = olive[g]
        else:
            check_6 = 0

        # convert yum 7
        check_7 = yum_7

        if check_7 == "lettuce":
            check_7 = lettuce[g]
        elif check_7 == "cucumber":
            check_7 = cucumber[g]
        elif check_7 == "onion":
            check_7 = onion[g]
        elif check_7 == "capsicum":
            check_7 = capsicum[g]
        elif check_7 == "carrot":
            check_7 = carrot[g]
        elif check_7 == "olive":
            check_7 = olive[g]
        else:
            check_7 = 0
        
        # convert yum 8
        check_8 = yum_8

        if check_8 == "bacon":
            check_8 = bacon[g]
        elif check_8 == "pink sauce":
            check_8 = pink_sauce[g]
        elif check_8 == "paprika":
            check_8 = paprika[g]
        elif check_8 == "salt & pepper":
            check_8 = salt_pepper[g]
        elif check_8 == "pepper":
            check_8 = pepper[g]
        elif check_8 == "salt":
            check_8 = salt[g]
        else:
            check_8 = 0

        # convert yum 9
        check_9 = yum_9

        if check_9 == "bacon":
            check_9 = bacon[g]
        elif check_9 == "pink sauce":
            check_9 = pink_sauce[g]
        elif check_9 == "paprika":
            check_9 = paprika[g]
        elif check_9 == "salt & pepper":
            check_9 = salt_pepper[g]
        elif check_9 == "pepper":
            check_9 = pepper[g]
        elif check_9 == "salt":
            check_9 = salt[g]
        else:
            check_9 = 0

        # convert yum 10
        check_10 = yum_10

        if check_10 == "bacon":
            check_10 = bacon[g]
        elif check_10 == "pink sauce":
            check_10 = pink_sauce[g]
        elif check_10 == "paprika":
            check_10 = paprika[g]
        elif check_10 == "salt & pepper":
            check_10 = salt_pepper[g]
        elif check_10 == "pepper":
            check_10 = pepper[g]
        elif check_10 == "salt":
            check_10 = salt[g]
        else:
            check_10 = 0

        yum_overall = (check + check_2 + check_3 + check_4 + check_5 + check_6 + check_7 + check_8 + check_9 + check_10)/10
        yum_overall = str(round(yum_overall, 2))
        self.yum_counter.setText(str(yum_overall))
        self.yum_counter.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

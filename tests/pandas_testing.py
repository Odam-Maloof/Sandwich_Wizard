import pandas

col_list = ["meat"]
csv_file = pandas.read_csv('sheets/book.csv', usecols=col_list)
print(csv_file)
# print(type(csv_file))

x = 0 
the_list = []
for i in range (0,3):
    the_list.append(csv_file.iloc[x, 0])
    x+= 1
y = len(the_list)
print(the_list)
print()

bread_csv = pandas.read_csv('sheets/breads.csv')
print(bread_csv)

y = 0
z = 1 
white = []
for i in range (0,4):
    white.append(bread_csv.iloc[y, z])
    z+= 1
print(white)

y += 1
z = 1 
sourdough = []
for i in range (0,4):
    sourdough.append(bread_csv.iloc[y, z])
    z+= 1
print(sourdough)

y += 1
z = 1 
wheatmeal = []
for i in range (0,4):
    wheatmeal.append(bread_csv.iloc[y, z])
    z+= 1
print(wheatmeal)

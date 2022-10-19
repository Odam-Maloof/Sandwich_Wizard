from tkinter import *

window = Tk()

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# set the features of the GUI which won't change
# set the title
window.title("Sandwich Wizard")

# set the dimensions of the windows
window.geometry("400x600")

# run the window on loop
window.mainloop()

from tkinter import *
import tkinter as tk

window = tk.Tk()

# ingredients widget
w = tk.Label(window, text="Ingredients", bg="blue", fg="white")
w.pack(padx=5, ipadx=20, pady=0, side=tk.LEFT)
w.configure(font=("Comic Sans MS", 20))

# clear widget
w = tk.Label(window, text="Clear", bg="white", fg="black") 
w.pack(padx=5, ipadx=20, pady=0, side=tk.LEFT)
w.configure(font=("Comic Sans MS", 20))

# set the features of the GUI which won't change
# set the title
window.title("Sandwich Wizard")

# set the dimensions of the windows
# window.geometry("400x600")

# run the window on loop
window.mainloop()

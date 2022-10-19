# import PyQt5
import PyQt5
from PyQt5.QtWidgets import QApplication, QLabel

# creates the Qapplication, a requirement of PyQt5
app = QApplication([])
label = QLabel('Sandwich Wizard')
label.show()

# this runs and keeps the window running
app.exec_()

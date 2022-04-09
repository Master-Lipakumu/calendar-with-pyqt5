from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

"""apres avoir fait tout
 ces importations nous allons
  passez au code lui meme"""

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #reglage du titre
        self.setWindowTitle("Master Lipakumu")
        #reglage du geometry(dimension)
        self.setGeometry(100, 100, 600, 400)
        #appel de la methode
        self.UiComponents()
        #demarez tout les widgets
        self.show()
#methode pour le components
    def UiComponents(self):
        #creation de l'objet Qcalendarwidgets
        calendar = QCalendarWidget(self)
        # reglage du geometry du calendar
        calendar.setGeometry(10, 10, 400, 250)
        #creation du boutton suivant
        push = QPushButton("année suivante", self)
        #reglage du geometry du boutton
        push.setGeometry(120, 280, 100, 40)
        #reglage de l'action du boutton
        push.clicked.connect(lambda: do_action())
        def do_action():
            calendar.showNextYear()


#creation de l'application qt
App = QApplication(sys.argv)


#creation de l'instance window
window = Window()

# demarage de l'application

sys.exit(App.exec())

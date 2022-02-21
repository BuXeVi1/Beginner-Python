from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainwindow

import sys

def window():
    app=QApplication(sys.argv)
    window=QMainwindow()
    window.setGeometry(200,200,400,300)
    window.setWindowTitle("Beginner GCS")
    window.show()
    sys.exit(app.exec_())

window()
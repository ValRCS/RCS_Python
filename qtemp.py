import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import uic

# I created main.ui in QTDesigner found in ProgramData/Anaconda3/Library/bin on Windows
uifile = os.path.join(os.getcwd(), 'UI', 'main.ui') 
print(uifile)
form, base = uic.loadUiType(uifile)

class Example(base, form):
    def __init__(self):
        super(base,self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mpage = Example()
    mpage.show()
    sys.exit(app.exec_())

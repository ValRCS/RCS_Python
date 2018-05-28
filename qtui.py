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
        self.actionQuit.triggered.connect(self.actionQuit_slot)
        self.radioButton_2.toggled.connect(self.radioButton_2_slot)
        self.horizontalSlider.valueChanged.connect(self.valuechange_slot)
        self.dial.valueChanged.connect(self.dial_slot)
        #.valueChanged.connect(self.valuechange)

    def dial_slot(self):
        print(f'Dial value {self.dial.value()}')
        self.lcdNumber.display(self.dial.value())

    def actionQuit_slot(self):
        print('Going to Quit Seriously!')
        sys.exit(app.exec_())

    def radioButton_2_slot(self): #Notice how it also works when connected Radio Button 1 is toggled!
        print('Radio Button Toggled!')

    def valuechange_slot(self):
        print(f'Slider Value: {self.horizontalSlider.value()}')
        self.mysliderLabel.setText(f'Slider Value: {self.horizontalSlider.value()}')


if __name__ == '__main__':
    print('Starting qtui')
    app = QApplication(sys.argv)
    mpage = Example()
    mpage.show()
    sys.exit(app.exec_())

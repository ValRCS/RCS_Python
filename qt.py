import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
    app = QApplication(sys.argv) #here we use optional command line arguments directly without argparse

    w = QWidget()
    w.resize(300, 200) # initial size
    w.move(100,200) # just move to a specific space on screen
    w.setWindowTitle('First QT App')
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
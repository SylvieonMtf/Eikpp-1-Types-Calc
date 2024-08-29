import sys
from PyQt5.QtWidgets import QApplication, QDialog
from SylvieCalc import Ui_Form 

class MainWindow(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

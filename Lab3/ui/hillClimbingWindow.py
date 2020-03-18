from PyQt5.QtWidgets import QDesktopWidget, QMainWindow


class HillClimbingWindow(QMainWindow):
    def __init__(self, parent=None):
        super(HillClimbingWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hill Climbing')
        self.resize(400, 400)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

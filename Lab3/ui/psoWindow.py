from PyQt5.QtWidgets import QDesktopWidget, QMainWindow


class PSOWindow(QMainWindow):
    def __init__(self, parent=None):
        super(PSOWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Particle Swarm Optimisation')
        self.resize(400, 400)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

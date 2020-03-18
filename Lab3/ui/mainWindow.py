import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QDesktopWidget, QMainWindow, QVBoxLayout, \
    QHBoxLayout

from Lab3.ui.eaWindow import EAWindow
from Lab3.ui.hillClimbingWindow import HillClimbingWindow
from Lab3.ui.psoWindow import PSOWindow


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.hillClimbingWindow = None
        self.ea = None
        self.pso = None
        self.initUI()

    def initUI(self):
        self.resize(400, 400)
        self.center()
        self.setWindowTitle('AI')

        layout = QHBoxLayout(self)
        hillClimbingButton = QPushButton('Hill Climbing')
        hillClimbingButton.clicked.connect(self.openHillClimbing)
        eaButton = QPushButton('Evolutionary Algorithm')
        eaButton.clicked.connect(self.openEA)
        psoButton = QPushButton('Particle Swarm Optimisation ')
        psoButton.clicked.connect(self.openPSO)

        layout.addWidget(hillClimbingButton)
        layout.addWidget(eaButton)
        layout.addWidget(psoButton)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openHillClimbing(self):
        self.hillClimbingWindow = HillClimbingWindow()
        self.hillClimbingWindow.show()
        self.hide()

    def openEA(self):
        self.ea = EAWindow()
        self.ea.show()
        self.hide()

    def openPSO(self):
        self.pso = PSOWindow()
        self.pso.show()
        self.hide()


def run():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

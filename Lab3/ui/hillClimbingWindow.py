from PyQt5.QtWidgets import *

from Lab3.controller.hillClimbing.hillClimbingSimulation import HillClimbingSimulation


class HillClimbingWindow(QMainWindow):
    def __init__(self, parent=None):
        super(HillClimbingWindow, self).__init__(parent)
        self.sp: QSpinBox = None
        self.controller: HillClimbingSimulation = None
        self.console: QTextEdit = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hill Climbing')
        self.resize(400, 400)
        self.center()

        self.sp = QSpinBox()
        self.sp.setValue(5)
        layout = QVBoxLayout()
        layout.addWidget(self.sp)

        buttonLayout = QHBoxLayout()
        button = QPushButton("Begin")
        button.clicked.connect(self.beginAlg)
        buttonLayout.addWidget(button)

        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.cancelAlg)
        buttonLayout.addWidget(cancelButton)

        layout.addLayout(buttonLayout)

        self.console = QTextEdit()
        self.console.setEnabled(False)
        self.console.setFontPointSize(20)
        layout.addWidget(self.console)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def beginAlg(self):
        if self.controller is not None:
            self.controller.requestInterruption()
        self.controller = HillClimbingSimulation(self.sp.value())
        self.controller.progress.connect(self.progress)
        self.controller.start()

    def progress(self, fitness, board):
        self.console.setText("Fitness: " + str(fitness) + "\n\n" + str(board))

    def cancelAlg(self):
        self.controller.requestInterruption()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

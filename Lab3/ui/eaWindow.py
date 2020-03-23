from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from Lab3.controller.ea.eaSimulation import EASimulation
from Lab3.controller.ea.validation import Validation


class EAWindow(QMainWindow):
    def __init__(self, parent=None):
        super(EAWindow, self).__init__(parent)
        self.size: QSpinBox = None
        self.populationSize: QSpinBox = None
        self.mutationChance: QDoubleSpinBox = None
        self.generations: QSpinBox = None
        self.controller: EASimulation = None
        self.validation: Validation = None
        self.console: QTextEdit = None
        self.avg: QLineEdit = None
        self.graphWidget: PlotWidget = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Evolutionary Algorithm')
        self.resize(400, 400)
        self.center()

        layout = QVBoxLayout()
        data = QHBoxLayout()

        label1 = QLabel("Board size:")
        self.size = QSpinBox()
        self.size.setValue(5)
        data.addWidget(label1)
        data.addWidget(self.size)

        label2 = QLabel("Population size:")
        self.populationSize = QSpinBox()
        self.populationSize.setMaximum(200)
        self.populationSize.setValue(40)
        data.addWidget(label2)
        data.addWidget(self.populationSize)

        label3 = QLabel("Mutation chance:")
        self.mutationChance = QDoubleSpinBox()
        self.mutationChance.setSingleStep(0.01)
        self.mutationChance.setValue(0.2)
        data.addWidget(label3)
        data.addWidget(self.mutationChance)

        label4 = QLabel("Generations: ")
        self.generations = QSpinBox()
        self.generations.setMaximum(100000000)
        self.generations.setValue(1000)
        data.addWidget(label4)
        data.addWidget(self.generations)

        layout.addLayout(data)

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

        validationLayout = QHBoxLayout()
        label5 = QLabel("Average fitness: ")
        validationLayout.addWidget(label5)
        self.avg = QLineEdit()
        self.avg.setEnabled(False)
        validationLayout.addWidget(self.avg)
        validationButton = QPushButton("Validation")
        validationButton.clicked.connect(self.validate)
        validationLayout.addWidget(validationButton)
        layout.addLayout(validationLayout)

        self.graphWidget = pg.PlotWidget()
        layout.addWidget(self.graphWidget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def beginAlg(self):
        if self.controller is not None:
            self.controller.requestInterruption()
        self.controller = EASimulation(self.size.value(), self.populationSize.value(), self.mutationChance.value(),
                                       self.generations.value())
        self.controller.progress.connect(self.progress)
        self.controller.start()

    def progress(self, generation, fitness, solution):
        self.console.setText("Generation: " + str(generation) + "\nFitness: " + str(fitness) + "\n\n" + solution)

    def cancelAlg(self):
        self.controller.requestInterruption()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def validate(self):
        if self.validation is not None:
            self.validation.requestInterruption()
        self.validation = Validation()
        self.validation.done.connect(self.validationDone)
        self.validation.start()

    def validationDone(self, avg, std, graph):
        self.avg.setText(str(avg))
        self.graphWidget.plot([i for i in range(len(graph))], graph)

import pyqtgraph as pg
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget

from Lab3.simulations.pso.psoSimulation import PSOSimulation
from Lab3.simulations.pso.validation import Validation


class PSOWindow(QMainWindow):
    def __init__(self, parent=None):
        super(PSOWindow, self).__init__(parent)
        self.size: QSpinBox = None
        self.populationSize: QSpinBox = None
        self.inertia: QDoubleSpinBox = None
        self.social: QDoubleSpinBox = None
        self.cognitive: QDoubleSpinBox = None
        self.generations: QSpinBox = None
        self.controller: PSOSimulation = None
        self.validation: Validation = None
        self.console: QTextEdit = None
        self.avg: QLineEdit = None
        self.graphWidget: PlotWidget = None
        self.std: QLineEdit = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Particle Swarm Optimization')
        self.resize(800, 400)
        self.center()

        layout = QHBoxLayout()
        normalLayout = QVBoxLayout()
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

        label3 = QLabel("Inertia:")
        self.inertia = QDoubleSpinBox()
        self.inertia.setSingleStep(0.01)
        self.inertia.setValue(0.8)
        data.addWidget(label3)
        data.addWidget(self.inertia)

        label5 = QLabel("Social coefficient:")
        self.social = QDoubleSpinBox()
        self.social.setSingleStep(0.01)
        self.social.setValue(0.5)
        data.addWidget(label5)
        data.addWidget(self.social)

        label5 = QLabel("Cognitive coefficient:")
        self.cognitive = QDoubleSpinBox()
        self.cognitive.setSingleStep(3)
        self.cognitive.setValue(1)
        data.addWidget(label5)
        data.addWidget(self.cognitive)

        label4 = QLabel("Generations: ")
        self.generations = QSpinBox()
        self.generations.setMaximum(100000000)
        self.generations.setValue(1000)
        data.addWidget(label4)
        data.addWidget(self.generations)

        normalLayout.addLayout(data)

        buttonLayout = QHBoxLayout()
        button = QPushButton("Begin")
        button.clicked.connect(self.beginAlg)
        buttonLayout.addWidget(button)

        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.cancelAlg)
        buttonLayout.addWidget(cancelButton)

        normalLayout.addLayout(buttonLayout)

        self.console = QTextEdit()
        self.console.setEnabled(False)
        self.console.setFontPointSize(20)
        normalLayout.addWidget(self.console)

        bigValidationLayout = QVBoxLayout()
        validationLayout = QHBoxLayout()
        label5 = QLabel("Average fitness: ")
        validationLayout.addWidget(label5)
        self.avg = QLineEdit()
        self.avg.setEnabled(False)
        validationLayout.addWidget(self.avg)
        label6 = QLabel("Standard deviation of fitness: ")
        validationLayout.addWidget(label6)
        self.std = QLineEdit()
        self.std.setEnabled(False)
        validationLayout.addWidget(self.std)
        validationButton = QPushButton("Validation")
        validationButton.clicked.connect(self.validate)
        validationLayout.addWidget(validationButton)
        bigValidationLayout.addLayout(validationLayout)

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setXRange(0, 1000)
        self.graphWidget.setYRange(0, 1)
        self.graphWidget.setLabel('left', "<span style=\"color:purple;font-size:30px\">Fitness</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:purple;font-size:30px\">Generation</span>")
        self.graphWidget.setBackground('w')
        bigValidationLayout.addWidget(self.graphWidget)

        layout.addLayout(normalLayout)
        layout.addLayout(bigValidationLayout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def beginAlg(self):
        if self.controller is not None:
            self.controller.requestInterruption()
        self.controller = PSOSimulation(self.size.value(),
                                        self.populationSize.value(),
                                        self.inertia.value(),
                                        self.cognitive.value(),
                                        self.social.value(),
                                        self.generations.value()
                                        )
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
        self.avg.setText("{:.4f}".format(avg))
        self.std.setText("{:.4f}".format(std))
        self.graphWidget.setXRange(0, self.validation.generations)
        pen = pg.mkPen(color=(60, 0, 60), width=3)
        self.graphWidget.plot([i for i in range(len(graph))], graph, pen=pen)

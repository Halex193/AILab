import pyqtgraph as pg
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget

from Lab3.simulations.aco.acoSimulation import ACOSimulation
from Lab3.simulations.pso.psoSimulation import PSOSimulation
from Lab3.simulations.pso.validation import Validation

# 0, 0.5, 0.8, 0.2
class ACOWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ACOWindow, self).__init__(parent)
        self.size: QSpinBox = None
        self.populationSize: QSpinBox = None
        self.alpha: QDoubleSpinBox = None
        self.beta: QDoubleSpinBox = None
        self.q0: QDoubleSpinBox = None
        self.rho: QDoubleSpinBox = None
        self.generations: QSpinBox = None
        self.controller: PSOSimulation = None
        self.validation: Validation = None
        self.console: QTextEdit = None
        self.avg: QLineEdit = None
        self.graphWidget: PlotWidget = None
        self.std: QLineEdit = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ant Colony Optimization')
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

        label3 = QLabel("Alpha:")
        self.alpha = QDoubleSpinBox()
        self.alpha.setSingleStep(0.1)
        self.alpha.setValue(0.8)
        data.addWidget(label3)
        data.addWidget(self.alpha)

        label5 = QLabel("Beta:")
        self.beta = QDoubleSpinBox()
        self.beta.setSingleStep(0.1)
        self.beta.setValue(0.5)
        data.addWidget(label5)
        data.addWidget(self.beta)

        label6 = QLabel("Q0:")
        self.q0 = QDoubleSpinBox()
        self.q0.setSingleStep(0.1)
        self.q0.setValue(0.5)
        data.addWidget(label6)
        data.addWidget(self.q0)

        label7 = QLabel("Rho:")
        self.rho = QDoubleSpinBox()
        self.rho.setSingleStep(0.1)
        self.rho.setValue(0.8)
        data.addWidget(label7)
        data.addWidget(self.rho)

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
        self.controller = ACOSimulation(self.size.value(),
                                        self.populationSize.value(),
                                        self.alpha.value(),
                                        self.beta.value(),
                                        self.q0.value(),
                                        self.rho.value(),
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

""" INICIO SECCIÓN: Importación de librerias"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout

#### --> Importación de docs tipo LIBRERIAS
from LIBRERIAS import LIBRERIA_Class_RealTimePlot as graph1
from LIBRERIAS import LIBRERIA_Class_RealTimePlot_1 as graph2
from LIBRERIAS import LIBRERIA_Class_RealTimePlot_2 as graph3



class GraphsWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Real-Time Intensity Measurements")
        self.resize(1200, 900)

        layout = QVBoxLayout()

        self.g1 = graph1.RealTimePlot()
        self.g2 = graph2.RealTimePlot()
        self.g3 = graph3.RealTimePlot()

        layout.addWidget(self.g1)
        layout.addWidget(self.g2)
        layout.addWidget(self.g3)

        self.setLayout(layout)

""" INICIO SECCIÓN: Importación de librerias"""

from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
)


#### --> Importación de docs tipo LIBRERIAS

from LIBRERIAS import LIBRERIA_Class_RealTimePlot as graph1
from LIBRERIAS import LIBRERIA_Class_RealTimePlot_1 as graph2



""" Inicio sección: Definición Window REAL TIME PLOT class"""

class MenuWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Seleccionar visualización")

        layout = QVBoxLayout()

        self.btn_graph1 = QPushButton("Intensidad vs Tiempo ")
        self.btn_graph2 = QPushButton("Intensidad vs Longitud de onda")
        self.btn_both = QPushButton("Visualizar ambos gráficos")

        layout.addWidget(self.btn_graph1)
        layout.addWidget(self.btn_graph2)
        layout.addWidget(self.btn_both)

        self.setLayout(layout)

        self.btn_graph1.clicked.connect(self.open_graph1)
        self.btn_graph2.clicked.connect(self.open_graph2)
        self.btn_both.clicked.connect(self.open_both)
    
    def open_graph1(self):

        self.g1 = graph1.RealTimePlot()

        self.g1.show()
    

    def open_graph2(self):

        self.g2 = graph2.RealTimePlot()

        self.g2.show()

    def open_both(self):

        self.g1 = graph1.RealTimePlot()
        self.g2 = graph2.RealTimePlot()

        self.g1.show()
        self.g2.show()

        

""" INICIO SECCIÓN: Importación de librerias"""

from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
)


#### --> Importación de docs tipo LIBRERIAS

from LIBRERIAS import LIBRERIA_ComunicacionSerial as comSerial
from LIBRERIAS import LIBRERIA_Class_RealTimePlot as graph1
from LIBRERIAS import LIBRERIA_Class_RealTimePlot_1 as graph2



""" Inicio sección: Definición Window REAL TIME PLOT class"""

class MenuWindow(QWidget):

    def __init__(self):

        super().__init__()

        # Window configuration
        self.setWindowTitle("Seleccionar visualización")

        # ====================================================
        # LAYOUT
        # ====================================================
        layout = QVBoxLayout()


        # ====================================================
        # CONFIGURATION BUTTON
        # ====================================================
        self.btn_graph1 = QPushButton("Intensidad vs Tiempo ")
        self.btn_graph2 = QPushButton("Intensidad vs Longitud de onda")
        self.btn_stop = QPushButton("STOP")

        layout.addWidget(self.btn_graph1)
        layout.addWidget(self.btn_graph2)
        layout.addWidget(self.btn_stop)

        self.setLayout(layout)

        # Connect button to function
        self.btn_graph1.clicked.connect(self.open_graph1)
        self.btn_graph2.clicked.connect(self.open_graph2)
        self.btn_stop.clicked.connect(self.stop_measurement)
    
    
    # ========================================================
    # START GRAPHIC 1 FUNCTION
    # ========================================================
    def open_graph1(self):

        self.g1 = graph1.RealTimePlot()

        self.g1.show()
    

    # ========================================================
    # START GRAPHIC 2 FUNCTION
    # ========================================================
    def open_graph2(self):

        self.g2 = graph2.RealTimePlot()

        self.g2.show()

    
    # ========================================================
    # STOP FUNCTION
    # ========================================================
    def stop_measurement(self):

        print("Stopping measurement...")

        #comSerial.ser.write(b'D')

        
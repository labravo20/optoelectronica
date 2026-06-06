
""" INICIO SECCIÓN: Importación de librerias"""

from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
)


#### --> Importación de docs tipo LIBRERIAS

from LIBRERIAS import LIBRERIA_ComunicacionSerial as comSerial
from LIBRERIAS import LIBRERIA_Class_GraphsWindow as graphWindow
from LIBRERIAS import LIBRERIA_Class_Clibracion as calibration



""" Inicio sección: Definición Window REAL TIME PLOT class"""

class MenuWindow(QWidget):

    def __init__(self):

        super().__init__()
                # Window configuration

        

        # Window configuration
        self.setWindowTitle("Menú Principal")
        self.setGeometry(300, 300, 500, 300)

        # ====================================================
        # LAYOUT
        # ====================================================
        layout = QVBoxLayout()


        # ====================================================
        # CONFIGURATION BUTTON
        # ====================================================
        self.btn_graph1 = QPushButton("Grasficar Intensidad ")
        self.btn_graph2 = QPushButton("Calibración")
        self.btn_stop = QPushButton("STOP")

        layout.addWidget(self.btn_graph1)
        layout.addWidget(self.btn_graph2)
        layout.addWidget(self.btn_stop)

        self.setLayout(layout)

        # Connect button to function
        self.btn_graph1.clicked.connect(self.open_graphs)
        self.btn_graph2.clicked.connect(self.open_calibration)
        self.btn_stop.clicked.connect(self.stop_measurement)
    
    
    # ========================================================
    # START GRAPHIC 1 FUNCTION
    # ========================================================
    def open_graphs(self):

        self.graph_window = graphWindow.GraphsWindow()
        self.graph_window.show()
    

    # ========================================================
    # START GRAPHIC 2 FUNCTION
    # ========================================================
    def open_calibration(self):

          self.calibration_window = calibration.CalibrationWindow()
          self.calibration_window.show()

    
    # ========================================================
    # STOP FUNCTION
    # ========================================================
    def stop_measurement(self):

        print("Stopping measurement...")

        #comSerial.ser.write(b'D')

        
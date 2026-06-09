""" INICIO SECCIÓN: Importación de librerias"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer


#### --> Importación de docs tipo LIBRERIAS
from LIBRERIAS import LIBRERIA_ComunicacionSerial as comSerial

from LIBRERIAS import LIBRERIA_Class_RealTimePlot as graph1
from LIBRERIAS import LIBRERIA_Class_RealTimePlot_1 as graph2
from LIBRERIAS import LIBRERIA_Class_RealTimePlot_2 as graph3



class GraphsWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Real-Time Intensity Measurements")
        self.resize(1200, 900)

        layout = QVBoxLayout()

        #self.g1 = graph1.RealTimePlot()
        self.g2 = graph2.RealTimePlot()
        self.g3 = graph3.RealTimePlot()

        # CONEXION CON PUERTO SERIAL PARA ADQUISICION DE DATOS MCU
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_serial)
        self.timer.start(50)

        #layout.addWidget(self.g1)
        layout.addWidget(self.g2)
        layout.addWidget(self.g3)

        self.setLayout(layout)

    def read_serial(self):

        if comSerial.ser.in_waiting:

            line = comSerial.ser.readline().decode().strip()

            try:
                intensidad = float(line)

                #self.g1.update_plot(intensidad)

                self.g2.update_plot(intensidad)

                self.g3.update_plot(intensidad)


            except:
                
                pass


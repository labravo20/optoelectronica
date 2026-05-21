
# Generando 'print' identificador del entorno de programación
print("Inicializando entorno de programación --> Interfaz Práctica 01 OPTOELECTRÓNICA")



""" Importación de librerias necesarias """
import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
import serial




""" INICIO SECCIÓN CONEXIÓN CON PUERTO SERIAL  """

ser = serial.Serial(
    port='COM3',
    baudrate=115200
)
 




""" INICIO SECCIÓN ASOCIADA A ESTRUCTURA DE INTERFAZ  """

class RealTimePlot(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Real-Time Data Visualization")
        self.setGeometry(100, 100, 800, 500)

        # Create plot widget
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # Graph settings
        self.graphWidget.setBackground('w')
        self.graphWidget.setTitle("Sensor Data")
        self.graphWidget.setLabel('left', 'Value')
        self.graphWidget.setLabel('bottom', 'Samples')

        # Data containers
        self.x = list(range(100))
        self.y = [0] * 100

        # Create curve
        self.data_line = self.graphWidget.plot(
            self.x,
            self.y,
            pen=pg.mkPen(width=2)
        )

        # Timer for updates
        self.timer = QTimer()
        self.timer.setInterval(50)  # milliseconds
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):

        # =====================================
        # RANDOM SOMULATOR DATA
        # =====================================

        # new_value = np.random.normal()

        # # Update buffer
        # self.y = self.y[1:]
        # self.y.append(new_value)

        # # Update graph
        # self.data_line.setData(self.x, self.y)
          
        # =====================================
        # MICROCONTROLLER DATA
        # =====================================
        if ser.in_waiting:

            line = ser.readline().decode().strip()

            try:
                new_value = float(line)

                self.y = self.y[1:]
                self.y.append(new_value)

                self.data_line.setData(self.x, self.y)

            except:
                pass

app = QApplication(sys.argv)
window = RealTimePlot()
window.show()
sys.exit(app.exec_())


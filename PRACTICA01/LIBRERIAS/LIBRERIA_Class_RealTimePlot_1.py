""" GRAPHIC --> Intensidad vs Longitud de onda"""


""" INICIO SECCIÓN: Importación de librerias"""

#### --> Importación de librerias necesarias

import numpy as np

# Libreria importada para 'PyQt5 components for the graphical interface'
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

# Libreria importada para 'QTimer allows repetitive execution every X milliseconds'
from PyQt5.QtCore import QTimer

# Libreria importada para 'Fast real-time plotting library'
import pyqtgraph as pg



#### --> Importación de docs tipo LIBRERIAS
from LIBRERIAS import LIBRERIA_ComunicacionSerial as comSerial
from LIBRERIAS import LIBRERIA_ProcesamientoData as procesamiento



""" Inicio sección: Definición Window REAL TIME PLOT class"""

# NOTA: QMainWindow is a PyQt5 window template --> Diseño de clase a partir de este 'template'
class RealTimePlot(QWidget):

    "Definiendo funcion 'init' --> Se ejecuta automáticamente cuando la ventana de la interfaz es creada"
    def __init__(self):

        super().__init__() # Inicialización de 'parent class'
        layout = QVBoxLayout(self)

        self.setWindowTitle("Real-Time Data Visualization Espectral Information") # --> Definición de TITULO de la ventana
        self.setGeometry(100, 100, 800, 500) # Window size and position
                                             # (x position, y position, width, height)


        # =====================================
        # CREATE GRAPH WIDGET
        # =====================================
        self.graphWidget = pg.PlotWidget()  # Create a plotting area
        layout.addWidget(self.graphWidget)
        
        #self.setCentralWidget(self.graphWidget) # Put graph inside the main window


        # =====================================
        # GRAPH APPEARANCE CONFIGURATION
        # =====================================
        self.graphWidget.setBackground('w') # White background
        self.graphWidget.setTitle("Sensor Data Espectral Information") # Graph title
        
        
        # Axis labels --- MCU:
        self.graphWidget.setLabel(
            'left',
            'Intensidad (lux)'
        )

        self.graphWidget.setLabel(
            'bottom',
            'Longitud de Onda (nm)'
        )




        # =====================================
        # # DATA STORAGE --- PRUEBA CON DATA RANDOM
        # =====================================       
        
        # # X-axis values:
        # # --> Creates numbers from 0 to 99
        # self.x = list(range(100))

        # # Y-axis values:
        # # --> Creates numbers from 0 to 99
        # self.y = [0] * 100



        # =====================================
        # DATA STORAGE ---- IMPLEMENTANDO MCU
        # =====================================

        # Number of points displayed in the graph
        self.num_points = 100

        # Time axis (seconds)
        self.x = [0] * self.num_points

        # Signal values
        self.y = [0] * self.num_points



        # =====================================
        # # CREATE GRAPH LINE
        # =====================================               

        # Create curve --> Plot initial data
        self.data_line = self.graphWidget.plot(

            # X values
            self.x,
            
            # Y values
            self.y,
            
            # Pen controls line appearance
            pen=pg.mkPen(width=2)
        )


        # =====================================
        # # TIMER CONFIGURATION
        # =====================================               

        # QTimer repeatedly calls a function
        self.timer = QTimer()

        # Execute every 50 milliseconds
        self.timer.setInterval(50)  

        # Connect timer to update function
        # Every 50 ms -> update_plot() runs
        self.timer.timeout.connect(self.update_plot)

        # Start timer
        self.timer.start()



    "Definiendo funcion 'update' --> Se ejecuta para la actualización constante del gráfico de la interfaz"
    def update_plot(self):

        # =====================================
        # RANDOM SOMULATOR DATA (!!!!) --> Desactivar cuando mcu está conectado
        # =====================================

        # new_value = (np.random.normal())**2 # Generación artificial de data

        # # Update buffer
        # self.y = self.y[1:]
        # self.y.append(new_value)

        # # Update graph
        # self.data_line.setData(self.x, self.y)
          

        # =====================================
        # MICROCONTROLLER DATA 
        # =====================================

        # --> CHECK IF THERE IS DATA AVAILABLE <--
        
        # In_waiting tells how many bytes are waiting in buffer
        if comSerial.ser.in_waiting:

            # =================================================
            # READ ONE LINE FROM SERIAL PORT
            # =================================================

            # readline() reads until '\n'
            # decode() converts bytes -> text
            # strip() removes spaces/newlines

            line = comSerial.ser.readline().decode().strip()
                    

            # =================================================
            # TRY TO CONVERT DATA TO FLOAT
            # =================================================

            try:

                # Convert incoming text into number
                intensidad = float(line)
                
                # Cada lectura recibida equivale a un paso
                self.numero_pasos += 1

               # ==========================
               # UPDATE X BUFFER (PASOS)
               # ==========================

                # Convirtiendo el número de pasos en desplazamiento efectivo
                desplazamiento = procesamiento.pasos_a_desplazamiento(self.numero_pasos)


                # Convirtiendo desplazamiento efectivo en coordenada angular
                senAngulo,angulo = procesamiento.Angulo(desplazamiento)


                # Convirtiendo coordenada angular en Longitud de Onda
                longitudOnda = procesamiento.longitud_Onda(senAngulo)


                self.x = self.x[1:]
                self.x.append(longitudOnda)

                # =============================================
                # UPDATE DATA BUFFER
                # =============================================
                  
                  # Remove oldest value
                self.y = self.y[1:]
                  
                  # Add newest value
                self.y.append(intensidad)

                # =============================================
                # UPDATE GRAPH VISUALLY
                # =============================================
                
                  # Replace old graph data with new data
                self.data_line.setData(self.x, self.y)

        # If conversion fails, ignore the error
            except:
                pass



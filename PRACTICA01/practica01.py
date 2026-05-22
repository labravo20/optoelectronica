
# Generando 'print' identificador del entorno de programación
print("Inicializando entorno de programación --> Interfaz Práctica 01 OPTOELECTRÓNICA")



""" Importación de librerias necesarias """
import numpy as np
import matplotlib.pyplot as plt
import sys
import serial

# Libreria importada para 'PyQt5 components for the graphical interface'
from PyQt5.QtWidgets import QApplication, QMainWindow

# Libreria importada para 'QTimer allows repetitive execution every X milliseconds'
from PyQt5.QtCore import QTimer

# Libreria importada para 'Fast real-time plotting library'
import pyqtgraph as pg






""" INICIO SECCIÓN CONEXIÓN CON PUERTO SERIAL  """

# Creando Conexión Serial
# --> Inicializa comunicación con el microcontrolador (mcu) <--
# ser = serial.Serial(
    
#     ### IMPORTANTE VERIFICAR PUERTO ASOCIADO AL mcu EN USO 
#     port='COM3', 
    
#     # Velocidad de comunicación --> Valor estándar establecido en el mcu
#     baudrate=115200
# )
 


""" INICIO SECCIÓN ASOCIADA DEFINICIÓN DE FUNCIONES PARA PROCESAMIENTO DATA SENSOR  """



# NOTA: OUTPUT DEL SENSOR ESTÁ ASOCIADO A MEDIDAS EN 'lux'
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX





""" INICIO SECCIÓN ASOCIADA A ESTRUCTURA DE INTERFAZ  """


### --> MAIN WINDOW CLASS <-- ###


# NOTA: QMainWindow is a PyQt5 window template --> Diseño de clase a partir de este 'template'
class RealTimePlot(QMainWindow):

    "Definiendo funcion 'init' --> Se ejecuta automáticamente cuando la ventana de la interfaz es creada"
    def __init__(self):

        super().__init__() # Inicialización de 'parent class'

        self.setWindowTitle("Real-Time Data Visualization") # --> Definición de TITULO de la ventana
        self.setGeometry(100, 100, 800, 500) # Window size and position
                                             # (x position, y position, width, height)


        # =====================================
        # CREATE GRAPH WIDGET
        # =====================================
        self.graphWidget = pg.PlotWidget()  # Create a plotting area
        self.setCentralWidget(self.graphWidget) # Put graph inside the main window


        # =====================================
        # GRAPH APPEARANCE CONFIGURATION
        # =====================================
        self.graphWidget.setBackground('w') # White background
        self.graphWidget.setTitle("Sensor Data") # Graph title

        # Axis labels:
        self.graphWidget.setLabel('left', 'Value')
        self.graphWidget.setLabel('bottom', 'Samples')



        # =====================================
        # # DATA STORAGE
        # =====================================       
        
        # X-axis values:
        # --> Creates numbers from 0 to 99
        self.x = list(range(100))

        # Y-axis values:
        # --> Creates numbers from 0 to 99
        self.y = [0] * 100



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

        new_value = np.random.normal() # Generación artificial de data

        # Update buffer
        self.y = self.y[1:]
        self.y.append(new_value)

        # Update graph
        self.data_line.setData(self.x, self.y)
          

        # =====================================
        # MICROCONTROLLER DATA
        # =====================================

        # --> CHECK IF THERE IS DATA AVAILABLE <--
        
        # In_waiting tells how many bytes are waiting in buffer
        # if ser.in_waiting:

            # =================================================
            # READ ONE LINE FROM SERIAL PORT
            # =================================================

            # readline() reads until '\n'
            # decode() converts bytes -> text
            # strip() removes spaces/newlines

        #     line = ser.readline().decode().strip()

            # =================================================
            # TRY TO CONVERT DATA TO FLOAT
            # =================================================

        #     try:

                 # Convert incoming text into number
        #         new_value = float(line)


                # =============================================
                # UPDATE DATA BUFFER
                # =============================================
                  
                  # Remove oldest value
        #         self.y = self.y[1:]
                  
                  # Add newest value
        #         self.y.append(new_value)

                # =============================================
                # UPDATE GRAPH VISUALLY
                # =============================================
                
                  # Replace old graph data with new data
        #         self.data_line.setData(self.x, self.y)

        # If conversion fails, ignore the error
        #     except:
        #         pass





# ============================================================
# CREATE APPLICATION
# ============================================================

# QApplication controls the entire GUI application
app = QApplication(sys.argv)



# ============================================================
# CREATE WINDOW OBJECT
# ============================================================

window = RealTimePlot()



# ============================================================
# SHOW WINDOW
# ============================================================

window.show()



# ============================================================
# START APPLICATION LOOP
# ============================================================

# Keeps the window alive and responsive
sys.exit(app.exec_())


""" GRAPHIC --> FACTOR DE CORRECCIÓN; Intensidad vs Longitud de onda"""


""" INICIO SECCIÓN: Importación de librerias"""

#### --> Importación de librerias necesarias

import numpy as np

# Libreria importada para 'PyQt5 components for the graphical interface'
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout


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

        self.setWindowTitle("Real-Time Data Visualization Espectral Correction") # --> Definición de TITULO de la ventana
        self.setGeometry(100, 100, 800, 500) # Window size and position
                                             # (x position, y position, width, height)


        # Contador de pasos
        self.numero_pasos = 500

        # Contador de número de barridos para PRECISIÓN
        self.numero_barridos_precision = 0

        self.longitudes_medidasIntensidadCorrection = []
        self.intensidades_medidasIntensidadCorrection = []
        

        # ===========================================================================================================
        # VARIABLES PARA ESTUDIO DE PRECISIÓN
        # =====================================

        # Almacena todos los barridos realizados
        self.espectros_precision = []

        # Barrido actualmente en adquisición
        self.longitudes_barrido_actual = []
        self.intensidades_barrido_actual = []



        # ================================================================================================================ 
        # CREATE GRAPH WIDGET
        # =====================================
        self.graphWidget = pg.PlotWidget()  # Create a plotting area
        layout.addWidget(self.graphWidget)
        
        #self.setCentralWidget(self.graphWidget) # Put graph inside the main window


        # =====================================
        # GRAPH APPEARANCE CONFIGURATION
        # =====================================
        self.graphWidget.setBackground('w') # White background
        self.graphWidget.setTitle("Sensor Data Espectral Correction") # Graph title

        
        # Axis labels --- MCU:
        self.graphWidget.setLabel(
            'left',
            'Intensidad '
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
        self.num_points = 1500

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



    "Definiendo funcion guardado DATA barridos"
    # def guardar_barrido_precision(self):

    #     #ANEXANDO DATA EN DICCIONARIO GLOBAL
    #     self.espectros_precision.append({

    #         "longitudes":
    #         self.longitudes_barrido_actual.copy(),

    #         "intensidades":
    #         self.intensidades_barrido_actual.copy()
    #     })


    #     self.numero_barridos_precision += 1 #AUMENTANDO CONTADOR DE NÚMERO DE BARRIDOS

        
    #     #Print de verificación cantidad de barridos realizados
    #     print(
    #         f"Barrido almacenado. Total = "
    #         f"{len(self.espectros_precision)}"
    #     )

        
    #     #Limpiando listas de almacenamiento por barrido
    #     self.longitudes_barrido_actual.clear()
    #     self.intensidades_barrido_actual.clear()


    #     # AL FINALIZAR BARRIDOS, GUARDA DATA RECOLECTADA EN ATRIBUTOS DE LA CLASE
    #     if self.numero_barridos_precision == 3:

    #         (
    #             self.longitudes_precision,
    #             self.media_precision,
    #             self.desviacion_precision
    #         ) = procesamiento.procesar_precision(
    #             self.espectros_precision
    #         ) # --> Llamando función para procesamiento de data precision

    #         print("Procesamiento de precisión finalizado")

    

    "Definiendo funcion 'update' --> Se ejecuta para la actualización constante del gráfico de la interfaz"
    def update_plot(self,intensidad):
                
                

        # =====================================
        # RANDOM SOMULATOR DATA (!!!!) --> Desactivar cuando mcu está conectado
        # =====================================

        # new_value = (np.random.normal())**3 # Generación artificial de data

        # # Update buffer
        # self.y = self.y[1:]
        # self.y.append(new_value)

        # # Update graph
        # self.data_line.setData(self.x, self.y)

        # self.longitudes_medidasIntensidadCorrection = self.x.copy()
        # self.intensidades_medidasIntensidadCorrection = self.y.copy()

          

        # =====================================
        # MICROCONTROLLER DATA 
        # =====================================

        # --> CHECK IF THERE IS DATA AVAILABLE <--
        
        # In_waiting tells how many bytes are waiting in buffer
        # if comSerial.ser.in_waiting:

        #     # =================================================
        #     # READ ONE LINE FROM SERIAL PORT
        #     # =================================================

        #     # readline() reads until '\n'
        #     # decode() converts bytes -> text
        #     # strip() removes spaces/newlines

        #     line = comSerial.ser.readline().decode().strip()


        #     #VERIFICANDO FINALIZACIÓN DEL CICLO DE MEDICIÓN (utilidad para HISTÉRESIS y PRECISIÓN)
        #     if line == "F":
                
        #         self.guardar_barrido_precision()
        #         return
                    

            # =================================================
            # TRY TO CONVERT DATA TO FLOAT
            # =================================================

            # try:


                #  # Convert incoming text into number
                # intensidad = float(line)
                
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
                  
                # Aplicando factor de corrección asociado a sensor

                
                intensidad = procesamiento.corregir_espectroInclinacionAngular(intensidad,(angulo+0.7))
                
                intensidadReal = procesamiento.corregir_espectro(intensidad,longitudOnda)
               


                # Remove oldest value
                self.y = self.y[1:]
               
                  
                  # Add newest value
                self.y.append(intensidadReal)

                # Normalización
                max_intensidad = max(self.y)
              

                # ==================================================================================================
                # ALMACENAMIENTO PARA PRECISIÓN
                # =====================================

                self.longitudes_barrido_actual.append(
                    longitudOnda
                )

                self.intensidades_barrido_actual.append(
                    intensidadReal
                )
               
                # =============================================
                # UPDATE GRAPH VISUALLY NORMALIZADA
                # =============================================
                if max_intensidad > 0:
                    y_norm = [valor/max_intensidad for valor in self.y]
                else:
                    y_norm = self.y

                self.data_line.setData(self.x, y_norm)
                
                # ======================================================================================================
                # UPDATE GRAPH VISUALLY
                # =============================================
                
                  # Replace old graph data with new data
                #self.data_line.setData(self.x, self.y)
              
        
                
                # ALMACENANDO DATA PARA ERROR RELATIVO
                self.longitudes_medidasIntensidadCorrection = self.x.copy()
                self.intensidades_medidasIntensidadCorrection = self.y.copy()


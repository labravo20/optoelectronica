""" INICIO SECCIÓN: Importación de librerias"""

from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)



#### --> Importación de docs tipo LIBRERIAS
from LIBRERIAS import LIBRERIA_ProcesamientoData as procesamiento
from LIBRERIAS import LIBRERIA_Class_GraphPrecision as precisionGraph

# Import serial communication
from LIBRERIAS import LIBRERIA_ComunicacionSerial as comSerial




# ====================================================
# CALIBRATION MENU
# ====================================================
class CalibrationWindow(QWidget):

    def __init__(self, graph_window):
        super().__init__()

        self.graph_window = graph_window

        
        self.setWindowTitle("Menú de Calibración")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.btn_cal1 = QPushButton("Resolución")
        self.btn_cal2 = QPushButton("Error Relativo")
        self.btn_cal3 = QPushButton("Precisión")
        self.btn_cal4 = QPushButton("Histéresis")
        self.btn_cal6 = QPushButton("Incertidumbre")

        layout.addWidget(self.btn_cal1)
        layout.addWidget(self.btn_cal2)
        layout.addWidget(self.btn_cal3)
        layout.addWidget(self.btn_cal4)
        layout.addWidget(self.btn_cal6)

        self.setLayout(layout)

        # Conectar funciones
        self.btn_cal1.clicked.connect(self.resolucion)
        self.btn_cal2.clicked.connect(self.error_Relativo)
        self.btn_cal3.clicked.connect(self.precision)
        self.btn_cal4.clicked.connect(self.histeresis)
        self.btn_cal6.clicked.connect(self.incertidumbre)

    def resolucion(self):
        
        # Ejemplo de cálculo
        resolucion = procesamiento.resolucion()

        # Mostrar mensaje
        QMessageBox.information(
            self,
            "Resolution Information",
            f"<b>Resolución:</b> {resolucion:.3f} nm"
        )

    def error_Relativo(self):

        x_med = self.graph_window.g3.longitudes_medidasIntensidadCorrection
        y_med = self.graph_window.g3.intensidades_medidasIntensidadCorrection

        errorRelativoPromedio = procesamiento.error_relativo(x_med,y_med)
        
        # Mostrar mensaje
        QMessageBox.information(
            self,
            "Resolution Information",
            f"<b>Resolución:</b> {errorRelativoPromedio:.3f} %"
        )

    def precision(self):


        # ====================================================
        # SEND CHARACTER TO MICROCONTROLLER
        # ====================================================

        comSerial.ser.write(b'P')


        try:

            longitudes = (
                self.graph_window.g3.longitudes_precision
            )

            media = (
                self.graph_window.g3.media_precision
            )

            desviacion = (
                self.graph_window.g3.desviacion_precision
            )

            self.precisionWindow = (
                precisionGraph.PrecisionPlot(
                    longitudes,
                    media,
                    desviacion
                )
            )

            self.precisionWindow.show()
        
        except AttributeError:

            QMessageBox.warning(
                self,
                "Precisión",
                "Aún no existen 3 barridos completos."
            )

    
    def histeresis(self):

        print("Sending histeresis command to MCU...")


        # ====================================================
        # SEND CHARACTER TO MICROCONTROLLER
        # ====================================================

        #comSerial.ser.write(b'H')


    def incertidumbre(self):
        print("Ejecutando Incertidumbre")



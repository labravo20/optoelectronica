""" INICIO SECCIÓN: Importación de librerias"""

from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)



#### --> Importación de docs tipo LIBRERIAS
from LIBRERIAS import LIBRERIA_ProcesamientoData as procesamiento

# Import serial communication
from LIBRERIAS import LIBRERIA_ComunicacionSerial as comSerial




# ====================================================
# CALIBRATION MENU
# ====================================================
class CalibrationWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menú de Calibración")
        self.resize(300, 200)

        layout = QVBoxLayout()

        self.btn_cal1 = QPushButton("Resolución")
        self.btn_cal2 = QPushButton("Error Relativo")
        self.btn_cal3 = QPushButton("Precisión")
        self.btn_cal4 = QPushButton("Histéresis")
        self.btn_cal5 = QPushButton("Desviación Estándar")

        layout.addWidget(self.btn_cal1)
        layout.addWidget(self.btn_cal2)
        layout.addWidget(self.btn_cal3)
        layout.addWidget(self.btn_cal4)
        layout.addWidget(self.btn_cal5)

        self.setLayout(layout)

        # Conectar funciones
        self.btn_cal1.clicked.connect(self.resolucion)
        self.btn_cal2.clicked.connect(self.error_Relativo)
        self.btn_cal3.clicked.connect(self.precision)
        self.btn_cal4.clicked.connect(self.histeresis)
        self.btn_cal5.clicked.connect(self.standarDeviation)

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
        print("Ejecutando Error relativo")

    def precision(self):

        print("Sending precision command to MCU...")


        # ====================================================
        # SEND CHARACTER TO MICROCONTROLLER
        # ====================================================

        #comSerial.ser.write(b'P')
    
    def histeresis(self):

        print("Sending histeresis command to MCU...")


        # ====================================================
        # SEND CHARACTER TO MICROCONTROLLER
        # ====================================================

        #comSerial.ser.write(b'H')

    def standarDeviation(self):
        print("Ejecutando Desviación Estándar")



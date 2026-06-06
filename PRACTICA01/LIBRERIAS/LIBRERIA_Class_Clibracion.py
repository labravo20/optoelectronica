""" INICIO SECCIÓN: Importación de librerias"""

from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)



#### --> Importación de docs tipo LIBRERIAS
from LIBRERIAS import LIBRERIA_ProcesamientoData as procesamiento



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
        self.btn_cal2 = QPushButton("Calibración 2")
        self.btn_cal3 = QPushButton("Calibración 3")

        layout.addWidget(self.btn_cal1)
        layout.addWidget(self.btn_cal2)
        layout.addWidget(self.btn_cal3)

        self.setLayout(layout)

        # Conectar funciones
        self.btn_cal1.clicked.connect(self.resolucion)
        self.btn_cal2.clicked.connect(self.calibration2)
        self.btn_cal3.clicked.connect(self.calibration3)

    def resolucion(self):
        
        # Ejemplo de cálculo
        resolucion = procesamiento.resolucion()

        # Mostrar mensaje
        QMessageBox.information(
            self,
            "Resolution Information",
            f"<b>Resolution:</b> {resolucion:.3f} nm"
        )

    def calibration2(self):
        print("Ejecutando calibración 2")

    def calibration3(self):
        print("Ejecutando calibración 3")


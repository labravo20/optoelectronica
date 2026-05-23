
# Generando 'print' identificador del entorno de programación
print("Inicializando entorno de programación --> Interfaz Práctica 01 OPTOELECTRÓNICA")




""" INICIO SECCIÓN: Importación de librerias"""

# Importación de librerias necesarias
import matplotlib.pyplot as plt
import sys

# Libreria importada para 'PyQt5 components for the graphical interface'
from PyQt5.QtWidgets import QApplication


# Importación de docs tipo LIBRERIAS
from LIBRERIAS import LIBRERIA_Class_RealTimePlot as classRealTime




""" INICIO SECCIÓN ASOCIADA DEFINICIÓN DE FUNCIONES PARA PROCESAMIENTO DATA SENSOR  """

# NOTA: OUTPUT DEL SENSOR ESTÁ ASOCIADO A MEDIDAS EN 'lux'
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX








""" INICIO SECCIÓN EJECUCIÓN INTERFAZ """

# ============================================================
# CREATE APPLICATION
# ============================================================

# QApplication controls the entire GUI application
app = QApplication(sys.argv)



# ============================================================
# CREATE WINDOW OBJECT
# ============================================================

window = classRealTime.RealTimePlot()



# ============================================================
# SHOW WINDOW
# ============================================================

window.show()



# ============================================================
# START APPLICATION LOOP
# ============================================================

# Keeps the window alive and responsive
sys.exit(app.exec_())


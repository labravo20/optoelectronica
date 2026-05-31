
""" INICIO SECCIÓN: Importación de librerias"""

#### --> Importación de librerias necesarias
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)

from PyQt5.QtCore import Qt


#### --> Importación de docs tipo LIBRERIAS

# Import graph window
from LIBRERIAS import LIBRERIA_Class_RealTimePlot as classPlot

# Import serial communication
from LIBRERIAS import LIBRERIA_ComunicacionSerial as comSerial





""" Inicio sección: Definición Window REAL TIME PLOT class"""

class StartWindow(QWidget):

    def __init__(self):

        super().__init__()

        # Window configuration
        self.setWindowTitle("OPTOELECTRONICS INTERFACE")
        self.setGeometry(300, 300, 500, 300)

        # ====================================================
        # LAYOUT
        # ====================================================

        layout = QVBoxLayout()


        # ====================================================
        # TITLE
        # ====================================================

        title = QLabel("INTERFAZ ESPECTRÓMETRO OPTO-ELECTRÓNICA")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet(
            "font-size: 24px;"
            "font-weight: bold;"
        )

        layout.addWidget(title)


        # ====================================================
        # DESCRIPTION
        # ====================================================

        description = QLabel(

            "Sistema de vizualización en tiempo real.\n"
        )

        description.setAlignment(Qt.AlignCenter)

        description.setStyleSheet(
            "font-size: 14px;"
        )

        layout.addWidget(description)


        # ====================================================
        # START BUTTON
        # ====================================================

        self.start_button = QPushButton("START")

        self.start_button.setFixedHeight(50)

        # Connect button to function
        self.start_button.clicked.connect(self.start_measurement)

        layout.addWidget(self.start_button)


        # Apply layout
        self.setLayout(layout)


    # ========================================================
    # START MEASUREMENT FUNCTION
    # ========================================================

    def start_measurement(self):

        print("Sending start command to MCU...")


        # ====================================================
        # SEND CHARACTER TO MICROCONTROLLER
        # ====================================================

        #comSerial.ser.write(b'S')


        # ====================================================
        # OPEN GRAPH WINDOW
        # ====================================================

        self.graph_window = classPlot.RealTimePlot()

        self.graph_window.show()


        # ====================================================
        # CLOSE INITIAL WINDOW
        # ====================================================

        self.close()

       
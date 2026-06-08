""" INICIO SECCIÓN: Importación de librerias"""

import numpy as np

from PyQt5.QtWidgets import QWidget, QVBoxLayout

import pyqtgraph as pg



class PrecisionPlot(QWidget):

    def __init__(
        self,
        longitudes,
        media,
        desviacion
    ):

        super().__init__()

        self.setWindowTitle(
            "Precision Analysis"
        )

        self.resize(1000,600)

        layout = QVBoxLayout(self)


        # ==============================
        # SECTION FOR GRAPHIC DEFINITION
        # ==============================
        
        self.graphWidget = pg.PlotWidget()

        layout.addWidget(
            self.graphWidget
        )

        self.graphWidget.setBackground('w')

        self.graphWidget.setTitle(
            "Precision Analysis"
        )

        self.graphWidget.setLabel(
            'left',
            'Intensity'
        )

        self.graphWidget.setLabel(
            'bottom',
            'Wavelength (nm)'
        )

        
        # ==============================
        # GRÁFICO CON CURVA PROMEDIO 
        # ==============================
        self.graphWidget.plot(
            longitudes,
            media,
            pen=pg.mkPen(width=2)
        )

        
        errores = pg.ErrorBarItem(

            x=np.array(longitudes),

            y=np.array(media),

            top=np.array(desviacion),

            bottom=np.array(desviacion),

            beam=0.5
        )

        self.graphWidget.addItem(
            errores
        )





""" Importación de librerias """

import numpy as np




""" INICIO SECCIÓN ASOCIADA DEFINICIÓN DE FUNCIONES PARA PROCESAMIENTO DATA SENSOR  """

def pasos_a_desplazamiento(numero_pasos,desplazamiento_paso):

    """
    Convierte número de pasos del motor
    a desplazamiento físico.

    """

    desplazamiento = numero_pasos * desplazamiento_paso

    return desplazamiento



def longitud_Onda(desplazamiento,distancia_RedToSensor,ancho_Rejilla):

    """
    Convierte número de pasos del motor
    a desplazamiento físico.

    """

    hipotenusa = np.sqrt((distancia_RedToSensor**2) + (desplazamiento)**2)

    senAngulo =  desplazamiento/hipotenusa

    longitudOnda = ancho_Rejilla*senAngulo

    return longitudOnda


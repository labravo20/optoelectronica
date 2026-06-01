
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




def Angulo(desplazamiento,distancia_RedToSensor):

    """
    Convierte desplazamiento del motor
    en el ángulo de difracción asociado.

    """

    hipotenusa = np.sqrt((distancia_RedToSensor**2) + (desplazamiento)**2)

    senAngulo =  desplazamiento/hipotenusa

    Angulo = np.arcsin(senAngulo) # OUTPUT por defecto en RADIANES

    return senAngulo, Angulo





def longitud_Onda(senAngulo,ancho_Rejilla):

    """
    Convierte ángulo de difracción 
    a longitud de onda respectiva.

    """


    longitudOnda = ancho_Rejilla*senAngulo

    return longitudOnda


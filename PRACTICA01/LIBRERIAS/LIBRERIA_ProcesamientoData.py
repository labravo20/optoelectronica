
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



def Angulo_Paso_Motor(numero_pasos,grados_paso):

    """
    Convierte pasos del motor (caracterizados por ángulo específico)
    en el ángulo de difracción asociado.

    """
    angulo =  numero_pasos* grados_paso 

    senAngulo =  np.sin(angulo)

    

    return senAngulo, angulo



def longitud_Onda(senAngulo,ancho_Rejilla):

    """
    Convierte ángulo de difracción 
    a longitud de onda respectiva.

    """


    longitudOnda = ancho_Rejilla*senAngulo

    return longitudOnda




""" INICIO SECCIÓN ASOCIADA CORRECCIÓN ESPECTRAL DATA SENSOR  """

 
def sensibilidad_Sensor(lambda_nm):

    # Definición de tabla asociada a curva de sensibilidad sensor

    ### LONGITUD DE ONDA
    lambda_tabla = [
        500,
        550,
        600,
        650,
        700,
        750,
        800,
        850,
        900,
        950,
        1000
    ]

    ### SENSIBILIDAD ASOCIADA
    S_tabla = [
        0.00,
        0.03,
        0.10,
        0.25,
        0.40,
        0.47,
        0.48,
        0.45,
        0.35,
        0.25,
        0.12
    ]


    # Retornando valor de sensibilidad correspondiente a la longitud de onda ingresada 
    return np.interp(
        lambda_nm,
        lambda_tabla,
        S_tabla
    )



def corregir_espectro(lux_medido, lambda_nm):

    sensibilidad = sensibilidad_Sensor(lambda_nm)

    return lux_medido / sensibilidad

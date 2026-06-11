
""" Importación de librerias """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



""" INICIO SECCIÓN ASOCIADA DEFINICIÓN DE FUNCIONES PARA PROCESAMIENTO DATA SENSOR  """

def pasos_a_desplazamiento(numero_pasos,desplazamiento_paso = 3.8528E4): # DESPLAZAMIENTO DEL PASO EN nm

    """
    Convierte número de pasos del motor
    a desplazamiento físico.

    """

    desplazamiento = numero_pasos * desplazamiento_paso

    return desplazamiento



def Angulo(desplazamiento,distancia_RedToSensor = 5E7): #SEPARACION RED-SENSOR ES DE APROX 5E7nm=50mm

    """
    Convierte desplazamiento del motor
    en el ángulo de difracción asociado.

    """

    hipotenusa = np.sqrt((distancia_RedToSensor**2) + (desplazamiento)**2)

    senAngulo =  desplazamiento/hipotenusa

    Angulo = np.arcsin(senAngulo) # OUTPUT por defecto en RADIANES

    return senAngulo, Angulo




def longitud_Onda(senAngulo,ancho_Rejilla = 1E3): #PERIODO REJILLA (1000ln/mm) ES DE APROX 1000nm

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
        500, 525, 550, 575, 600,
        625, 650, 675, 700, 725,
        750, 775, 800, 825, 850,
        875, 900, 925, 950, 975,
        1000, 1025, 1050, 1075, 1100
    ]

    ### SENSIBILIDAD ASOCIADA (Canal 1)
    """
    S_tabla = [
        0.00, 0.01, 0.03, 0.07, 0.12,
        0.18, 0.25, 0.31, 0.37, 0.42,
        0.46, 0.48, 0.48, 0.47, 0.45,
        0.42, 0.38, 0.33, 0.27, 0.21,
        0.15, 0.10, 0.06, 0.03, 0.01
    ]"""
    
    ### SENSIBILIDAD ASOCIADA (Canal 0)
    S_tabla = [
        0.84, 0.89, 0.92, 0.95, 0.97,
        0.99, 1, 0.99, 0.96, 0.89,
        0.87, 0.84, 0.80, 0.75, 0.55,
        0.53, 0.48, 0.43, 0.35, 0.25,
        0.18, 0.16, 0.10, 0.08, 0.02
    ]
    

    # Retornando valor de sensibilidad correspondiente a la longitud de onda ingresada 
    return np.interp(
        lambda_nm,
        lambda_tabla,
        S_tabla
    )



def corregir_espectro(lux_medido, lambda_nm):

    sensibilidad = sensibilidad_Sensor(lambda_nm)

    # Evitar división por valores muy pequeños
    sensibilidad = max(sensibilidad, 0.01)

    return lux_medido / sensibilidad



 
def sensibilidad_SensorInclinacionAngular(angle):

    # Definición de tabla asociada a curva de sensibilidad sensor

    ### COORDENADA ANGULAR
    angle_tabla = [
        0.0000,  # 0°
        0.1745,  # 10°
        0.3491,  # 20°
        0.5236,  # 30°
        0.6981,  # 40°
        0.8727,  # 50°
        1.0472,  # 60°
        1.2217,  # 70°
        1.3963,  # 80°
        1.5708   # 90°
    ]

    # Respuesta normalizada aproximada
    S_tabla = [
        1.00,  # 0°
        0.98,  # 10°
        0.94,  # 20°
        0.87,  # 30°
        0.76,  # 40°
        0.64,  # 50°
        0.52,  # 60°
        0.37,  # 70°
        0.21,  # 80°
        0.06   # 90°
    ]
    

    # Retornando valor de sensibilidad correspondiente a la longitud de onda ingresada 
    return np.interp(
        angle,
        angle_tabla,
        S_tabla
    )



def corregir_espectroInclinacionAngular(lux_medido, angle):

    sensibilidad = sensibilidad_SensorInclinacionAngular(angle)

    # Evitar división por valores muy pequeños
    sensibilidad = max(sensibilidad, 0.01)

    return lux_medido / sensibilidad





""" INICIO SECCIÓN ASOCIADA DEFINICIÓN DE FUNCIONES PARA CALIBRACIÓN  """


def resolucion(numeroPasos = 1):  
    
    desplazamiento_Minimo = pasos_a_desplazamiento(numeroPasos) #Calcula el desplazamiento asociado a UN paso del motor
    
    senAngulo,angulo = Angulo(desplazamiento_Minimo) # Calcula las coordenadas angulares asociadass al desplazamiento del motor
    
    resolucionLongOnda = longitud_Onda(senAngulo) # Calcula el valor asociada a mínima separación entre longitudes de óptica para resolver como independientes

    return resolucionLongOnda



def error_relativo(x_med,y_med):
    
    # IMPORTANDO DOC. CON INFO ESPECTROMETRO THORLABS
    tabla = pd.read_csv(
        "C:/Users/lauri/Downloads/laura.csv/laura.csv",
        sep=";",
        skiprows=53,
        header=None,
        names=["LongitudOnda", "Intensidad"]
    )

    # SIGUE SECCIÓN DE CONVERSIÓN A VALORES NUMÉRICOS
    
    tabla["LongitudOnda"] = pd.to_numeric(
        tabla["LongitudOnda"],
        errors="coerce"
    )

    tabla["Intensidad"] = pd.to_numeric(
        tabla["Intensidad"],
        errors="coerce"
    )

    #Eliminando filas de NO utilidad
    tabla = tabla.dropna()

    
    #Conversión a arreglos de numpy
    x_ref = tabla["LongitudOnda"].to_numpy()
    y_ref = tabla["Intensidad"].to_numpy()

    
    # NORMALIZANDO AMBAS CURVAS DE DATA
    y_ref_norm = y_ref / np.max(y_ref)
    y_med_norm = y_med / np.max(y_med)
    
    # Comenzando proceso de interpolacion 
    y_ref_interp = np.interp(x_med, x_ref,y_ref_norm)

  
    #Calculando porcentaje de error relativo PUNTO A PUNTO
    
    
    # error_relativo = np.abs(
    #     (y_med_norm - y_ref_interp)
    #     / y_ref_interp) * 100

    errores = []

    for i in range(len(x_med)):

        if (
           y_med_norm[i] > 0.1
        ):

            error = abs(
                (y_med_norm[i] - y_ref_interp[i])
                / y_ref_interp[i]
            ) * 100

            errores.append(error)
        
        else:
            errores.append(0)
    
    #Calculando error relativo PROMEDIO
    error_promedio = np.mean(errores)

    
    # ==================================================
    # GRÁFICA COMPARATIVA
    # ==================================================

    plt.figure(figsize=(10, 6))

    plt.plot(
        x_ref,
        y_ref_norm,
        label="Referencia (Thorlabs)"
    )

    plt.plot(
        x_med,
        y_med_norm,
        label="Espectrofotómetro"
    )

    plt.xlabel("Longitud de onda (nm)")
    plt.ylabel("Intensidad normalizada")
    plt.title(
        f"Comparación espectral\nError relativo promedio = {error_promedio:.2f}%"
    )

    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


    # ==================================================
    # EXPORTAR DATOS MEDIDOS A CSV
    # ==================================================

    # datos_exportar = pd.DataFrame({
    #     "LongitudOnda_nm": x_med,
    #     "Intensidad_Normalizada": y_med_norm
    # })

    # ruta_salida = "C:/Users/lauri/Downloads/espectro_medido.csv"

    # datos_exportar.to_csv(
    #     ruta_salida,
    #     index=False,
    #     sep=";"
    # )

    # print(f"Archivo guardado en:\n{ruta_salida}")

    return error_promedio



def incertidumbre_medida(y_med):

    y_med = np.asarray(y_med)

    n = len(y_med)

    media = np.mean(y_med)

    desviacion_estandar = np.std(
        y_med,
        ddof=1
    )

    incertidumbre = (
        desviacion_estandar
        / np.sqrt(n)
    )

    incertidumbre_expandida = (
        2 * incertidumbre
    )

    return {
        "n": n,
        "media": media,
        "desviacion_estandar": desviacion_estandar,
        "incertidumbre": incertidumbre,
        "incertidumbre_expandida": incertidumbre_expandida
    }




def procesar_precision(espectros):

    intensidades = []

    for barrido in espectros:

        intensidades.append(
            barrido["intensidades"]
        )
    
    #CONVIRTIENDO DATA DE INTENSIDADES EN UNA REPRESENTACION MATRICIAL
    intensidades = np.array(intensidades)

    #Calculando media de valores de intensidad recolectados
    media = np.mean(
    intensidades,
    axis=0
    )


    #Calculando DESVIACION ESTANDAR de valores de intensidad recolectados
    desviacion = np.std(
    intensidades,
    axis=0
    )

    # DEFINIENDO DATA ASOCIADA A EJE X 
    longitudes = espectros[0]["longitudes"]


    return (
    longitudes,
    media,
    desviacion
    )




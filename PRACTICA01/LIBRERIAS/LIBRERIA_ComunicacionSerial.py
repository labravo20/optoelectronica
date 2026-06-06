
""" INICIO SECCIÓN: Importación de librerias"""
import serial



""" INICIO SECCIÓN CONEXIÓN CON PUERTO SERIAL  """

# Creando Conexión Serial
# --> Inicializa comunicación con el microcontrolador (mcu) <--
ser = serial.Serial(
    
    ### IMPORTANTE VERIFICAR PUERTO ASOCIADO AL mcu EN USO 
    port='COM3', 
    
    # Velocidad de comunicación --> Valor estándar establecido en el mcu
    baudrate=115200
)
 


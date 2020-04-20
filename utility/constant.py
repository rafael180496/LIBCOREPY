"""
Es-Se carga todas las constante del paquete utility.

En-All utility package constants are loaded.
"""

import utility.msj as msj

#FORMAT_DATE_DEFAULT : ES-Formato por defecto de pasar un date a string
#FORMAT_DATE_DEFAULT : EN-Default format of passing a date to string
FORMAT_DATE_DEFAULT="{yyyy}{mm}{dd}"

#BS : ES-Cantidad de byte que contiene la llave
#BS : EN-Amount of byte containing the key
BS=16

#MSJ : ES-Contiene los mensajes de la libreria
#MSJ : EN-Contains the messages from the library
MSJ=msj.Msj({
    "P01":"Prueba",
    "JS01":"Error converting dictionary to json",
    "JS02":"Error converting json to dictionary"
})

def GetMsj():
    """
    Es-Obtiene una instancia de la variable global de errores.
    
    En-Gets an instance of the global error variable.
    """
    global MSJ
    return MSJ

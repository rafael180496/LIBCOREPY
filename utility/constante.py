import utility.msj as msj

MSJ=msj.Msj({
    "P01","Prueba"
})

def GetMsj():
    """
    Es-Obtiene una instancia de la variable global de errores.
    
    En-Gets an instance of the global error variable.
    """
    global MSJ
    return MSJ

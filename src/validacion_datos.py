
def validar_registro(registro):
    """
    def validar_registro(registro):

        Que hace la funcion: 
            Verifica los tipo de datos y que los valores no esten vacios ni sean negativos

        Parameteros:
            registro(dicc): diccionario con los datos de un registro     

        Retornos:
            bool: True si el registro es valido y False si el registro no es valido

        """
    if "id_participante" not in registro or "fecha" not in registro or "app" not in registro or "cantidad_uso" not in registro or"tiempo_uso" not in registro:
        return False
    
    if registro["fecha"] == "":
        return ("la fecha ingresada es incorrecta")
    if registro["app"] == "":
        return ("el nombre de la aplicacion es incorrecto")
    if registro["id_participante"] <= 0:
        return ("el id del participante es incorrecto")
    if registro["cantidad_uso"] <0:
        return ("el valor ingresado en cantidad de uso es incorrecto")
    if registro["tiempo_uso"] <0:
        return ("el valor ingresado en tiempo de uso es incorrecto")
    
    return True
 
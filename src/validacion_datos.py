
def validar_registro(registro):
    """
    Valida un registro verificando:
    - existencia de claves
    - tipos de datos
    - valores válidos

    Returns:
        (bool, str): (True, "") si es válido
                     (False, mensaje_error) si no lo es
    """
    claves = ["id_participante", "fecha", "app", "cantidad_uso", "tiempo_uso"]

    for clave in claves:
        if clave not in registro:
            return False, f"Falta la clave: {clave}"

    try:
        id_participante = int(registro["id_participante"])
        fecha = str(registro["fecha"])
        app = str(registro["app"])
        cantidad_uso = int(registro["cantidad_uso"])
        tiempo_uso = float(registro["tiempo_uso"])

    except ValueError:
        return False, "Error en tipos de datos"

    if fecha == "":
        return False, "Fecha vacía"

    if app == "":
        return False, "App vacía"

    if id_participante <= 0:
        return False, "ID inválido"

    if cantidad_uso < 0:
        return False, "Cantidad de uso inválida"

    if tiempo_uso < 0:
        return False, "Tiempo de uso inválido"

    return True, ""
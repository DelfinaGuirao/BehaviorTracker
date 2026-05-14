# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:42:21 2026

@author: delfi
"""
#chequear que el id exista
def filtrar_por_participante(datos, id_participante):
    """
    "Recibe un diccionario y un id. A partir del id que recibe, crea un filtro devolviendo un diccionario con solo aquellos id's que coincidan con el del parametro"

    Parameters
    ----------
    datos: dicc
        Diccionario que tiene como clave el tipo de informacion y como valor una lista con los correspondientes datos.
    id_participante : int
        ID que va a funcionar como filtro para devolver el diccionario final.

    Returns
    -------
    dicc_procesado : dicc
        Diccionario procesado con el filtro del id ingresado.

    """
    dicc_procesado = {
        "id_participante": [],
        "fecha": [],
        "app": [],
        "cantidad_uso": [],
        "tiempo_uso": []
    }

    for i in range(len(datos["id_participante"])):

        if datos["id_participante"][i] == id_participante:

            dicc_procesado["id_participante"].append(datos["id_participante"][i])
            dicc_procesado["fecha"].append(datos["fecha"][i])
            dicc_procesado["app"].append(datos["app"][i])
            dicc_procesado["cantidad_uso"].append(datos["cantidad_uso"][i])
            dicc_procesado["tiempo_uso"].append(datos["tiempo_uso"][i])

    return dicc_procesado
    

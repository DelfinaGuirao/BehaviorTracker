# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:42:21 2026

@author: delfi
"""

def procesamiento_datos(datos, id_participante):
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
    dicc_procesado = {}

    for i in range(len(datos["id_participante"])):

        if datos["id_participante"][i] == id_participante:

            if "id_participante" not in dicc_procesado:
                dicc_procesado["id_participante"] = []
            dicc_procesado["id_participante"].append(datos["id_participante"][i])

            if "fecha" not in dicc_procesado:
                dicc_procesado["fecha"] = []
            dicc_procesado["fecha"].append(datos["fecha"][i])
            
            if "app" not in dicc_procesado:
                dicc_procesado["app"] = []
            dicc_procesado["app"].append(datos["app"][i])

            if "cantidad_uso" not in dicc_procesado:
                dicc_procesado["cantidad_uso"] = []
            dicc_procesado["cantidad_uso"].append(datos["cantidad_uso"][i])
            
            if "tiempo_uso" not in dicc_procesado:
                dicc_procesado["tiempo_uso"] = []
            dicc_procesado["tiempo_uso"].append(datos["tiempo_uso"][i])
        else:
            print("No hay informacion sobre el id ingresado.")

    return dicc_procesado
    

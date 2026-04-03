# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:42:46 2026

@author: delfi
"""

def calcular_tiempo_total(datos):
    """
    La funcion recibe por parametro un dicc y calcula el tiempo total

    arg:
        dicc_procesado: diccionario  con claves (id, fecha, app, cantidad_uso, tiempo_uso)
        y listas como valores
        
    returns:
        num(float): tiempo total 
       

    """
    total = 0

    for tiempo in datos["tiempo_uso"]:
        total += tiempo

    return total

        

def calcular_promedio_uso(datos):
    """
    la funcion recibe un dicc y de ahi guarda la cantidad de uso en una variable para luego\
        calcular el promedio de uso
        
    args:
        dicc_procesado: un diccionario con claves (id, fecha, app, cantidad_uso, tiempo_uso)
        y listas como valores
        
    returns:
        num(float): el promedio calculado por el tiempo total y la cantidad de uso
        
        """

    total_tiempo = calcular_tiempo_total(datos)
    total_usos = 0
    
    for cantidad in datos["cantidad_uso"]:
        total_usos += cantidad

    if total_usos == 0:
        return 0   
    promedio= total_tiempo / total_usos
    return promedio
        

    
        
    




        
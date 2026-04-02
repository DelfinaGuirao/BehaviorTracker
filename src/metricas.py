# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:42:46 2026

@author: delfi
"""

def calcular_tiempo_total(dicc_procesado):
    """
    La funcion recibe por parametro un dicc y calcula el tiempo total

    arg:
        dicc_procesado: diccionario  con claves (id, fecha, app, cantidad_uso, tiempo_uso)
        y listas como valores
        
    returns:
        num(float): tiempo total 
       

    """
    tiempo_total=0
   
    for tiempo_uso in dicc_procesado["tiempo_uso"]:

        tiempo_total= tiempo_total + tiempo_uso
        
    return tiempo_total 
        
        


def calcular_promedio_uso(dicc_procesado):
    """
    la funcion recibe un dicc y de ahi guarda la cantidad de uso en una variable para luego\
        calcular el promedio de uso
        
    args:
        dicc_procesado: un diccionario con claves (id, fecha, app, cantidad_uso, tiempo_uso)
        y listas como valores
        
    returns:
        num(float): el promedio calculado por el tiempo total y la cantidad de uso
        
        """
    cant_uso_total=0
    
    for cantidad_uso in dicc_procesado["cantidad_uso"]:
        cant_uso_total +=1
        
  
    tiempo_uso=calcular_tiempo_total(dicc_procesado)
    
    promedio_uso= tiempo_uso/ cant_uso_total
    
    return promedio_uso
    
 
        

    
        
    




        
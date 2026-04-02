# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:37:44 2026

@author: delfi
"""

from src.cargar_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total, calcular_promedio_uso


def main():
    # 1. Cargar datos
    datos_proyecto = cargar_datos("datos/datos.csv")

    # 2. Pedir ID al usuario
    id_participante = int(input("Ingrese el ID del participante: "))

    # 3. Filtrar datos
    datos_participante = filtrar_por_participante(datos_proyecto, id_participante)

    # 4. Verificar si existe el participante
    if len(datos_participante["id_participante"]) == 0:
        print("No se encontraron datos para ese participante.")
        return
    # 5. Calcular métricas
    tiempo_total = calcular_tiempo_total(datos_participante)
    promedio = calcular_promedio_uso(datos_participante)
    
    if len(datos_participante["id_participante"]) == 0:
        print("No hay informacion sobre el id ingresado.")

    # 6. Mostrar resultados
    print("\nResultados:")
    print("Participante:", id_participante)
    print("Tiempo total de uso:", tiempo_total)
    print("Promedio de uso:", promedio)


main()
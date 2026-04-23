# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:37:44 2026

@author: delfi
"""

from src.cargar_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total, calcular_promedio_uso
from src.validacion_datos import validar_registro


def main():
    """
 Función principal del programa.

 Coordina el flujo general del sistema:
 - Carga los datos desde un archivo CSV.
 - Valida los registros individualmente.
 - Solicita al usuario un ID de participante.
 - Filtra los datos correspondientes a ese ID.
 - Calcula métricas de uso (tiempo total y promedio).
 - Muestra los resultados por pantalla.

 Parameters:
 ----------
 None
     La función no recibe parámetros directamente, pero solicita
     al usuario un ID de participante mediante entrada por teclado.

 Returns:
 -------
 None
     No retorna valores, solo imprime los resultados en pantalla.
 """
    try:
        datos = cargar_datos("datos/BehaviorTracker_mock_data_error10.csv")
    except Exception as e:
        print (e)

    else:
        datos_validos = {
        "id_participante": [],
        "fecha": [],
        "app": [],
        "cantidad_uso": [],
        "tiempo_uso": []
    }

    for i in range(len(datos["id_participante"])):

        registro = {
            "id_participante": datos["id_participante"][i],
            "fecha": datos["fecha"][i],
            "app": datos["app"][i],
            "cantidad_uso": datos["cantidad_uso"][i],
            "tiempo_uso": datos["tiempo_uso"][i]
        }

        valido, mensaje= validar_registro(registro)

        if valido:
            for clave in datos_validos:
                datos_validos[clave].append(registro[clave])

    id_participante = int(input("Ingrese el ID del participante: "))

    datos_filtrados = filtrar_por_participante(datos_validos, id_participante)

    if len(datos_filtrados["id_participante"]) == 0:
        print("No hay informacion sobre el id ingresado.")
        return None #no hace el print

    tiempo_total = calcular_tiempo_total(datos_filtrados)
    promedio = calcular_promedio_uso(datos_filtrados)

    print("\nResultados:")
    print("Participante:", id_participante)
    print("Tiempo total de uso:", tiempo_total)
    print("Promedio de uso:", promedio)


main()

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:37:44 2026

@author: delfi
"""

id_participante= input("Ingrese ID: ")
datos=cargar_datos(x,y)
dicc_procesado= procesamiento_datos(datos, id_participante)
tiempo_total= calcular_timepo_total(dicc_procesado)
calcular_promedio_uso=calcular_promedio_uso(dicc_procesado)
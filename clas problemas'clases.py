# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:47:00 2026

@author: delfi
"""

class Alumno:
    def __init__(self, nombre, legajo):
        self.nombre= nombre
        self.legajo= legajo
        self.asistencias= 0
        self.notas= []
        
    def registrar_asistencia(self):
        self.asistencias+=1
        
    def agregar_nota(self, nota):
        self.notas.append(nota)
        
    def promedio(self):
        sum(self.notas)/len(self.notas)
        
class Materia:
    def __init__(self, nombre):
        self.nombre= nombre
        self.alumnos=[]

    def agregar_alumno(self, alumno):
         self.alumnos.append(alumno)
         
    def mostrar_alumnos(self):
        for alumno in self.alumnos:
            print("Nombre del alumno:", self.nombre)
            print("legajo:", self.legajo)

alumno1= Alumno("maira", 1554)
alumno2= Alumno("tomas", 1236)
alumno3= Alumno("emilia", 1896)

materia1= Materia("Lengua")
materia2= Materia("Matematica")
materia1.agregar_alumno(alumno1)
materia1.agregar_alumno(alumno3)
materia2.agregar_alumno(alumno2)

materia1.mostrar_alumnos()

for alumno in materia1.alumnos:
    materia1.agregar_alumno(alumno)
    
for alumno in materia1.alumnos:
    alumno.registrar_asistencia()
    alumno.agregar_notas(9)
    
materia1.mostrar_alumnos()
    
    

    
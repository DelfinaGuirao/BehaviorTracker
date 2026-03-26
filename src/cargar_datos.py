def parsear_linea (linea):
    linea_strip=linea.strip("\n")
    linea_split=linea_strip.split(";")
    registro={"id_participante": int(linea_split[0]), "fecha":linea_split[1], "app":linea_split[2], "cantidad_uso":int(linea_split[3]), "tiempo_uso":float(linea_split[4])}
    return registro
def cargar_datos (ruta): 
    datos=[]
    archivo=open(ruta,"r")
    for linea in archivo:
        if linea.strip() != "":
            registro = parsear_linea(linea)
            datos.append(registro)
    archivo.close()

    return datos

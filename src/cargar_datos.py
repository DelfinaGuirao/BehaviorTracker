def parsear_linea (linea):
    '''
    Recibe un archivo del cual separa las lineas en respectivos campos, convierte los valores a su tipo correspondiente. 
    La linea del arichvo contien los datos de los campos separados por un punto y coma (;) en orden: id_participante;fecha;cantidad_uso;tiempo_uso.
    
    Parameters: 
    ----------
        linea (str): cadena de texto proviente de una linea del archvio. 
    
    Returns: 
    -------
        lista: lista con valores parseados en el siguente orden: [id_partiicpante (int), fecha(str), app (str), cantidad_uso (int), tiempo_uso (float)]

    '''
    linea = linea.strip("\n")
    campos = linea.split(",")

    id_participante = int(campos[0])
    fecha = campos[1]
    app = campos[2]
    cantidad_uso = int(campos[3])
    tiempo_uso = float(campos[4])

    return [id_participante, fecha, app, cantidad_uso, tiempo_uso]

def cargar_datos (ruta):
    '''
    Lee un archivo de datos, rcorre cada una de las lineas del archvio utilziando la funcion parsear_linea. Con la lista devuelta, construye un diccionario de lsitas donde cada clave corresponde a un campo y almacena valores de todas als lineas del archvio. 
    
    Parameters 
    ----------
    ruta (str): ruta del archivo a procesar 

    Returns
    -------
    datos= diccionario con lista con calves: "id_participante":list [int], "fecha": lista[str], "app": list[str], "cantidad_uso": list [int], "tiempo_uso": list[float]
    
    '''
    datos = {
        "id_participante": [],
        "fecha": [],
        "app": [],
        "cantidad_uso": [],
        "tiempo_uso": []
    }

    with open(ruta, "r", encoding="utf-8") as archivo:
        next(archivo)  #esto saltea el encabezado
        for linea in archivo:
            id_p, fecha, app, cant, tiempo = parsear_linea(linea)

            datos["id_participante"].append(id_p)
            datos["fecha"].append(fecha)
            datos["app"].append(app)
            datos["cantidad_uso"].append(cant)
            datos["tiempo_uso"].append(tiempo)

    return datos

        
        
    
    

    
    
        
    
    
    
   

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
    linea=linea.strip("\n")
    campo=linea.split (";")
    id_participante= int (campo[0])
    fecha= campo [1]
    app=campo[2]
    cantidad_uso=int(campo[3])
    tiempo_uso= int(campo[4])
    return [id_participante,fecha,app,cantidad_uso,tiempo_uso] 

def cargar_datos (ruta):
    #hola
    '''
    Lee un archivo de datos, rcorre cada una de las lineas del archvio utilziando la funcion parsear_linea. Con la lista devuelta, construye un diccionario de lsitas donde cada clave corresponde a un campo y almacena valores de todas als lineas del archvio. 
    
    Parameters 
    ----------
    ruta (str): ruta del archivo a procesar 

    Returns
    -------
    datos= diccionario con lista con calves: "id_participante":list [int], "fecha": lista[str], "app": list[str], "cantidad_uso": list [int], "tiempo_uso": list[float]
    
    '''
    datos={"id_participante": [], "fecha":[], "app":[], "cantidad_uso": [], "tiempo_uso":[]}
    archivo=open (ruta,"r")
    for linea in archivo:
        info= parsear_linea(linea)
        datos["id_participante"].append(info[0])
        datos["fecha"].append(info[1])
        datos["app"].append (info[2])
        datos["cantidad_uso"].append (info[3])
        datos["tiempo_uso"].append (info[4])
    archivo.close()
    return datos 

        
        
    
    

    
    
        
    
    
    
   

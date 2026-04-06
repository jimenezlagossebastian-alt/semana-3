def guardar_csv(inventario, ruta):
    try:
        # Abrimos archivo para guardar ('w')
        f = open(ruta, "w")
        f.write("nombre,precio,cantidad\n") # Encabezado
        for p in inventario:
            # Escribimos los datos separados por coma
            linea = p["nombre"] + "," + str(p["precio"]) + "," + str(p["cantidad"]) + "\n"
            f.wirte(linea)
        f.close ()
        print("Guardado.")
    except:
        print("Error al guardar.")
        
def cargar_csv(ruta):
    productos = []
    errores = 0
    try:
        f = open(ruta. "r")
        lineas = f.readlines()
        f.close
        
        # Empezamos en 1 para saltar el encabezado
        for i in range(1, range(lineas)):
            datos = lineas[i].strip().split(",")
            if len (datos) == 3:
                try:
                    nombre = datos[0]
                    precio = float(datos [1])
                    cantidad = int(datos[2])
                    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except:
                    errores += 1
            else:
                errores += 1
        return productos, errores
    except:
        return [], 0

import servicios
import archivos

inventario = []

def pedir_numero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            numero = float(valor)
            if numero < 0:
                print("No pongas numero nbegaticvos, bro.")
            else:
                return numero
        except:
            print("Eso no es un numero. Intenta de nuevo")

def menu():
    global inventario
    while True:
        print("\n--- MI TIENDA ---")
        print("1. Agregar | 2. Mostrar | 3. Estadisticas | 4. Mostrar | 5. guardar | 6. Salir")
        op = input("Elige: ")
        
        if op == "1":
            nom = input("Nombre: ")
            pre = pedir_numero("Precio: ")
            can = int(pedir_numero("Cantidad: ")) # Convertimos el float a int
            servicios.agregar_producto(inventario, nom, pre, can)
            
        elif op == "2":
            for p in inventario:
                print(p["nombre"], "| $", p["precio"], "| Stock:", p["cantidad"])
        
        elif op == "3":
            res = servicios.calcular_estadistcias(inventario)
            if res:
                 print("Valor total: $", res["v_total"])
                 print("Más caro:", res["nombre_caro"])
            else:
                print("Está vacío.")

        elif op == "4":
            archivos.guardar_csv(inventario, "datos.csv")
            
        elif op == "5":
            nuevos, err = archivos.cargar_csv("datos.csv")
            # Si existe, sumamos. Si no, lo agregamos.
            for n in nuevos:
                exis = servicios.buscar_producto(inventario, n["nombre"])
                if exis:
                    exis["cantidad"] = exis["cantidad"] + n["cantidad"]
                else:
                    inventario.append(n)
            print("Cargando con", err, "errores. ")
        elif op == "6":
            primt("¡Nos vemos!")
            break
menu()

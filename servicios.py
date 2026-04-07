def agregar_producto(inventario, nombre, precio, cantidad):
    # Creamos el diccionario y lo metemos a la lista
    producto ={"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append (producto)
    
def buscar_producto(inventario, nombre):
    # Buscamos recorriendo la lista uno por uno
    for p in inventario:
        if p in["nombre"].lower() == nombre.lower():
            return p
        return None
    
def calcular_estadistcias(inventario):
    if len(inventraio) == 0:
        return None
    
    total_u = 0
    total_v = 0
    # Usamos el primer porducto como referencia para comprar
    p_caro = inventario = [0]
    p_stock = inventario = [0]
    
    for p in inventario:
        total_u = total_u + p["cantidad"]
        total_v = total_v + (p["precio"] * p["cantidad"])
        
        # ¿Es este más caro que el que yo conocía?
        if p["precio"] > p_stock["cantidad"]:
            p_caro = p
            
    return{
        "u_totales": total_u,
        "v_total": total_v,
        "nombre_caro": p_caro["nombre"],
        "nombre_stock": p_stock["nombre"]
    }

#Lista de clientes
clientes = []

#Menu con opciones
while True:
    print("\nSistema de Gestión Básica De Productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":

        #Ingresar el numero de clientes 
        while True:
            numero_clientes_str = input("¿Cuántos clientes querés ingresar? ")
            if not numero_clientes_str.strip(): #Validación para que no este vacío
             print("¡Error! No puede estar vacío.") 
            elif not numero_clientes_str.isdigit(): #Validación para que sea un número entero positivo
                print("¡Error! Debe ser un número entero positivo.") 
            else:
                numero_clientes = int(numero_clientes_str) #Convertir el string a entero después de la validación
                break  # Salir del bucle si es válido

        # Ingresar nombre del cliente 
        inicio = 0
        while inicio < numero_clientes:
            print("Cliente", inicio + 1)
            while True:
                nombre_cliente = input("Ingrese el nombre del cliente: ")
                if not nombre_cliente.strip(): #Validación para que no este vacío
                    print("¡Error! El nombre del cliente no puede estar vacío.") 
                elif nombre_cliente.isdigit(): #Validación para que no sea un número
                    print("¡Error! El nombre del cliente no puede ser un número.") 
                else:    
                    break  # Salir del bucle si es válido

            # Ingresar los productos del cliente en una lista
            productos = []
            #Ingresar la candidad de productos 
            while True:
                numero_productos_str = input("¿Cuántos productos queres ingresar para este cliente? ")
                if not numero_productos_str.strip(): #Validación para que no este vacío
                    print("¡Error! No puede estar vacío.")
                elif not numero_productos_str.isdigit(): #Validación para que sea un número entero positivo
                    print("¡Error! Debe ser un número entero positivo.")
                else: 
                    numero_productos = int(numero_productos_str) #Convertir el string a entero después de la validación
                    break  # Salir del bucle si es válido
        
            #Ingresar datos de los productos
            inicio_prod = 0
            while inicio_prod < numero_productos:
                print("Producto", inicio_prod + 1)
                #Ingresar nombre del producto 
                while True:
                    nombre_producto = input("Nombre del producto: ")
                    if not nombre_producto.strip(): #Validación para que no este vacío
                        print("¡Error! El nombre del producto no puede estar vacío.") 
                    elif nombre_producto.isdigit():#Validación para que no sea un número
                        print("¡Error! El nombre del producto no puede ser un número.") 
                    else:
                        break  # Salir del bucle si es válido
            
                #Ingresar categoria del producto 
                while True:
                    categoria = input("Categoría del producto: ")
                    if not categoria.strip(): #Validación para que no este vacío
                        print("¡Error! La categoría del producto no puede estar vacía.")                     
                    else:
                        break  # Salir del bucle si es válido
            
                #Ingresar precio del producto 
                while True:
                    precio_str = input("Precio del producto (sin centavos): ")
                    if not precio_str.strip(): #Validación para que no este vacío
                        print("¡Error! El precio del producto no puede estar vacío.") 
                    elif not precio_str.isdigit(): #Validación para que sea un número entero positivo
                        print("¡Error! El precio del producto debe ser un número entero positivo.")
                    else:
                        precio = int(precio_str)  # Convertir a entero después de la validación
                        break  # Salir del bucle si es válido   
            
            
                # Agregar productos a la lista de productos del cliente
                producto = [nombre_producto, categoria, precio]
                productos.append(producto)
                inicio_prod += 1

            # Agregar cliente con sus productos a la lista de clientes
            cliente = [nombre_cliente, productos]
            clientes.append(cliente)
            inicio += 1

    # Mostrar datos
    elif opcion == "2":
        if not clientes: #Mensaje si no se ingresaron clientes
            print("No hay clientes ni productos registrados.")
        else:
            print("Resumen de productos por cliente:")
            for i, cliente in enumerate(clientes): #recorrer la lista de clientes, cada cliente es una lista con el nombre y los productos
                print(f"Cliente {i + 1}: {cliente[0]}") #Imprime el nombre del cliente tomando el primer elemento de la lista cliente
                productos_cliente = cliente[1] #asignar a una variable los productos del cliente, que es el segundo elemento de la lista cliente
                for i, producto in enumerate(productos_cliente): #recorrer la lista de productos del cliente, cada producto es una lista con el nombre, categoria y precio
                    print(f"- Producto {i + 1}: {producto[0]} - Categoria: {producto[1]} - Precio: ${producto[2]}") 
    
    #Buscar un producto por nombre
    elif opcion == "3":
        if not clientes: #Mensaje si no se ingresaron clientes
            print("No hay productos para buscar.")
        else: #Input para pedir el nombre del producto a buscar
            print("Buscar producto por nombre")
            producto_buscado = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()

            encontrado = False #Variable para verificar si se encontró el producto se inicializa en False por defecto
            for cliente_busqueda in clientes: #Recorrer la lista de clientes
                productos_buscados = cliente_busqueda[1] #Asignar a una variable los productos del cliente, que es el segundo elemento de la lista cliente
                for producto_busqueda in productos_buscados: #Recorrer la lista de productos del cliente, cada producto es una lista con el nombre, categoria y precio
                    if producto_busqueda[0].strip().lower() == producto_buscado: #Comparar el nombre del producto ingresado con el nombre del producto en la lista, ignorando mayúsculas y minúsculas
                        print(f"Producto encontrado: {producto_busqueda[0]} (Categoría: {producto_busqueda[1]}, Precio: ${producto_busqueda[2]}) - Cliente: {cliente_busqueda[0]}") #Imprimir el producto encontrado con su categoría, precio y nombre del cliente
                    encontrado = True #Al encontrar el producto, se cambia la variable encontrado a True
                if not encontrado: #Si no se encontró el producto en la lista de productos del cliente, se imprime un mensaje
                    print("No se encontró el producto con ese nombre.")
    
    #Eliminar producto por posición
    elif opcion == "4":
        if not clientes:  # Validar si hay clientes cargados
            print("No hay clientes ni productos registrados.")
        else:
        # Mostrar lista de clientes
            print("Lista de clientes:")
            for i, cliente in enumerate(clientes):
                print(f"{i + 1}. {cliente[0]}")

        # Pedir número de cliente del cual se desea eliminar un producto
            while True:
                cliente_str = input("Seleccione el número del cliente del que desea eliminar un producto: ")
                if not cliente_str.strip(): #Validación para que no este vacío
                    print("¡Error! No puede estar vacío.") 
                elif not cliente_str.isdigit(): #Validación para que sea un número entero positivo
                    print("¡Error! Debe ingresar un número entero.")
                else:
                    cliente_id = int(cliente_str) - 1 # Convertir a índice (restar 1) porque la listas en python comienzan en 0 y el usuario ingresa un número comenzando en 1
                    if cliente_id < 0 or cliente_id >= len(clientes): #Validacion para que el numero del cliente este dentro del rango de clientes
                        print("¡Error! Número de cliente inválido.")
                    else:
                        break #Salir del bucle si es válido

            productos_cliente = clientes[cliente_id][1] # Obtener la lista de productos del cliente seleccionado
            if not productos_cliente: # Validar si el cliente tiene productos
                print("Este cliente no tiene productos.")
            else:
                print(f"Productos de {clientes[cliente_id][0]}:") # Imprimir el nombre del cliente seleccionado
                for i, producto in enumerate(productos_cliente): # Recorrer la lista de productos del cliente
                    print(f"{i + 1}. {producto[0]} ({producto[1]}): ${producto[2]}")# Imprimir el nombre del producto, categoría y precio

                # Pedir número de producto a eliminar
                while True:
                    producto_str = input("Ingrese el número del producto que desea eliminar: ")
                    if not producto_str.strip(): #Validación para que no este vacío
                        print("¡Error! No puede estar vacío.")
                    elif not producto_str.isdigit(): #Validación para que sea un número entero positivo
                        print("¡Error! Debe ingresar un número entero.")
                    else:
                        producto_id = int(producto_str) - 1 # Convertir a índice (restar 1) porque la listas en python comienzan en 0 y el usuario ingresa un número comenzando en 1
                        if producto_id < 0 or producto_id >= len(productos_cliente): #Validacion para que el numero del producto este dentro del rango de productos del cliente
                            print("¡Error! Número de producto inválido.")
                        else:
                            break

                # Eliminar producto
                producto_eliminado = productos_cliente.pop(producto_id) # Eliminar el producto de la lista
                print(f"Producto '{producto_eliminado[0]}' eliminado correctamente.")
    
    #Salir del Menu
    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    # Opción de menu inválida    
    else:
        print("Opción inválida. Por favor ingrese un número entre 1 y 5.")
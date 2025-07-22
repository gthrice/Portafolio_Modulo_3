# inventario.py
from logica_guardar import guardar_objeto, cargar_objeto

def menu():
    print("\n--- Menú del Inventario ---")
    print("1. Agregar objeto al inventario")
    print("2. Mostrar inventario")
    print("3. Eliminar objeto del inventario")
    print("4. Modificar objeto del inventario")
    print("5. Salir")

def agregar_objeto(objeto):
    objetos = cargar_objeto()
    objetos.append(objeto)
    guardar_objeto(objetos)
    print(f"\nEl objeto '{objeto['nombre']}' ha sido agregado al inventario.\n")

def mostrar_inventario(objetos):
    print("\n" + "--" * 20)
    print("Inventario:")
    if not objetos:
        print("El inventario está vacío.")
    else:
        for i, objeto in enumerate(objetos):
            print(f"{i + 1}. Nombre: {objeto['nombre']} - Precio: ${objeto['precio']} - Cantidad: {objeto['cantidad']} - Características: {objeto['caracteristicas']}")
    print("--" * 20)

def main():
    print("--" * 20)
    print("Bienvenidos al sistema de inventario en Python")
    print("--" * 20)

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1": # --- AGREGAR OBJETO ---
            try:
                nombre = input("Ingrese el nombre del objeto: ")
                precio = float(input("Ingrese el precio del objeto: "))
                cantidad = int(input("Ingrese la cantidad del objeto: "))
                caracteristicas = input("Ingrese las características del objeto: ")
                
                nuevo_objeto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad,
                    "caracteristicas": caracteristicas
                }
                agregar_objeto(nuevo_objeto)

            except ValueError:
                print("\nError: El precio y la cantidad deben ser números. Intente de nuevo.\n")

        elif opcion == "2": # --- MOSTRAR INVENTARIO ---
            objetos = cargar_objeto()
            mostrar_inventario(objetos)
            if objetos:
                valor_total = sum(obj["precio"] * obj["cantidad"] for obj in objetos)
                print(f"Total de tipos de objetos: {len(objetos)}")
                print(f"Valor total del inventario: ${valor_total:.2f}")
            print("--" * 20)

        elif opcion == "3": # --- ELIMINAR OBJETO ---
            objetos = cargar_objeto()
            if not objetos:
                print("\nEl inventario está vacío. No hay nada que eliminar.\n")
                continue
            mostrar_inventario(objetos)
            try:
                id_eliminar_str = input("Ingrese el ID del objeto a eliminar (o presione Enter para cancelar): ")
                if not id_eliminar_str:
                    continue
                id_eliminar = int(id_eliminar_str)
                if 1 <= id_eliminar <= len(objetos):
                    objeto_eliminado = objetos.pop(id_eliminar - 1)
                    guardar_objeto(objetos) 
                    print(f"\nEl objeto '{objeto_eliminado['nombre']}' ha sido eliminado del inventario.\n")
                else:
                    print("\nID inválido. No existe un objeto con ese ID.\n")
            
            except ValueError:
                print("\nError: Debe ingresar un número de ID válido.\n")

        elif opcion == "4":
            objetos = cargar_objeto()
            if not objetos:
                print("\nEl inventario está vacío. No hay nada que modificar.\n")
                continue
            mostrar_inventario(objetos)
            try:
                id_modificar_str = input("Ingrese el ID del objeto a modificar (o presione Enter para cancelar): ")
                if not id_modificar_str: # si no se ingresa nada
                    continue
                id_modificar = int(id_modificar_str)
                if not (1 <= id_modificar <= len(objetos)):
                    print("\nID inválido. No existe un objeto con ese ID.\n")
                    continue
                objeto_a_modificar = objetos[id_modificar - 1]
                while True:
                    print(f"\nModificando el objeto: '{objeto_a_modificar['nombre']}' - Precio: ${objeto_a_modificar['precio']} - Cantidad: {objeto_a_modificar['cantidad']} - Características: {objeto_a_modificar['caracteristicas']}")
                    print("\nSeleccione el campo que desea modificar:")
                    print("1. Nombre")
                    print("2. Precio")
                    print("3. Cantidad")
                    print("4. Características")
                    print("5. Salir")
                    opcion_modificar = input("Seleccione una opcción: ")
                    if opcion_modificar == "1":# Modificar nombre
                        nuevo_nombre = input(f"Nuevo nombre ({objeto_a_modificar['nombre']}): ")
                        if nuevo_nombre.strip(): #.strip() para quitar espacios en blanco
                            objeto_a_modificar['nombre'] = nuevo_nombre
                            print(f"\nEl nombre del objeto '{objeto_a_modificar['nombre']}' ha sido modificado.\n")
                    elif opcion_modificar == "2": # Modificar precio
                        nuevo_precio_str = input(f"Nuevo precio (${objeto_a_modificar['precio']}): ")
                        if nuevo_precio_str.strip():
                            try:
                                objeto_a_modificar['precio'] = float(nuevo_precio_str)
                                print(f"\nEl precio del objeto '{objeto_a_modificar['precio']}' ha sido modificado.\n")
                            except ValueError:
                                print("Error: Ingrese un precio numérico válido.")
                    elif opcion_modificar == "3":
                        while True:
                            nueva_cantidad_str = input(f"Nueva cantidad ({objeto_a_modificar['cantidad']}): ")
                            if nueva_cantidad_str.strip():
                                try:
                                    objeto_a_modificar['cantidad'] = int(nueva_cantidad_str)
                                    print(f"\nLa cantidad del objeto '{objeto_a_modificar['cantidad']}' ha sido modificada.\n")
                                    break
                                except ValueError:
                                    print("Error: Ingrese una cantidad numérica válida.")
                            else:
                                break
                    elif opcion_modificar == "4":# Modificar características
                        nuevas_caracteristicas = input(f"Nuevas características ({objeto_a_modificar['caracteristicas']}): ")
                        if nuevas_caracteristicas.strip():
                            objeto_a_modificar['caracteristicas'] = nuevas_caracteristicas
                            print(f"\nLas características del objeto '{objeto_a_modificar['caracteristicas']}' han sido modificadas.\n")    
                    elif opcion_modificar == "5":
                        guardar_objeto(objetos)
                        print("\nEl objeto ha sido modificado exitosamente.\n")
                        break
                    else:
                        print("\nOpción inválida. Por favor, seleccione una opción del 1 al 5.\n")
                        continue
            except ValueError:
                print("\nError: Debe ingresar un número de ID válido.\n")
        elif opcion == "5":
            print("\nSaliendo del programa... ¡Hasta luego!\n")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione una opción del 1 al 5.\n")

if __name__ == "__main__":
    main()

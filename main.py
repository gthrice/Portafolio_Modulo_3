#invetario.py
from logica_guardar import guardar_objeto, cargar_objeto #importar la logica_guardar

def menu():
    print("1. Agregar objeto al inventario")
    print("2. Mostrar inventario")
    print("3. Eliminar objeto del inventario")
    print("4. Modificar atributos del objeto")
    print("5. Salir")
   
def agregar_objeto(objeto):
    objetos = cargar_objeto()
    objetos.append(objeto)
    guardar_objeto(objetos)

def mostrar_inventario():
    objetos = cargar_objeto()
    for objeto in objetos:
        print(objeto)

def eliminar_objeto(objeto):
    objetos = cargar_objeto()
    objetos.remove(objeto)
    guardar_objeto(objetos)

def mostrar_inventario(objetos):
    print("Inventario:")
    for i, objeto in enumerate(objetos):
        print(f"{i + 1}. Nombre: {objeto["nombre"]} - ${objeto["precio"]} - cantidad: {objeto["cantidad"]} - caracteristicas: {objeto["caracteristicas"]}")
    print("\n")       

def main():
    memoria_invetario = cargar_objeto()
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del objeto: ")
            precio = float(input("Ingrese el precio del objeto: "))
            cantidad = int(input("Ingrese la cantidad del objeto: "))
            caracteristicas = input("Ingrese las características del objeto: ")
            agregar_objeto({"nombre": nombre, "precio": precio, "cantidad": cantidad, "caracteristicas": caracteristicas})
            print(f"\nEl objeto {nombre} ha sido agregado al inventario.\n")
        elif opcion == "2":
            mostrar_inventario(memoria_invetario)
            if len(cargar_objeto()) == 0:
                print("El inventario está vacío.")
        elif opcion == "3":
            ID = input("Ingrese el id del objeto a eliminar: ")
            if not cargar_objeto():
                print("El inventario está vacío.")
                continue
            objeto = cargar_objeto()[int(ID) - 1]
            eliminar_objeto(objeto)
            print(f"\nEl objeto {objeto['nombre']} ha sido eliminado del inventario.\n")
        elif opcion == "4":
            pass
        elif opcion == "5":
            break
    print("Bienvenidos a el sitema de inventario python")

if __name__ == "__main__":
    main()
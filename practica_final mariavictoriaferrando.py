""" 
PRACTICA FINAL: GESTOR DE TAREAS
"""

# Creo clase que representa una tarea y la inicializo con sus atributos
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion   # descripcion de la tarea
        self.completada = False    # por defecto estado no completada = pendiente

    def __str__(self): # creo metodo que devuelve un texto con la descripcion de la tarea y su estado
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

#Creo clase que representa la lista de tareas y la inicializo con sus atributos
class ListaDeTareas:
    def __init__(self):
        self.tareas = []    #Inicializo una lista vacía de tareas


    def agregar_tarea(self, descripcion): # creo método para agregar una nueva tarea a la lista de tareas
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, posicion):   #creo método para marcar una tarea como completada, segun su posición en la lista con manejo de excepciones
        try:
            self.tareas[posicion].completada = True
        except IndexError:
            print("Error: La posición ingresada no es válida.")

    def mostrar_todas_las_tareas(self):   #creo método para mostrar todas las tareas numeradas y su estado
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea}")

    def eliminar_tarea(self, posicion):   #creo método para eliminar una tarea de la lista, dada su posición con manejo de excepciones
        try:
            del self.tareas[posicion]
        except IndexError:
            print("Error: La posición ingresada no es válida.")


#Creo función para mostrar el menú de opciones y gestionar la interacción con el usuario con manejo de excepciones
def menu():
    lista_de_tareas = ListaDeTareas()
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Opción no válida. Por favor, ingrese un número.")
            continue
        
        if opcion == 1:
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == 2:
            try:
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: ")) - 1
                lista_de_tareas.marcar_completada(posicion)
            except ValueError:
                print("Error: La posición ingresada no es válida.")
        elif opcion == 3:
            lista_de_tareas.mostrar_todas_las_tareas()
        elif opcion == 4:
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
                lista_de_tareas.eliminar_tarea(posicion)
            except ValueError:
                print("Error: La posición ingresada no es válida.")
        elif opcion == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 5.")


# Creo funcion para ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    menu()

# gestor-de-tareas
Aquí tienes un programa en Python que gestiona una lista de tareas pendientes utilizando Programación Orientada a Objetos (POO). El programa permite agregar nuevas tareas, marcar tareas como completadas, mostrar todas las tareas y eliminar tareas. Además, maneja excepciones y contiene comentarios explicativos.

Explicación del código:
Clase Tarea:

__init__: Inicializa una nueva tarea con su descripción y estado (pendiente por defecto).
__str__: Devuelve una cadena que representa la tarea con su estado (completada o pendiente).
Clase ListaDeTareas:

__init__: Inicializa una lista vacía de tareas.
agregar_tarea: Agrega una nueva tarea a la lista.
marcar_completada: Marca una tarea como completada según su posición en la lista.
mostrar_todas_las_tareas: Muestra todas las tareas con su número y estado.
eliminar_tarea: Elimina una tarea de la lista según su posición.
Función menu:

Muestra un menú de opciones y permite al usuario interactuar con la lista de tareas.
Utiliza un bucle while para mantener el programa en ejecución hasta que el usuario elija salir.
Maneja excepciones para opciones no válidas y posiciones fuera de rango.
Este programa ofrece una gestión básica de tareas pendientes con manejo de errores y una interfaz de usuario en la línea de comandos.

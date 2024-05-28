# Enunciado:
# Escribe un programa en Python utilizando POO que gestione una lista de tareas
# pendientes. El programa deberá permitir al usuario realizar las siguientes operaciones:
# Agregar una nueva tarea: El programa deberá permitir al usuario agregar una
# nueva tarea a la lista de tareas pendientes.
# Marcar una tarea como completada: El programa deberá permitir al usuario marcar
# una tarea como completada, dada su posición en la lista.
# Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea
# de la lista, dada su posición.
# Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las
# tareas pendientes, numeradas y mostrando su estado(completada o pendiente)


class Tareas: # Creamos la clase para cambiar el estado "pendiente" o "completado" de una tarea

    def __init__(self, nombre): 
        self.pendiente = False # Las tareas de inicio tendrán estado "pendiente"
        self.nombre = nombre

    def completada(self):
        self.pendiente = True  # Las tareas que llamen a este método, cambiarán su estado a "completada"

    def __str__(self):
        estado = "completada" if self.pendiente else "pendiente" 
        return f"{self.nombre} - {estado}"


class GestionTareas: # Creamos la clase que gestiona la lista de tareas

    def __init__(self):
        self.lista = [] # Inicialización de la lista vacía

    def listar_opciones(self): # Clase por la que empezará el usuario a elegir lo que desea hacer
        while True: # usamos un bucle, para que el usuario pueda seguir interactuando mientras no marque la opción de "salir"
            try: # se implementa una excepción para capturar el ValueError
                print("\nElige una opción de la siguiente lista:\n ")
                eleccion = int(input("1. Añadir una nueva tarea a la lista.\n2. Marcar tarea como completada\n3. Eliminar una tarea de la lista\n4. Salir\n\nIntroduce solo el número => "))
                if eleccion == 1:
                    self.nueva_tarea()
                elif eleccion == 2:
                    self.estado_tarea()
                elif eleccion == 3:
                    self.elimina_tarea()
                elif eleccion == 4:
                    print("\n¡Gracias!\n")
                    break
                else:
                    print("\nOpción errónea, debes eligir entre 1 - 4\n")
            except ValueError:
                print("\nDebes introducir un número!\n")
                                       
    def listado_tareas(self):# este método solo imprime las tareas que existen
        if not self.lista: 
            print ("La lista está vacía!\n")
        else:
            print("\nListado de tareas:\n")
            for i, tarea in enumerate(self.lista, start=1):
                print(f"{i}. {tarea}") # debería llamar al método __str__ de Tarea

    def nueva_tarea(self): # función para añadir elementos a la lista de tareas
        self.listado_tareas()
        nombre_tarea = input("Introduce una nueva tarea:\n").strip().lower()
        tarea = Tareas(nombre_tarea)# Llama a la clase constructora Tareas con 1 argumento.
        self.lista.append(tarea) # añade la instancia de Tarea a la lista
        print(f"Nueva tarea '{nombre_tarea}' añadida.")
        self.listado_tareas()
        self.listar_opciones()
        
    def estado_tarea(self): # método para cambiar el estado de una determinada tarea
        self.listado_tareas()
        try: # se implementa excepciones
            cambio = int(input("\nElige número de tarea, para cambiar a completada: ")) - 1
            if 0 <= cambio < len(self.lista):
                self.lista[cambio].completada() #llamamos al método completada() de la clase Tareas 
                print(f"Tarea '{self.lista[cambio]}' completada")
            else:
                print("Índice de tarea no válido") 
        except ValueError:
            print("\nDebes introducir un número!\n")
        self.listado_tareas()
        
    def elimina_tarea(self): # método para eliminar una tarea 
        self.listado_tareas()
        try: # se implementa excepciones
            eliminada = int(input("\nElige número de tarea a eliminar: ")) - 1
            if 0 <= eliminada < len(self.lista):
                tarea_eliminada = self.lista.pop(eliminada)
                print(f"Tarea '{tarea_eliminada.nombre}' eliminada") 
            else:
                print("Índice de tarea no válido")
        except ValueError:
            print("\nDebes introducir un número!\n")
        self.listado_tareas()    


# creación de instancia a la clase GestionTareas y comenzar el menú interactivo   
usuario = GestionTareas() 
usuario.listar_opciones()

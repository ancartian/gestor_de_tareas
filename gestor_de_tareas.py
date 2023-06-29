
class Tarea:
    """Clase que representa una tarea."""

    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

class GestorTareas:
    """Clase que gestiona las tareas."""

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea."""
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, indice):
        """Marca una tarea como completada."""
        if indice >= 0 and indice < len(self.tareas):
            self.tareas[indice].completada = True

    def eliminar_tarea(self, indice):
        """Elimina una tarea."""
        if indice >= 0 and indice < len(self.tareas):
            del self.tareas[indice]

# Ejemplo de uso:
gestor = GestorTareas()

while True:
    
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Eliminar tarea")
    print("4. Mostrar tareas pendientes")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Ingresa una nueva tarea: ")
        gestor.agregar_tarea(tarea)
    elif opcion == "2":
        indice = int(input("Ingresa el índice de la tarea a marcar como completada: "))
        gestor.marcar_completada(indice - 1)
    elif opcion == "3":
        indice = int(input("Ingresa el índice de la tarea a eliminar: "))
        gestor.eliminar_tarea(indice - 1)
    elif opcion == "4":
        print("Tareas pendientes:")
        for indice, tarea in enumerate(gestor.tareas):
            if not tarea.completada:
                print(f"{indice + 1}. {tarea.descripcion}")
        print()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")

for indice, tarea in enumerate(gestor.tareas):
    estado = "Completada" if tarea.completada else "Pendiente"
    print(f"{indice + 1}. {tarea.descripcion} - {estado}")


class TareasPendientes:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append({"descripcion": tarea, "completada": False})
    
    def marcar_completada(self, posicion):
        try:
            self.tareas[posicion]["completada"] = True
            print("Tarea marcada como completada.")
        except IndexError:
            print("La posicion especificada no existe.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes")
        else:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{i + 1}. {tarea['descripcion']} - {estado}")

    def eliminar_tarea(self, posicion):
        try:
            del self.tareas[posicion]
            print("Tarea eliminada.")
        except IndexError:
            print("La posicion especificada no existe.")

def main():
    lista_tareas = TareasPendientes()

    while True:
        print("\n-- Gestor de Tareas Pendientes ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            tarea = input("Ingrese la descripcion de la nueva tarea: ")
            lista_tareas.agregar_tarea(tarea)
        elif opcion == "2":
            lista_tareas.mostrar_tareas()
            posicion = int(input("Ingrese la posicion de la tarea a marcar como completada: ")) - 1
            lista_tareas.marcar_completada(posicion)
        elif opcion == "3":
            lista_tareas.mostrar_tareas()
        elif opcion == "4":
            lista_tareas.mostrar_tareas()
            posicion = int(input("Ingrese la posicion de la tarea a eliminar: ")) - 1
            lista_tareas.eliminar_tarea(posicion)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Por favor, seleccione una opcion valida.")

if __name__ == "__main__":
    main()
    



This code defines a class `TareasPendientes` which is a simple task management system. 
It allows users to add, mark as completed, display, and delete tasks. Here's a breakdown of its functionality:

- **Initialization (`__init__` method):** Initializes an empty list to store tasks.
- **Add Task (`agregar_tarea` method):** Adds a new task to the list, with a default status of not completed.
- **Mark Task as Completed (`marcar_completada` method):** Changes the status of a specified task to completed.
- **Display Tasks (`mostrar_tareas` method):** Prints all tasks with their current status (completed or pending).
- **Delete Task (`eliminar_tarea` method):** Removes a specified task from the list.

The `main` function provides a command-line interface to interact with the `TareasPendientes` class, 
offering options to add, complete, display, and delete tasks, as well as to exit the program. 
This setup allows users to manage their tasks through a simple text-based menu.

import heapq
from datetime import datetime

class Actividad:
    def __init__(self, prioridad, encargado, descripcion, hora, stormtroopers=None):
        self.prioridad = prioridad
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.stormtroopers = stormtroopers
    
    def __str__(self):
        stormtroopers_info = f", {self.stormtroopers} Stormtroopers" if self.stormtroopers else ""
        return f"[Prioridad {self.prioridad}] {self.descripcion} por {self.encargado} a las {self.hora}{stormtroopers_info}"

    def __lt__(self, other):
        return self.prioridad > other.prioridad  
def agregar_actividad(cola, prioridad, encargado, descripcion, hora, stormtroopers=None):
    actividad = Actividad(prioridad, encargado, descripcion, hora, stormtroopers)
    heapq.heappush(cola, actividad)

def atender_actividad(cola):
    if cola:
        actividad = heapq.heappop(cola)
        print(f"Atendiendo: {actividad}")
    else:
        print("No hay actividades pendientes.")

cola_actividades = []

agregar_actividad(cola_actividades, 3, "Kylo Ren", "Buscar información del droide BB-8", "09:00")
agregar_actividad(cola_actividades, 3, "Líder Supremo Snoke", "Supervisar la construcción de la base", "09:30")
agregar_actividad(cola_actividades, 2, "Capitán Phasma", "Revisión de los Stormtroopers", "10:00", 50)
agregar_actividad(cola_actividades, 2, "Capitán Phasma", "Control de armas en el sector 7", "10:30", 30)
agregar_actividad(cola_actividades, 1, "General Hux", "Informe de estado de la base", "11:00")
agregar_actividad(cola_actividades, 1, "General de la base", "Revisión de sistemas de comunicación", "11:30")
agregar_actividad(cola_actividades, 1, "General de la base", "Prueba de sistemas de defensa", "12:00")
agregar_actividad(cola_actividades, 1, "General de la base", "Supervisión de la sala de control", "12:30")

print("Operaciones cargadas inicialmente en la cola de prioridad:")
for actividad in cola_actividades:
    print(actividad)

print("\n--- Iniciando atención de actividades ---\n")

for i in range(5):
    atender_actividad(cola_actividades)

agregar_actividad(cola_actividades, 2, "Capitán Phasma", "Revisión de intrusos en el hangar B7", "13:00", 25)
print("\nSe ha agregado la operación de Capitán Phasma para revisión de intrusos en el hangar B7.")

atender_actividad(cola_actividades)

agregar_actividad(cola_actividades, 3, "Líder Supremo Snoke", "Destruir el planeta Takodana", "13:30")
print("\nSe ha agregado la operación de Líder Supremo Snoke para destruir el planeta Takodana.")

while cola_actividades:
    atender_actividad(cola_actividades)

print("\n--- Todas las actividades han sido atendidas ---")

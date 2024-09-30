from collections import deque
class StarWarsQueue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, nombre, planeta):
        self.queue.append({'nombre': nombre, 'planeta': planeta})
    def mostrar_personajes_por_planeta(self, planetas):
        print(f"Personajes de {', '.join(planetas)}:")
        for personaje in self.queue:
            if personaje['planeta'] in planetas:
                print(f"{personaje['nombre']} del planeta {personaje['planeta']}")
    def planeta_natal(self, nombres):
        for personaje in self.queue:
            if personaje['nombre'] in nombres:
                print(f"{personaje['nombre']} es del planeta {personaje['planeta']}")
    def insertar_antes_de_yoda(self, nombre, planeta):
        nueva_cola = deque()
        yoda_encontrado = False
        for personaje in self.queue:
            if personaje['nombre'] == 'Yoda' and not yoda_encontrado:
                nueva_cola.append({'nombre': nombre, 'planeta': planeta})
                yoda_encontrado = True
            nueva_cola.append(personaje)
        self.queue = nueva_cola
    def eliminar_despues_de_jarjar(self):
        nueva_cola = deque()
        eliminar_siguiente = False
        for personaje in self.queue:
            if eliminar_siguiente:
                eliminar_siguiente = False
                continue
            nueva_cola.append(personaje)
            if personaje['nombre'] == 'Jar Jar Binks':
                eliminar_siguiente = True
        self.queue = nueva_cola
    def mostrar_cola(self):
        for personaje in self.queue:
            print(f"{personaje['nombre']} del planeta {personaje['planeta']}")
cola = StarWarsQueue()
cola.enqueue("Luke Skywalker", "Tatooine")
cola.enqueue("Han Solo", "Corellia")
cola.enqueue("Leia Organa", "Alderaan")
cola.enqueue("Yoda", "Dagobah")
cola.enqueue("Jar Jar Binks", "Naboo")
cola.enqueue("Chewbacca", "Kashyyyk")
cola.mostrar_personajes_por_planeta(["Alderaan", "Endor", "Tatooine"])
cola.planeta_natal(["Luke Skywalker", "Han Solo"])
cola.insertar_antes_de_yoda("Obi-Wan Kenobi", "Stewjon")
print("\nCola después de insertar a Obi-Wan Kenobi antes de Yoda:")
cola.mostrar_cola()
cola.eliminar_despues_de_jarjar()
print("\nCola después de eliminar el personaje después de Jar Jar Binks:")
cola.mostrar_cola()

from collections import deque
class MCUQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, personaje, heroe, genero):
        self.queue.append({'personaje': personaje, 'heroe': heroe, 'genero': genero})

    def personaje_de_capitana_marvel(self):
        for personaje in self.queue:
            if personaje['heroe'] == 'Capitana Marvel':
                print(f"El nombre del personaje de Capitana Marvel es {personaje['personaje']}")
                return
        print("Capitana Marvel no se encuentra en la cola.")

    def mostrar_superheroes_femeninos(self):
        print("Superhéroes femeninos:")
        for personaje in self.queue:
            if personaje['genero'] == 'F':
                print(f"{personaje['heroe']} ({personaje['personaje']})")

    def mostrar_personajes_masculinos(self):
        print("Personajes masculinos:")
        for personaje in self.queue:
            if personaje['genero'] == 'M':
                print(f"{personaje['personaje']} ({personaje['heroe']})")

    def superheroe_de_scott_lang(self):
        for personaje in self.queue:
            if personaje['personaje'] == 'Scott Lang':
                print(f"El superhéroe de Scott Lang es {personaje['heroe']}")
                return
        print("Scott Lang no se encuentra en la cola.")

    def mostrar_personajes_con_s(self):
        print("Personajes o superhéroes cuyos nombres comienzan con S:")
        for personaje in self.queue:
            if personaje['personaje'].startswith('S') or personaje['heroe'].startswith('S'):
                print(f"{personaje['personaje']} es {personaje['heroe']} ({personaje['genero']})")

    def buscar_carol_danvers(self):
        for personaje in self.queue:
            if personaje['personaje'] == 'Carol Danvers':
                print(f"Carol Danvers es {personaje['heroe']}")
                return
        print("Carol Danvers no se encuentra en la cola.")
    def mostrar_cola(self):
        for personaje in self.queue:
            print(f"{personaje['personaje']} es {personaje['heroe']} ({personaje['genero']})")


cola = MCUQueue()


cola.enqueue("Tony Stark", "Iron Man", "M")
cola.enqueue("Steve Rogers", "Capitán América", "M")
cola.enqueue("Natasha Romanoff", "Black Widow", "F")
cola.enqueue("Carol Danvers", "Capitana Marvel", "F")
cola.enqueue("Scott Lang", "Ant-Man", "M")
cola.enqueue("Peter Parker", "Spider-Man", "M")
cola.enqueue("Wanda Maximoff", "Scarlet Witch", "F")

# a
cola.personaje_de_capitana_marvel()

# b) 
cola.mostrar_superheroes_femeninos()

# c) 
cola.mostrar_personajes_masculinos()

# d)
cola.superheroe_de_scott_lang()

# e)
cola.mostrar_personajes_con_s()

# f)
cola.buscar_carol_danvers()

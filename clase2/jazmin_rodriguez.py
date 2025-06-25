

class Mascota:
    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre
        
    def dueño(self, nombre):
        print(f"El dueñ@ de {self.nombre} es {nombre}")
        print("El dueñ@ de ", self.nombre ," es " , nombre)

class Perro(Mascota):

    def hablar(self):
        print(f"{self.nombre} es perro y ladra")
        
    def acciones(self):
        print(f"{self.nombre} mueve la cola")
        
class Gato(Mascota):
        
    def hablar(self):
        print(f"{self.nombre} dice miau")
        
    def acciones(self):
        print(f"{self.nombre} trepa a los arbol")



if __name__ == "__main__":
    Campito = Perro("Canino", "Campito")
    Campito.dueño("Nicolas")
    Campito.hablar()
    firulais = Perro("Canino", "Firulais")
    firulais.hablar()
    firulais.acciones()
    lulu = Gato("Felino", "lulu")
    lulu.hablar()
    lulu.dueño("Maria")
    lulu.acciones()
        
    
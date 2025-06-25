# Definición de una clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear objetos
persona1 = Persona("Jazmin", 28)
persona1.saludar()

# Atributos públicos
print(persona1.nombre)

# ---------------------------
# Encapsulamiento
# ---------------------------

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    def ver_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

cuenta = CuentaBancaria("Iván", 100)
cuenta.depositar(50)
print("Saldo actual:", cuenta.ver_saldo())

# ---------------------------
# Herencia
# ---------------------------

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

perro = Perro("Firulais")
gato = Gato("Michi")

perro.hablar()  # Guau!
gato.hablar()   # Miau!

# ---------------------------
# Polimorfismo
# ---------------------------

def hacer_hablar(animal):
    animal.hablar()

hacer_hablar(perro)
hacer_hablar(gato)

# ---------------------------
# isinstance y super()
# ---------------------------

print(isinstance(perro, Animal))  # True

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def saludar(self):
        print(f"Soy {self.nombre}, estudiante de {self.carrera}")

estudiante1 = Estudiante("Luis", 22, "Ingeniería")
estudiante1.saludar()
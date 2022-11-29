import pickle
import os


class Vehiculo:
    tipo = ""
    ruedas = 0
    puertas = 0
    marca = ""
    modelo = ""
    
    def __init__(self, tipo, ruedas, puertas, marca, modelo):
        self.tipo = tipo
        self.ruedas = ruedas
        self.puertas = puertas
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f'Tipo {self.tipo}, con {self.puertas} puertas'
    
    def getMarcaModelo(self):
        return self.marca , self.modelo
    
    

c1 = Vehiculo("coche", 4, 5, "Ford", "Focus")
m1 = Vehiculo("moto", 2, 0, "BMW", "C111")

print(c1.getMarcaModelo())

f = open('data.bin', 'wb')
pickle.dump(c1, f)
f.close()

f = open('data.bin', 'rb')
coche = pickle.load(f)
f.close()

print(str(coche))
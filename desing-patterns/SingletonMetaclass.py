class SingletonMeta(type):
    # Registro de todas las clases Singleton existentes
    _instances = {}
    def __call__(cls, *args, **kwargs):
        # Logica encargada de crear el Sinlgeton
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DbConnection_Singleton(metaclass=SingletonMeta):
    # Funciones y atributos que contendra nuestra clase Singleton
    def createConnection(self):
        return 

# Hay tres maneras de implementar singleton en python:
# 1. Por medio de una clase base
# 2. Haciendo uso de decoradores
# 3. Implementando metaclases
# Parar esta tarea implemntara metaclases dado que es el unico que no he hecho antes...

s1 = DbConnection_Singleton()
s2 = DbConnection_Singleton()

print("Con Singleton: ")
if id(s1) == id(s2):
    print(">    El Singleton funciono, ambas variables hacen referencia a la misma instance.")
else:
    print(">    El Singleton fallo, las variables referencias diferentes instancias.")

# Clase DbConnection sin funcionalidad Singleton
class DbConnection_NonSingleton():
    def createConnection(self):
        return 

s1 = DbConnection_NonSingleton()
s2 = DbConnection_NonSingleton()

print("Sin Singleton: ")
if id(s1) == id(s2):
    print(">    El Singleton funciono, ambas variables hacen referencia a la misma instance.")
else:
    print(">    El Singleton fallo, las variables referencias diferentes instancias.")


# P: ¿La clase a la que implementaste el patrón Singletón le es útil?
# R: Si, sus propiedades del Singleton permiten que sus valores y funciones
#    sean gloables a traves de toda la aplicación y centralizar el trabajo.
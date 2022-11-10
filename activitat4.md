# Enunciat:

Seguim amb la pràctica.

Python:

Anem a ordenar el codi, quan creem el nostre CRUD l'hem de fer de forma modular, reaprofitant codi i fent funcions senzilles, curtes i fàcils de mantenir.

### Exemple de CRUD:

Des del nostre fitxer principal cridem a la funció 

```
from backend import crudLocalizaciones


if __name__ == '__main__':
    while True:
        crudLocalizaciones()
```

i al nostre fitxer CRUD (que estarà segurament a backend.py):

```
def crudLocalizaciones():
    menuLocalizaciones()

def menuLocalizaciones():
    while True:
        print("OPCIONES:\n")
        print("1.- Mostrar localización")
        print("2.- Crear localización")
        print("3.- Modificar localización")
        print("4.- Listar localización")
        print("5.- Eliminar localización")
        print("6.- Volver")
        opcion = input("?")
        if (opcion == "1"):
            loc = input("¿Qué localización mostrar?")
            mostrarLocalizacion(loc)
        if (opcion == "2"):        
            crearLocalizacion(loc)
        if (opcion == "3"):
            loc = input("¿Qué localización modificar?")
            modificarLocalizacion(loc)            
        if (opcion == "4"):
            listarLocalizaciones()
        if (opcion == "5"):
            loc = input("¿Qué localización eliminar?")
            eliminarLocalizacion(loc)
        if (opcion == "6"):
            break
```

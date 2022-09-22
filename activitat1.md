# Activitat 1:

Aquesta activitat s'entregarà per GitHub, en un document MarkDown anomenat **activitat1.md**, i anirà per fases, totes elles dins el mateix document final.

Cada pas que feu l'heu de documentar dins del document amb text i captures de pantalla adients.

## Fase 0: 

- Tenir instal·lats PostgreSQL i Python.

## Fase 1:

- Entrar al gestor de Postgre:

```
sudo -u postgres psql
```


- Crear una base de dades anomenada: UF4XYZ, on Z, Y i Z són les teves inicials.

```
CREATE DATABASE UF4XYZ;
```

- Crear una taula anomenada estatsXYZ, on Z, Y i Z són les teves inicials, amb els camps següents.
  - id: nombre sencer, clau primària, autoincrementable.
  - nom: text.
  - superficie: nombre sencer.

- Afegir a la base de dades estatsXYZ els [estats de EEUU](https://www.sport-histoire.fr/es/Geografia/Lista_estados_estados_unidos.php).


- Crear una taula anomenada ciutatsXYZ, on Z, Y i Z són les teves inicials, amb els camps següents.
  - id: nombre sencer, clau primària, autoincrementable.   
  - nom: text.
  - habitants: nombre sencer.
  - estat: nombre sencer, clau forànea (Taula estats, camp id).

- Afegir a la taula ciutatsXYZ els registres de les [30 ciutats més poblades dels EEUU](https://libretilla.com/ciudades-mas-grandes-estados-unidos/). 

# Activitat 1:

Aquesta activitat s'entregarà per GitHub, en un document MarkDown anomenat **activitat1.md**, i anirà per fases, totes elles dins el mateix document final.

Cada pas que feu l'heu de documentar dins del document amb text i captures de pantalla adients.

## Fase 0: Instal·lació.

- Tenir instal·lats PostgreSQL i Python.

## Fase 1: Crear taules i inserir dades.

- Entrar al gestor de Postgre:

```
sudo -u postgres psql
```


- Crear una base de dades anomenada: UF4XYZ, on X, Y i Z són les teves inicials.

```
CREATE DATABASE UF4XYZ;
```

- Crear una taula anomenada estatsXYZ, on X, Y i Z són les teves inicials, amb els camps següents.
  - id: nombre sencer, clau primària, autoincrementable.
  - nom: text.
  - superficie: nombre sencer.

- Afegir a la base de dades estatsXYZ els [estats de EEUU](https://www.sport-histoire.fr/es/Geografia/Lista_estados_estados_unidos.php).


- Crear una taula anomenada ciutatsXYZ, on X, Y i Z són les teves inicials, amb els camps següents.
  - id: nombre sencer, clau primària, autoincrementable.   
  - nom: text.
  - habitants: nombre sencer.
  - estat: nombre sencer, clau forànea (Taula estats, camp id).

- Afegir a la taula ciutatsXYZ els registres de les [30 ciutats més poblades dels EEUU](https://libretilla.com/ciudades-mas-grandes-estados-unidos/).

- Mostreu exemples de la creació de les taules i l'entrada de registres.
- Feu un llistat on es vegi la informació entrada.
- Connecteu amb la bbdd des de Python i mostreu les següents respostes, afegint la Query:
  - Tots els estats amb una superfície més gran que 200.000 Km2.
  - Tots els estats amb una superfície més petita que 100.000 Km2 i més gran que 20.000 Km2.
  - Totes les ciutats amb més de 1.000.000 d'habitants.
  - Totes les ciutats amb menys de 1.000.000 d'habitants i més de 650.000 habitants.

## Fase 2: 

- Fes una copia de seguretat de la bbdd UF4XYZ al fitxer UF4XYZ.sql seguint la [DOCUMENTACIÓ OFICIAL](https://www.postgresql.org/docs/current/app-pgdump.html).

- Comprova que la bbdd de dades funciona restaurant-la com a UF4XYZ-copia.

- Comproveu que estan els registres de ciutats i estats a UF4XYZ-copia.

- Elimineu la bbdd UF4XYZ-copia.

- Elimineu de la taula estatsXYZ tots els estats que comencin per una lletra a la vostra elecció (i que fent-ho esborri almenys un registre).

- Elimineu de la taule estatsXYZ tots els estats que tinguin una superfície inferior a 100.000 Km2.

- Elimineu la taula estatsXYZ.

- Altereu la taula ciutatsXYZ afegint un camp que es digui atacsDeGodzilla i sigui de tipus sencer. El valor del camp serà 0.

- Feu un programa que crei un número aleatori de 0 a 1 en Python [tuto](https://dungeonofbits.com/conectar-con-una-base-de-datos-postgresql-desde-python.html).

- Feu que el programa assigni al camp atacsDeGodzilla el valor aleatori generat. Una vegada per cada registre.

-Feu una funció de Python que esborri tots els registres ciutat amb camp atacsDeGodzilla igual a 1.

-Elimineu la bbdd copia.

- Restabliu la bbdd UF4XYZ.




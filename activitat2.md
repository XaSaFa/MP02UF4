# Enunciat

En aquesta pràctica farem un programa de Python que es connectarà a la nostra bbdd de PostgreSQL.

## Fase 0:

### PostgreSQL:

Creem una taula anomenada localitzacions, aquesta taula tindrè com a camps mínims:

- id
- nom
- descripció

Sobre aquesta base anirem ampliant.

### Python:

Creem un programa que es connecta a la bbdd i que al rebre una id de localització busca a la taula localitzacions i ens mostra la descripció de la localització.

Farem que la descripció d'una localització es vegi en color blau. (mira com fer-ho [aqui](https://linuxhint.com/print-colored-text-python/)).

---------------------------------------------------------------------------------------------------------------------------------------

## Fase 1:

### PostgreSQL:

Creem una taula **camins**, aquesta taula significa un camí d'una localització a una altra, per tant podem fer que tingui:

- id de localització origen.
- id de localització destí.
- descripció: Què mostra el programa quan passem de l'origen al destí.

També crearem una taula **jugadors** per a guardar el progrés d'un jugador.

- nom jugador.
- contrasenya partida.
- localització actual.

Aquesta taula ha de guardar, de moment, la localització actual del jugador identificat per un nom de jugador i la seva contrasenya.

El joc ha de tenir una localització per defecte que serà la localització de sortida quan comença un joc nou.

### Python:

Al programa anterior, que anomenarem **backend.py**, crearem un **CRUD** de localitzacions.

El CRUD permet:

- Mostrar una localització.
- Crear una localització.
- Modificar una localització.
- Eliminar una localització.
- Llistar totes les localitzacions.

Creem un programa nou, aquest programa es dirà **adventure.py** i és el programa de joc.

El programa tindrà la opció de crear una nova partida, en aquest cas pregunta nom d'usuari i contrasenya.

També es podrà continuar una partida, llavors el nostre programa de joc ens pregunta el nom del jugador i la seva contrasenya, si no existeix o la contrasenya és incorrecta avisa a l'usuari/a. 

Si el jugador i la contrasenya són correctes el joc comença des de la localització on estava el jugador en aquell moment.

També ens deixa sortir del programa.





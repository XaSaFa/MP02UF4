# Enunciat

En aquesta pràctica **AMPLIAREM** el programa de Python adventure que vam començar a l'activitat 2.

## Fase 0:

### PostgreSQL:

Utilitzarem la directiva ALTER TABLE per fer uns canvis a la bbdd.

La taula localitzacions quedarà així:

**id**

nom

descripció

La taula camins quedarà així:

**idOrigen**, id de localització origen. (1 - que és del vestíbol planta baixa).
**idDestí**, de localització destí. (2 - que és del vestíbul primera planta)
nomOrigen, nom que rep la sortida vista a id origen. (Escales de pujada a la primera planta).
nomDestí, nom que rep la sortida vista a id destí. (Escales de baixada a la planta baixa).

**PREGUNTES**

1. Adjunta les comandes utilitzades per canviar la taula localitzacions.
2. Adjunta les comandes utilitzades per canviar la taula camins.

### Python:

#### Modificar el CRUD:

Primer modificarem el CRUD de localitzacions.

#### Moure el personatge:

Introduïm mínim dues localitzacions (la de sortida de joc i una altra) que estiguin comunicades per provar el moviment del personatge entre localitzacions.

Quan un personatge **entri a una localització** o escrigui la paraula **MIRAR** al programa el programa mostra:

- En color BLAU: el nom de la localització i la descripció, agafades de la taula localitzacions.
- En color LILA: el nom corresponent a les sortides que sortin des de la localització actual.

Quan un personatge escrigui les paraules **ANAR X** el programa buscará si a la localització actual hi ha el nom X com nom de sortida.

- De NO existir el nom a la localització actual es mostrarà un missatge d'error del estil: "No es pot anar a X.". 
- D'existir:
  - El programa mourà al personatge a la localització destí modificant la taula **jugadors**.
  - Es mostrarà nom, descripció i sortides de la localització actual.

**PREGUNTES**

3. Posa el codi de creació d'el registre a la taula camins que crea el camí entre les dues localitzacions.
4. Posa el codi de cerca a la taula camins per trobar els camins posibles de sortida d'una localització.

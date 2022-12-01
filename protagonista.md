# Protagonista:

Encara que només tindrem un protagonista l'haurem de guardar a la bbdd a la seva propia taula.

El protagonista de la aventura tindrà una serie de característiques personalitzables per l'usuari/a del joc.

- Nom. Serà el nom del protagonista.
- Descripció. Text descriptiu del personatge.
- Sexe. Podrem escollir entre: masculí, femení, altres.
- Edat. Els anys que té el/la protagonista de 18 a 99.
- Altura. Alçada del protagonista.
- Pes: Kg que pesa el personatge.
- FOR. Força del personatge. (de 1 a 20).
- DES. Destresa del personatge.(de 1 a 20).
- RES. Resistència del personatge.(de 1 a 20).
- Salut. Punts de vida del personatge. És igual a la RES. del personatge x 2.
- Potser ens hem deixat algo?

**Restriccions**: Les numèriques d'edat, for, des i res.

# Inventari:

La taula inventari és el conjunt d'objectes que poseeix el personatge protagonista.

_Quines alternatives tenim per implementar l'inventari?_ 

**Restricció des de l'aplicació**: El protagonista mai podrà tenir a inventari objectes amb un pes combinat superior a la seva FOR.

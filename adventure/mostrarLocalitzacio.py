import psycopg2
from config import config

colores = {
    "normal":"\033[0;0m",
    "azul":"\033[1;34;40m",
    "lila":"\033[1;35;40m"
}

def connect(sentenciaSQL):
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sentenciaSQL)
        return (cur)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            conn.close()

def mostrarLocalizacion(idLocalizacion):
    cur = connect('SELECT nombre,descripcion FROM localizaciones WHERE id = '+ idLocalizacion)
    respuesta = cur.fetchone()
    #print("\033[1;34;40m"+respuesta[0]+"\033[0;0m")
    print(colores["lila"] +"Localización: " + respuesta[0] + colores["normal"])
    print(colores["azul"] + "Descripción: " + respuesta[1] + colores["normal"] )
    cur.close()

if __name__ == '__main__':
    while True:
        localizacion = input("¿Qué localización mostrar?")
        mostrarLocalizacion(localizacion)

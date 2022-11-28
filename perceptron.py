import Conexion

def actualizarPokemon(cursor,conexion,sumatoria,pokemon,respuestas):
    nuevoValor = (sumatoria+pokemon["valor"])/2
    try:
        cursor.execute("update aprendizaje set color = {} where id = {}".format(respuestas[0],pokemon["id"]))
        conexion.commit()
    except:
        print("Error al actualizar el color")
    try:
        cursor.execute("update aprendizaje set tamanio = {} where id = {}".format(respuestas[1],pokemon["id"]))
        conexion.commit()
    except:
        print("Error al actualizar el tamanio")
    try:
        cursor.execute("update aprendizaje set tipo = {} where id = {}".format(respuestas[2],pokemon["id"]))
        conexion.commit()
    except:
        print("Error al actualizar el tipo")
    try:
        cursor.execute("update aprendizaje set caracteristica1 = {} where id = {}".format(respuestas[3],pokemon["id"]))
        conexion.commit()
    except:
        pass
    try:
        cursor.execute("update aprendizaje set caracteristica2 = {} where id = {}".format(respuestas[4],pokemon["id"]))
        conexion.commit()
    except:
        pass
    try:
        cursor.execute("update aprendizaje set caracteristica3 = {} where id = {}".format(respuestas[5],pokemon["id"]))
        conexion.commit()
    except:
        pass
    try:
        cursor.execute("update aprendizaje set caracteristica4 = {} where id = {}".format(respuestas[6],pokemon["id"]))
        conexion.commit()
    except:
        pass
    try:
        cursor.execute("update aprendizaje set caracteristica5 = {} where id  ={}".format(respuestas[7],pokemon["id"]))
        conexion.commit()
    except:
        pass
    try:
        cursor.execute("update aprendizaje set total = {} where id = {}".format(nuevoValor,pokemon["id"]))
        conexion.commit()
    except:
        print("Error al actualizar el total")

conexion = Conexion.conectar()
cursor = conexion.cursor()

"""
cursor.execute("Select number(*) from pokemon")
resultado = cursor.fetchall()
for i in resultado:
    print(i[1])"""

salir = "0"
pesoPreguntas = [1,2,3,4,5,6,7,8]

while salir != "1":
    respuestas = []
    #preguntamos el color
    print("¿Cual es el color de tu pokemon")
    cursor.execute("Select * from color")
    resultado = cursor.fetchall()
    for color in resultado:
        print(str(color[0])+".-"+color[1])
    idColor = input()
    respuestas.append(idColor)
    #preguntamos el tamanio
    print("¿Cual es el tamanio de tu pokemon")
    cursor.execute("Select * from tamanio")
    resultado = cursor.fetchall()
    for tamanio in resultado:
        print(str(tamanio[0])+".-"+tamanio[1])
    idTamanio = input()
    respuestas.append(idTamanio)
    #preguntamos el tipo
    print("¿Cual es el tipo de tu pokemon")
    cursor.execute("Select * from tipo")
    resultado = cursor.fetchall()
    for tipo in resultado:
        print(str(tipo[0])+".-"+tipo[1])
    idTipo = input()
    respuestas.append(idTipo)
    #preguntamos alguna otra caracteristica si es que la hay
    cursor.execute("Select * from caracteristica")
    preguntasExtra = cursor.fetchall()
    for pregunta in range(len(preguntasExtra)):
        print("¿Tu pokemon "+preguntasExtra[1]+"?")
        bandera = input("1.-No 2.-Si ")
        if bandera == "2":
            respuestas.append(preguntasExtra[0])
        else:
            respuestas.append(0)
    
    #hacemos la sumatoria de las entradas por los pesos
    sumatoria = 0
    for i in range(len(respuestas)):
        sumatoria += int(respuestas[i])*pesoPreguntas[i]

    #obtenemos el pokemon con el valor absoluto mas pequeño de la resta del valor en la base de datos con la salida actual
    cursor.execute("select aprendizaje.id,pokemon.pokemon,aprendizaje.total from aprendizaje inner join pokemon on pokemon.id = aprendizaje.pokemon")
    valores = cursor.fetchall()
    pokemon = {"id":"","nombre":"","valor":0}
    menor = 1000
    for i in range(len(valores)):
        if menor > abs(sumatoria-int(valores[i][2])):
            menor = abs(sumatoria-int(valores[i][2]))
            pokemon["id"]  = int(valores[i][0])
            pokemon["nombre"]  = valores[i][1]
            pokemon["valor"] = int(valores[i][2])
    #preguntamos si es correcto
    banderaCorrecto = input("¿Pensaste en el pokemon "+pokemon["nombre"]+"?\n1.-No 2.-Si\n")
    if banderaCorrecto == 2:
        #actualizamos los datos del pokemon
        actualizarPokemon(cursor,conexion,sumatoria,pokemon,respuestas)
    #creamos nuevo registro en caso de que sea uno nuevo
    else:
        nuevoNombre = input("Ingresa el nombre de tu pokemon")
        cursor.execute("select aprendizaje.id from pokemon inner join aprendizaje on aprendizaje.pokemon = pokemon.id where pokemon.pokemon = '"+nuevoNombre+"'")
        id = cursor.fetchone()
        if id != "0":
            pokemon["id"] = int(id)
            actualizarPokemon(cursor,conexion,sumatoria,pokemon,respuestas)
        else: 
            try:
                cursor.execute("insert into pokemon(pokemon)values('"+nuevoNombre+"')")
                conexion.commit()
                cursor.execute("select id from pokemon order by id desc limit 1")
                id = cursor.fetchone()[0]
                cursor.execute("insert into aprendizaje(color,tamanio,tipo,pokemon)values({},{},{},{})".format(respuestas[0],respuestas[1],respuestas[2],id))
                conexion.commit()
                cursor.execute("select id from aprendizaje order by id desc limit 1")
                id = cursor.fetchone()[0]
                pokemon["id"] = int(id)
                pokemon["valor"] = sumatoria
                actualizarPokemon(cursor,conexion,sumatoria,pokemon,respuestas)
            except:
                print("Error al insertar nuevo pokemon")
    #preguntamos una nueva caracteristica
    if preguntasExtra <= 5:
        pass


    salir = input("Desea continuar? \n 1.-No 2.-Si ")
conexion.close()
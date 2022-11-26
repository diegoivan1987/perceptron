import Conexion

conexion = Conexion.conectar()
cursor = conexion.cursor()

"""
cursor.execute("Select number(*) from pokemon")
resultado = cursor.fetchall()
for i in resultado:
    print(i[1])"""

salir = "0"
pesoPreguntas = [1,2,1,3,3,3,3,3]

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
            respuestas.append(preguntasExtra[0])
    
    #hacemos la sumatoria de las entradas por los pesos
    sumatoria = 0
    for i in range(len(respuestas)):
        print(respuestas[i] + "*" + str(pesoPreguntas[i]))
        sumatoria += int(respuestas[i])*pesoPreguntas[i]
    print("peso {}".format(sumatoria))

    #obtenemos el pokemon con el valor absoluto mas pequeño de la resta del valor en la base de datos con la salida actual
    #preguntamos si es correcto
    #actualizamos el valor en la base de datos
    #creamos nuevo registro
    #preguntamos una nueva caracteristica


    salir = input("Desea continuar? \n 1.-No 2.-Si ")
conexion.close()
import psycopg2

try:
    conexion = psycopg2.connect(user="postgres",
                                password="Kalamar01",
                                database="nacimientos",
                                host="localhost",
                                port="5432")
    print("Conexión correcta!")
    
    sql1 = """select *
         from madre
         ORDER BY 1;"""

    sql2 = """select *
         from padre
         ORDER BY 1;"""

    sql3 = """select *
         from bebe
         ORDER BY 1;"""
    

 #Se ejecuta la sentencia para mostrar los registros de la tabla madre
    cursor = conexion.cursor()
    cursor.execute(sql1)
    madres = cursor.fetchall()
    print("****tabla madre***")
    for madre in madres:
        print(f"id_madre: {madre[0]}")
        print(f"edad_madre: {madre[1]}")
        print(f"embarazos: {madre[2]}")
        print(f"hijos_vivos: {madre[3]}","\n") 

#Se ejecuta la sentencia para mostrar los registros de la tabla padre 
    """ cursor = conexion.cursor()
    cursor.execute(sql2)
    padres = cursor.fetchall()
    print("****tabla padre***")
    for padre in padres:
        print(f"id_padre: {padre[0]}")
        print(f"edad_padre: {padre[1]}","\n")  """
        

#Se ejecuta la sentencia para mostrar los registros de la tabla bebe 

    """ cursor = conexion.cursor()
    cursor.execute(sql3)
    bebes = cursor.fetchall()
    print("****tabla bebe***")
    for bebe in bebes:
        print(f"id_bebe: {bebe[0]}")
        print(f"genero: {bebe[1]}")
        print(f"peso: {bebe[2]}")
        print(f"talla: {bebe[3]}")
        print(f"fecha_nacimiento: {bebe[4]}")
        print(f"tiempo_gestacion: {bebe[5]}")
        print(f"tipo_parto: {bebe[6]}")
        print(f"multiplicidad: {bebe[7]}")
        print(f"apgar1: {bebe[8]}")
        print(f"apgar2: {bebe[9]}")
        print(f"id_madre_madre: {bebe[10]}")
        print(f"id_padre_padre: {bebe[11]}") """

    
    
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)

finally:
    cursor.close()
    conexion.close()

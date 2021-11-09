import psycopg2

try:
    conexion = psycopg2.connect(user="postgres",
                                password="Kalamar01",
                                database="nacimientos",
                                host="localhost",
                                port="5432")
    print("Conexión correcta!")
    
    sql1 = """select *
         from madre;"""

    sql2 = """select *
         from padre;"""

    sql3 = """SELECT * 
         from bebe;"""
    

 #Se ejecuta la sentencia para mostrar los registros de la tabla madre y se guarda en un archivo llamado madre.txt
    
    cursor = conexion.cursor()
    cursor.execute(sql1)
    madres = cursor.fetchall()
    with open('madre.txt','w') as m:

        m.write("****tabla madre***" + "\n")

        for madre in madres:
            m.write(f"id_madre: {madre[0]}" +"\n")
            m.write(f"edad_madre: {madre[1]}" +"\n")
            m.write(f"embarazos: {madre[2]}"+"\n")
            m.write(f"hijos_vivos: {madre[3]}"+"\n") 
            m.write("\n")
    

 #Se ejecuta la sentencia para mostrar los registros de la tabla padre y se guarda en un archivo llamado padre.txt
    
    cursor = conexion.cursor()
    cursor.execute(sql2)
    padres = cursor.fetchall()

    with open('padre.txt','w') as p:

        p.write("****tabla padre***")
        p.write('\n')

        for padre in padres:
            p.write(f"id_padre: {padre[0]}"+"\n")
            p.write(f"edad_padre: {padre[1]}"+"\n")   
            p.write('\n')
        
    
#Se ejecuta la sentencia para mostrar los registros de la tabla bebe y se guarda en un archivo llamado bebe.txt
    
    cursor = conexion.cursor()
    cursor.execute(sql3)
    bebes = cursor.fetchall()

    with open('bebe.txt','w') as d:

        d.write("tabla bebe")
        d.write('\n')
  
        for bebe in bebes:
            d.write(f"id_bebe:  {bebe[0]}" + "\n")
            d.write(f"genero: {bebe[1]}"+ "\n")
            d.write(f"peso: {bebe[2]}"+ "\n")
            d.write(f"talla: {bebe[3]}"+ "\n")
            d.write(f"fecha_nacimiento: {bebe[4]}"+ "\n")
            d.write(f"tiempo_gestacion: {bebe[5]}"+ "\n")
            d.write(f"tipo_parto: {bebe[6]}"+ "\n")
            d.write(f"multiplicidad: {bebe[7]}"+ "\n")
            d.write(f"apgar1: {bebe[8]}"+ "\n")
            d.write(f"apgar2: {bebe[9]}"+ "\n")
            d.write(f"id_madre_madre: {bebe[10]}"+ "\n")
            d.write(f"id_padre_padre: {bebe[11]}"+"\n")
            d.write("\n")
        
    
    
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)

finally:
    cursor.close()
    conexion.close()

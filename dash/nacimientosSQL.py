# grafica general para semanas de gestacion
def promediogestacionG():
    return """select genero, tiempo_gestacion as semana, count(*) as total
              from bebe
              group by genero,tiempo_gestacion
			  order by 2"""

def promediogestacionM():
    return """select tiempo_gestacion as semanas, count(*) as total
              from bebe 
              where genero = 'MASCULINO'
              group by tiempo_gestacion"""

def promediogestacionF():
    return """select tiempo_gestacion as semanas, count(*) as total
              from bebe 
              where genero = 'FEMENINO'
              group by tiempo_gestacion"""

def extprematuro():
    return """SELECT tiempo_gestacion as semanas, count(*) as total
           FROM bebe 
           WHERE tiempo_gestacion BETWEEN 23 AND 28
           group by tiempo_gestacion"""

def modprematuros():
    return """SELECT tiempo_gestacion as semanas, count(*) as total
           FROM bebe 
           WHERE tiempo_gestacion BETWEEN 29 AND 33
           group by tiempo_gestacion"""


           

def tardios():
    return """SELECT tiempo_gestacion as semanas, count(*) as total
           FROM bebe 
           WHERE tiempo_gestacion BETWEEN 34 AND 37
           group by tiempo_gestacion"""

# Peso bebes

def PesoGeneral():
    return """SELECT avg(peso) as promedio, multiplicidad
              FROM bebe
              GROUP BY  
              multiplicidad"""
              
def NormalPesoBebe():
    return """SELECT  count(peso) as cantidad, multiplicidad
            FROM bebe
            WHERE peso BETWEEN 2500 AND 4500
			GROUP BY
			multiplicidad"""

def BajoPeso():
    return """SELECT count(peso) as cantidad, multiplicidad
            FROM bebe
            WHERE peso < 2500
            GROUP BY
			multiplicidad"""

def SobrePeso():
    return """SELECT count(peso) as cantidad, multiplicidad
            FROM bebe
            WHERE peso > 4500
            GROUP BY
            multiplicidad"""
#talla
def TallaGeneral():
    return """SELECT avg(talla) as promedio, multiplicidad
              FROM bebe
              GROUP BY  
              multiplicidad"""

def NormalTallaBebe():
    return """SELECT  count(talla) as cantidad, multiplicidad
            FROM bebe
            WHERE talla BETWEEN 45 AND 47
			GROUP BY
			multiplicidad"""


def talla_grande():
    return """SELECT count(talla) as cantidad, multiplicidad
            FROM bebe
            WHERE talla > 47
            GROUP BY
            multiplicidad"""


def talla_pequeña():
    return """SELECT count(talla) as cantidad, multiplicidad
            FROM bebe
            WHERE talla < 45
            GROUP BY
            multiplicidad"""
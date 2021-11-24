import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import nacimientosSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# SEMANAS DE GESTACION GENERAL
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.promediogestacionG(), con.connection)
con.closeConnection()

dfgestacionGENERAL = pd.DataFrame(query, columns=["genero","semana","total"])

# Grafico barras
figBargeneral = px.bar(dfgestacionGENERAL.head(20), x="semana", y="total",color="genero")
# Grafico pie
figPiegeneral = px.pie(dfgestacionGENERAL.head(20), names="semana", values="total")


# SEMANAS (MASCULINO)
con = Connection()
con.openConnection()
query1 = pd.read_sql_query(sql.promediogestacionM(), con.connection)
con.closeConnection()

dfCasesgestacion2 = pd.DataFrame(query1, columns=["semanas","total"])

# Grafico barras
figBarmasculino = px.bar(dfCasesgestacion2.head(20), x="semanas", y="total",color_discrete_sequence =['blue']*len(dfCasesgestacion2),)

# Grafico pie
figPiemasculino = px.pie(dfCasesgestacion2.head(20), names="semanas", values="total")

# SEMANAS (FEMENINO)
con = Connection()
con.openConnection()
query2 = pd.read_sql_query(sql.promediogestacionF(), con.connection)
con.closeConnection()

dfCasesgestacion2 = pd.DataFrame(query2, columns=["semanas","total"])

# Grafico barras
figBarfemenino = px.bar(dfCasesgestacion2.head(20), x="semanas", y="total",color_discrete_sequence =['pink']*len(dfCasesgestacion2),)

# Grafico pie
figPiefemenino = px.pie(dfCasesgestacion2.head(20), names="semanas", values="total")



# RANGOS DE PREMATURIEDAD

#// extremadamente prematuro
con = Connection()
con.openConnection()
query3 = pd.read_sql_query(sql.extprematuro(), con.connection)
con.closeConnection()

dfCasesgestacion3 = pd.DataFrame(query3, columns=["semanas","total"])

# Grafico barras
figextprematuro = px.bar(dfCasesgestacion3.head(20), x="semanas", y="total",color_discrete_sequence =['red']*len(dfCasesgestacion3),)

#// moderamente prematuro

con = Connection()
con.openConnection()
query4 = pd.read_sql_query(sql.modprematuros(), con.connection)
con.closeConnection()

dfCasesgestacion4 = pd.DataFrame(query4, columns=["semanas","total"])

# Grafico barras
figmodprematuro = px.bar(dfCasesgestacion4.head(20), x="semanas", y="total",color_discrete_sequence =['orange']*len(dfCasesgestacion4),)


#// tardios 

con = Connection()
con.openConnection()
query5 = pd.read_sql_query(sql.tardios(), con.connection)
con.closeConnection()

dfCasesgestacion5 = pd.DataFrame(query5, columns=["semanas","total"])

# Grafico barras
figtardios = px.bar(dfCasesgestacion5.head(20), x="semanas", y="total",color_discrete_sequence =['green']*len(dfCasesgestacion5),)


#--------------------------------------------------------------------------------------------------
# PESO BEBE:
con.openConnection()
query6 = pd.read_sql_query(sql.PesoGeneral(), con.connection)
con.closeConnection()

dfpeso_general = pd.DataFrame(query6, columns=["multiplicidad", "promedio"])
# Grafico torta
figPiePesoGeneral = px.pie(dfpeso_general.head(20), names="multiplicidad", values="promedio")
# Grafico linea
figlinePesoGeneral = px.line(dfpeso_general.head(20), x="multiplicidad", y="promedio")

# PESO NORMAL BEBE
con.openConnection()
query7 = pd.read_sql_query(sql.NormalPesoBebe(), con.connection)
con.closeConnection()

dfpeso_normal = pd.DataFrame(query7, columns=["multiplicidad", "cantidad"])
# Grafico pie
figPieNormalPeso = px.pie(dfpeso_normal.head(20), names="multiplicidad", values="cantidad")
# Grafico barra
figBarNormalPeso = px.bar(dfpeso_normal.head(20), x="multiplicidad", y="cantidad")

# BEBE BAJO DE PESO
con.openConnection()
query8 = pd.read_sql_query(sql.BajoPeso(), con.connection)
con.closeConnection()
 
dfpeso_bajo = pd.DataFrame(query8, columns=["multiplicidad", "cantidad"])

# Grafico barra
figBarBajoPeso = px.bar(dfpeso_bajo.head(20), x="multiplicidad", y="cantidad")
# Grafico torta
figPieBajoPeso = px.pie(dfpeso_bajo.head(20), names="multiplicidad", values="cantidad")
# Grafico linea
figLineBajoPeso = px.line(dfpeso_bajo.head(20), x="multiplicidad", y="cantidad")


# BEBE CON SOBREPESO
con.openConnection()
query9 = pd.read_sql_query(sql.BajoPeso(), con.connection)
con.closeConnection()

dfsobre_peso = pd.DataFrame(query9, columns=["multiplicidad", "cantidad"])

# Grafico barra
figBarSobre = px.bar(dfsobre_peso.head(20), x="multiplicidad", y="cantidad")
# Grafico pie
figPieSobre = px.pie(dfsobre_peso.head(20), names="multiplicidad", values="cantidad")

#--------------------------------------------------------------------------------------------------
# talla BEBE:
con.openConnection()
query6 = pd.read_sql_query(sql.TallaGeneral(), con.connection)
con.closeConnection()

dfTalla_general = pd.DataFrame(query6, columns=["multiplicidad", "promedio"])
# Grafico torta
figPieTallaGeneral = px.pie(dfpeso_general.head(20), names="multiplicidad", values="promedio")
# Grafico linea
figlineTallaGeneral = px.line(dfpeso_general.head(20), x="multiplicidad", y="promedio")

# Talla NORMAL BEBE
con.openConnection()
query7 = pd.read_sql_query(sql.NormalTallaBebe(), con.connection)
con.closeConnection()

dfTalla_normal = pd.DataFrame(query7, columns=["multiplicidad", "cantidad"])
# Grafico pie
figPieNormalTalla = px.pie(dfTalla_normal.head(20), names="multiplicidad", values="cantidad")
# Grafico barra
figBarNormalTalla = px.bar(dfTalla_normal.head(20), x="multiplicidad", y="cantidad")

# BEBE talla baja
con.openConnection()
query8 = pd.read_sql_query(sql.talla_pequeña(), con.connection)
con.closeConnection()
 
dftalla_pequeña = pd.DataFrame(query8, columns=["multiplicidad", "cantidad"])

# Grafico barra
figBartalla_pequeña = px.bar(dftalla_pequeña.head(20), x="multiplicidad", y="cantidad")
# Grafico torta
figPietalla_pequeña= px.pie(dftalla_pequeña.head(20), names="multiplicidad", values="cantidad")
# Grafico linea
figLinetalla_pequeña = px.line(dftalla_pequeña.head(20), x="multiplicidad", y="cantidad")


# BEBE talla grande
con.openConnection()
query9 = pd.read_sql_query(sql.talla_grande(), con.connection)
con.closeConnection()

dftalla_grande = pd.DataFrame(query9, columns=["multiplicidad", "cantidad"])

# Grafico barra
figBartalla_grande = px.bar(dftalla_grande.head(20), x="multiplicidad", y="cantidad")
# Grafico pie
figPietalla_grande = px.pie(dftalla_grande.head(20), names="multiplicidad", values="cantidad")



# Layout 
app.layout = html.Div(children=[
    html.H1(children='Dashboard Nacimientos'),
    html.H2(children='Semanas de gestacion unificado (Barras)'),
    dcc.Graph(
        id='bargestaciongeneral',
        figure=figBargeneral
    ),
    html.H2(children='Semanas de gestacion unificado (Pastel)'),
    dcc.Graph(
        id='piegestaciongeneral',
        figure=figPiegeneral
    ),  
    html.H1(children='Nacimientos por semana (Masculino)'),
    html.H2(children='Barras'),
    dcc.Graph(
        id='bargestacionmas',
        figure=figBarmasculino
    ),
    html.H2(children='Pastel'),
    dcc.Graph(
        id='piegestacionmas',
        figure=figPiemasculino
    ),
    html.H1(children='Nacimientos por semana (Femenino)'),
    html.H2(children='Barras'),
    dcc.Graph(
        id='bargestacionfem',
        figure=figBarfemenino
    ),
    html.H2(children='Pastel'),
    dcc.Graph(
        id='piegestacionfem',
        figure=figPiefemenino
    ),

    html.H1(children='Rangos de prematuriedad'),
    html.H2(children='Rango de prematuriedad extrema (23-28 semanas)'),
    dcc.Graph(
        id='barextprem',
        figure=figextprematuro
    ),  
    html.H2(children='Rango de prematuriedad moderada (29-33 semanas)'),
    dcc.Graph(
        id='barmodprematuros',
        figure=figmodprematuro
    ),
    html.H2(children='Rango de prematuriedad tardia (34-37 semanas)'),
    dcc.Graph(
        id='bartardios',
        figure=figtardios
    ),
    html.H1(children='Pesos de los bebes (Gramos)'),
    #Peso Bebe
    html.H2(children='Promedio peso de los bebes (Torta)'),
    dcc.Graph(
        id='barpesogeneral',
        figure=figPiePesoGeneral
    ),
    html.H2(children='Promedio peso de los bebe (Linea)'),
    dcc.Graph(
        id='linepesogeneral',
        figure=figlinePesoGeneral
    ),
    html.H2(children='Bebes con indice normal de peso (Torta)'),
    dcc.Graph(
        id='tortapesonormal',
        figure=figPieNormalPeso
    ),
    html.H2(children='Bebes con indice normal de peso (Barras)'),
    dcc.Graph(
        id='barpesonormal',
        figure=figBarNormalPeso
    ),
    html.H2(children='Bebes bajos de peso (Torta)'),
    dcc.Graph(
        id='piepesobajo',
        figure=figPieBajoPeso
    ),
    html.H2(children='Bebes bajos de peso (Barra)') ,
    dcc.Graph(
        id='barpesobajo',
        figure=figBarBajoPeso
    ),
    html.H2(children='Bebes bajos de peso (Linea)'),
    dcc.Graph(
        id='linepesobajo',
        figure=figLineBajoPeso
    ),
    html.H2(children='Bebes con sobre peso (Pie)'),
    dcc.Graph(
        id='piesobrepeso',
        figure=figPieSobre
    ),
    html.H2(children='Bebes con sobre peso (Barra)'),
    dcc.Graph(
        id='barsobrepeso',
        figure=figBarSobre
    ),
    html.H1(children='talla de los bebes (cm)'),
    #tallaBebe
    html.H2(children='Promedio talla de los bebes (Torta)'),
    dcc.Graph(
        id='bartallageneral',
        figure=figPieTallaGeneral
    ),
    html.H2(children='Promedio talla de los bebe (Linea)'),
    dcc.Graph(
        id='linetallageneral',
        figure=figlineTallaGeneral
    ),
    html.H2(children='Bebes con indice normal de talla(Torta)'),
    dcc.Graph(
        id='tortatallanormal',
        figure=figPieNormalTalla
    ),
    html.H2(children='Bebes con indice normal de talla(Barras)'),
    dcc.Graph(
        id='bartallanormal',
        figure=figBarNormalTalla
    ),
    html.H2(children='Bebes pequeños de talla(Torta)'),
    dcc.Graph(
        id='pietallapequeña',
        figure=figBartalla_pequeña
    ),
    html.H2(children='Bebes pequeños de talla(Barra)') ,
    dcc.Graph(
        id='bartallapequeña',
        figure=figPietalla_pequeña
    ),
    html.H2(children='Bebes pequeños de talla(Linea)'),
    dcc.Graph(
        id='linetallapequeña',
        figure=figLinetalla_pequeña
    ),
    html.H2(children='Bebes con talla grande(Pie)'),
    dcc.Graph(
        id='piesobretalla',
        figure=figBartalla_grande
    ),
    html.H2(children='Bebes con talla grande(Barra)'),
    dcc.Graph(
        id='barsobretalla',
        figure=figPietalla_grande
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
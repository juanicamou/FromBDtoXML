# -*- coding: utf-8 -*-
import csv
from xml_creator import xmlCreator
from pretty_xml import p
from pyodbc import *
import pyodbc
import os
# Conexión a BD
conn = pyodbc.connect(
r'DRIVER={ODBC Driver 13 for SQL Server};'
r'SERVER=10.1.9.241;'
r'DATABASE=RLP-Nacimientos-Final;'
r'UID=juan;'
r'PWD=123456')
cursor = conn.cursor()

cursor.execute(u"SELECT [ID_Deleg], [TOMO], [AÑO], [CODIGOLIBRO], [Acta], [NombreInfante], [ApellidoInfante], [DNI], [idGenero], [FechaNacimiento], [PATH_IMAGE]"
            u"FROM [RLP-Nacimientos-Final].[dbo].[Lote3_Actas]"
            u"ORDER BY [CODIGOLIBRO], [Acta]"
			  )


rows = cursor.fetchall()
#def xmlCreator(circup_, tomo_, ano_, nroLibro_, actaNro_, primerNombre_, primerApellido_, tipoDoc_, nroDoc_, genero_, fechaDef_, imagePath_):
for row in rows:
    path=str(row[10])
    path=os.path.basename(path)
    nombre = str(row[5])
    nombre = nombre.encode('utf-8')
    nombre=str(nombre)
    nombre=nombre.replace("b'","")
    nombre=nombre.replace("'","")
    apellido = str(row[6])
    apellido = apellido.encode('utf-8')
    apellido=str(apellido)
    apellido=apellido.replace("b'","")
    apellido=apellido.replace("'","")
    fecha=str(row[9])
    fecha=fecha.replace(" 00:00:00","")
    tipoDNI="DNI"
    xmlCreator(str(int(row[0])), str(row[1]), str(int(row[2])), str(int(row[3])), str(int(row[4])), nombre, apellido, tipoDNI, str(int(row[7])), str(row[8]), fecha, path)

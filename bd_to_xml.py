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
r'SERVER=10.1.40.154;'
r'DATABASE=RLP-Nacimientos-Final;'
r'UID=juan;'
r'PWD=123456')
cursor = conn.cursor()
cursor.execute(u"SELECT [L].[Tomo], [L].[Año], [L].[sala], [D].[ID_Deleg], [A].[Libro], [A].[idGenero], [A].[DNI], [A].[NombreInfante], [A].[ApellidoInfante], [A].[FechaNacimiento], [A].[Acta] ,[A].[PAGE_IMAGES]"
              u"FROM [RLP-Nacimientos-Final].[dbo].[N_Redip] [A]"
              u"INNER JOIN [RLP-Nacimientos-Final].[dbo].[N_Libros] [L]"
              u"ON ([A].[Libro] = [L].[CODIGOLIBRO])"
			  u"INNER JOIN [RLP-Nacimientos-Final].[dbo].[N_Delegaciones] [D]"
			  u"ON ([D].[Delegacion] = [L].[DELEGACION])"
			  )


rows = cursor.fetchall()

for row in rows:
    #tomo_sala=StringVar()
    if (row[2] =="Z"):
        tomo_sala=row[0]
    else:
        tomo_sala= row[0] + row[2]
    #tipodoc=StringVar()
    tipodoc='DNI'
    path=str(row[11])
    path=os.path.basename(path)
    nombre = str(row[7])
    nombre = nombre.encode('utf-8')
    nombre=str(nombre)
    nombre=nombre.replace("b'","")
    nombre=nombre.replace("'","")
    apellido = str(row[8])
    apellido = apellido.encode('utf-8')
    apellido=str(apellido)
    apellido=apellido.replace("b'","")
    apellido=apellido.replace("'","")
    fecha=str(row[9])
    fecha=fecha.replace(" 00:00:00","")
    xmlCreator(str(int(row[3])), tomo_sala, str(int(row[1])), str(int(row[4])), str(int(row[10])), nombre, apellido, tipodoc, str(int(row[6])), str(row[5]), fecha, path)

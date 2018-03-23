#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyodbc import *
import pyodbc
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree, tostring
import os.path as path
import os

conn = pyodbc.connect(
r'DRIVER={ODBC Driver 11 for SQL Server};'
r'SERVER=PDECRETO-PC;'
r'DATABASE=RLP-Nacimientos-Final;'
r'UID=juan;'
r'PWD=123456')
cursor = conn.cursor()
cursor.execute(u"SELECT TOP(100) [L].[Tomo], [L].[Año], [L].[sala], [D].[ID_Deleg], [A].[Libro], [A].[idGenero], [A].[DNI], [A].[NombreInfante], [A].[ApellidoInfante], [A].[FechaNacimiento], [A].[Acta] ,[A].[PAGE_IMAGES], [A].[PAGE_IMAGES]"
              u"FROM [RLP-Nacimientos-Final].[dbo].[N_Redip] [A]"
              u"INNER JOIN [RLP-Nacimientos-Final].[dbo].[N_Libros] [L]"
              u"ON ([A].[Libro] = [L].[CODIGOLIBRO])"
			  u"INNER JOIN [RLP-Nacimientos-Final].[dbo].[N_Delegaciones] [D]"
			  u"ON ([D].[Delegacion] = [L].[DELEGACION])"
			  )


rows = cursor.fetchall()

for row in rows:
    path=str(row[12])
    #path=path.replace("r\\192.168.200.201\Images\ActasDeNacimiento",r"C:\XML_NACIMIENTOS_75_81\LOTE1")
    path = os.path.basename(path)
    print (path)

conn.close

# -*- coding: utf-8 -*-
import csv
from xml_creator import xmlCreator
from pretty_xml import p

# Main
with open('file.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader: # Por cada linea del archivo .csv invoca a xmlCreator con los campos del .csv que se desean en el XML
        xmlCreator(row['CIRCUNSCRIPCION'], row['TOMO'], row['ANO'], row['NROLIBRO'], row['ACTANRO'], row['PRIMERNOMBRE'], row['PRIMERAPELLIDO'], row['TIPODOCUMENTO'], row['NRODOCUMENTO'], row['GENERO'], row['FECHADEF'])

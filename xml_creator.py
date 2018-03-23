#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree, tostring
from pretty_xml import p
import os.path as path
import os
from tkinter import *
from tkinter import ttk
import pyodbc

from pyodbc import *
from tkinter import *
from tkinter import ttk
#from query_RPP import *
from PIL import Image
import pyodbc


# Creación de XML Frame
#-------------------------------------------------------------------------------
def xmlCreator(circup_, tomo_, ano_, nroLibro_, actaNro_, primerNombre_, primerApellido_, tipoDoc_, nroDoc_, genero_, fechaNac_, imagePath_):
    top = Element('xml') # XML root
    Acta = SubElement(top, 'Acta')
    tipoacta = SubElement(Acta, 'tipoacta')
    tipoacta.text= 'NACIMIENTOS'
    circunscripcion = SubElement(Acta, 'circunscripcion')
    circunscripcion.text= circup_
    tomo = SubElement(Acta, 'tomo')
    tomo.text= tomo_
    ano = SubElement(Acta, 'ano')
    ano.text= ano_
    nrolibro = SubElement(Acta, 'nrolibro')
    nrolibro.text= nroLibro_
    actanro = SubElement(Acta, 'actanro')
    actanro.text= actaNro_
    primernombre = SubElement(Acta, 'primernombre')
    primernombre.text= primerNombre_
    segundonombre = SubElement(Acta, 'segundonombre')
    tercernombre = SubElement(Acta, 'tercernombre')
    primerapellido = SubElement(Acta, 'primerapellido')
    primerapellido.text= primerApellido_
    segundoapellido = SubElement(Acta, 'segundoapellido')
    tercerapellido = SubElement(Acta, 'tercerapellido')
    tipodocumento = SubElement(Acta, 'tipodocumento')
    tipodocumento.text= tipoDoc_
    nrodocumento = SubElement(Acta, 'nrodocumento')
    nrodocumento.text= nroDoc_
    genero = SubElement(Acta, 'genero')
    genero.text= genero_
    fechadenacimiento = SubElement(Acta, 'fechadenacimiento')
    fechadenacimiento.text= fechaNac_
    imagefilename = SubElement(Acta, 'imagefilename')
    imagefilename.text= imagePath_
    obs  = SubElement(Acta, 'obs')
    #DetalleFallaProcesamiento = SubElement(top, 'DetalleFallaProcesamiento')
    #fechaProceso = SubElement(DetalleFallaProcesamiento, 'fechaProceso')
    #fechaProceso.text= '???????'
    #observacionRCE = SubElement(DetalleFallaProcesamiento, 'observacionRCE')
    #observacionRCE.text= '????????'
#-------------------------------------------------------------------------------

# XML output
#-------------------------------------------------------------------------------
    #direc=StringVar()
    direc=r"C:\XML_NACIMIENTOS_75_81\LOTE1\\"
    nroLibro_=str(nroLibro_)
    direc = direc + nroLibro_
    if not path.lexists(direc):
        os.makedirs(direc)
    name=imagePath_.replace(".jpg",".xml")
    path_file= direc + r"/" + name
    outfile = open(path_file, 'w')
    outfile.write(p(top))
    outfile.close()
#-------------------------------------------------------------------------------

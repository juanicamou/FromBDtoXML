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
    Acta = Element('Acta') # XML root
    #Acta = SubElement(top, 'Acta')
    # Datos del Libro
    #-------------------------------------------------------------------------
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
    # Datos del Acta
    #-------------------------------------------------------------------------
    actanro = SubElement(Acta, 'actanro')
    actanro.text= actaNro_
    # Datos del Causante
    #-------------------------------------------------------------------------
    primernombre = SubElement(Acta, 'primernombre')
    primernombre.text= primerNombre_
    segundonombre = SubElement(Acta, 'segundonombre')
    segundonombre.text=""
    tercernombre = SubElement(Acta, 'tercernombre')
    tercernombre.text=""
    primerapellido = SubElement(Acta, 'primerapellido')
    primerapellido.text= primerApellido_
    segundoapellido = SubElement(Acta, 'segundoapellido')
    segundoapellido.text=""
    tercerapellido = SubElement(Acta, 'tercerapellido')
    tercerapellido.text=""
    tipodocumento = SubElement(Acta, 'tipodocumento')
    tipodocumento.text= tipoDoc_
    nrodocumento = SubElement(Acta, 'nrodocumento')
    nrodocumento.text= nroDoc_
    genero = SubElement(Acta, 'genero')
    genero.text= genero_
    fechanacimiento = SubElement(Acta, 'fechanacimiento')
    fechanacimiento.text= fechaNac_
    renapercausante = SubElement(Acta, 'renapercausante')
    renapercausante.text=""
    # Imagen
    #-------------------------------------------------------------------------
    imagefilename = SubElement(Acta, 'imagefilename')
    #actaconceros = '%04d' % int(actaNro_)
    #actaconceros = str(actaconceros)
    #imagePath_2= nroLibro_ + "_" + actaconceros + ".pdf"
    imagePath_2=imagePath_.replace(".jpg",".pdf")
    imagefilename.text= imagePath_2
    # Datos de la Madre
    #-------------------------------------------------------------------------

    primernombremadre = SubElement(Acta, 'primernombremadre')
    primernombremadre.text=""
    segundonombremadre = SubElement(Acta, 'segundonombremadre')
    segundonombremadre.text=""
    tercernombremadre = SubElement(Acta, 'tercernombremadre')
    tercernombremadre.text=""
    primerapellidomadre = SubElement(Acta, 'primerapellidomadre')
    primerapellidomadre.text=""
    segundoapellidomadre = SubElement(Acta, 'segundoapellidomadre')
    segundoapellidomadre.text=""
    tercerapellidomadre = SubElement(Acta, 'tercerapellidomadre')
    tercerapellidomadre.text=""
    tipodocumentomadre = SubElement(Acta, 'tipodocumentomadre')
    tipodocumentomadre.text=""
    nrodocumentomadre = SubElement(Acta, 'nrodocumentomadre')
    nrodocumentomadre.text=""
    generomadre = SubElement(Acta, 'generomadre')
    generomadre.text=""
    renapermadre = SubElement(Acta, 'renapermadre')
    renapermadre.text=""

    # Observaciones
    #-------------------------------------------------------------------------
    obs  = SubElement(Acta, 'obs')
    obs.text=""
    #DetalleFallaProcesamiento = SubElement(top, 'DetalleFallaProcesamiento')

#-------------------------------------------------------------------------------

# XML output
#-------------------------------------------------------------------------------
    #direc=StringVar()
    direc=r"C:\XML_NAC_RELOAD\LOTE3\\"
    nroLibro_=str(nroLibro_)
    direc = direc + nroLibro_
    if not path.lexists(direc):
        os.makedirs(direc)
    name=imagePath_.replace(".jpg",".xml")
    path_file= direc + r"/" + name
    print (path_file)
    outfile = open(path_file, 'w')
    outfile.write(p(Acta))
    outfile.close()
#-------------------------------------------------------------------------------

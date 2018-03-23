# -*- coding: utf-8 -*-
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree, tostring
from xml.dom import minidom

# Funcion que hace "lindo" el XML
def p(elem):
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

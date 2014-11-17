#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web

# etree sax parser
from lxml import etree
class ParseRssNews ():
    def __init__ (self):
        print ('---- Principio del archivo')

    def start (self, tag, attrib): # Etiquetas de inicio
        print ('< %s>' % tag)
        for k in attrib:
            print (' %s = " %s"' % (k,attrib[k]))

    def end (self, tag): # Etiquetas de fin
        print ('</ %s>' % tag)

    def data (self, data): # texto
        print ('- %s-' % data)

    def close (self):
        print ('---- Fin del archivo')

parser = etree.XMLParser (target=ParseRssNews ())
etree.parse ('rss.xml', parser)
# rss.xml’ es un rss en
# http://ep00.epimg.net/rss/elpais/portada.xml

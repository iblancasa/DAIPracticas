#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import sys
import urllib
# etree sax parser
from lxml import etree


class ParseRssNews ():
    noticias=0
    imagen=0
    cantidadTermino = 0
    termino=""

    def __init__ (self,term):
        self.termino=term

    def start (self, tag, attrib): # Etiquetas de inicio
        if tag=="item":
            self.noticias += 1
        elif tag=="enclosure" and (attrib['type']=="image/png" or attrib['type']=="image/jpeg"):
            self.imagen += 1
            url=attrib['url']
            filename = url[url.rfind("/") + 1:]
            urllib.urlretrieve(url,filename)

    def end (self, tag): # Etiquetas de fin
        return

    def data (self, data): # texto
        if data.find(self.termino)>=0:
            self.cantidadTermino+=1

    def close (self):
        return


parseNews = ParseRssNews (sys.argv[1])
parser = etree.XMLParser (target=parseNews)
etree.parse ('rss.xml', parser)
# rss.xml’ es un rss en
# http://ep00.epimg.net/rss/elpais/portada.xml


print "Nº imagenes " + str(parseNews.imagen)
print "Nº noticias " + str(parseNews.noticias)
print "Nº noticias con término interesante "+str(parseNews.cantidadTermino)

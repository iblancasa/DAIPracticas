#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import sys
import urllib
# etree sax parser
from lxml import etree

'''
Busque por Internet páginas que ofrezcan contenidos
sindicados con RSS. Compruebe como visualiza su navegador dichos contenidos y
examine el código fuente (XML) de los mismos. Algunos sitios donde mirar:
+ Web de El País: http://elpais.es
+ Meneame: http://meneame.net
+ Barrapunto: http://barrapunto.com

Descargue alguno de los ficheros RSS a su ordenador para poder trabajar cómodamente con ellos.

lxml es una biblioteca bastante completa que permite analizar y trabajar
con ficheros XML de manera cómoda. De hecho, implementa varios mecanismos
distintos que permiten recorrer la estructura de un fichero XML así como tomar
distintas acciones según el contenido del mismo.


Una de las maneras de manejar los ficheros XML es usando SAX. Este sistema de análisis de XML
funciona de manera secuencial recorriendo las etiquetas. Usa una filosofía basada en
eventos donde una función es llamada cada vez que aparece un nuevo elemento del documento XML.

Se pide que se realice un pequeño script en Python que lea de disco un feed RSS cualquiera y:
+ Cuente el número de noticias o contenidos en el fichero RSS.
+ Contabilice el número de imágenes que contiene.
+ Busque algún término concreto (que se pueda pasar como parámetro al script) en los contenidos del RSS.
+ Descargue las imágenes de los feeds a su disco duro (por ejemplo usando urllib).
'''

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
            print data
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

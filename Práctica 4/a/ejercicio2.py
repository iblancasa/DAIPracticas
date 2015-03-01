#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Otra manera de manejar XML es a través de bibliotecas de manejo del DOM,
donde el fichero XML se carga en memoria en una estructura de  ́arbol que puede ser recorrida fácilmente. La biblioteca lxml
tiene la posibilidad de acceder a ficheros XML usando este tipo de acceso, usando el módulo etree.
Realice un script similar al del punto anterior pero usando esta tecnología DOM.
'''

from lxml import etree
import urllib
import sys

tree = etree.parse('rss.xml')

# Root element
rss = tree.getroot()

# Los elementos funcionan como listas
# First child
channel = rss[0]

items = channel.findall('item')
noticias = len(items)

imagenes=0
interesantes=0

termino = sys.argv[1]

for a in items:
        enclosures =a.findall('enclosure')
        for e in enclosures:
            if e.get("type") == "image/jpeg" or e.get("type") == "image/png":
                imagenes+=1
                url=e.get("url")
                filename = url[url.rfind("/") + 1:]
                urllib.urlretrieve(url,filename)

        if a.find("content").text.find(termino)>=0:
            interesantes+=1

print "Nº imágenes " + str(imagenes)
print "Nº noticias " + str(noticias)
print "Nº noticias con térmito interesante " + str(interesantes)

# -*- coding: utf-8 -*-

import feedparser
import urllib
import sys

url = "http://ep00.epimg.net/rss/elpais/portada.xml"

feed = feedparser.parse(url)

entradas = feed.entries


noticias = 0
imagenes = 0
interesantes = 0

for entrada in entradas:
    noticias+=1

    for enclosure in entrada.enclosures:
        if enclosure.type=="image/png" or enclosure.type=="image/jpeg":
            imagenes+=1
            url=enclosure.href
            filename = url[url.rfind("/") + 1:]
            urllib.urlretrieve(url,filename)

    for contenido in entrada.content:
        if contenido.value.find(sys.argv[1])>=0:
            interesantes+=1


print "Nº imágenes " + str(imagenes)
print "Nº noticias " + str(noticias)
print "Nº noticias con térmito interesante " + str(interesantes)

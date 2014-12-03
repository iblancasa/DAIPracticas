#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

for a in items:
        enclosures =a.findall('enclosure')
        for e in enclosures:
            if e.get("type") == "image/jpeg" or e.get("type") == "image/png":
                imagenes+=1
                url=e.get("url")
                filename = url[url.rfind("/") + 1:]
                urllib.urlretrieve(url,filename)

        if a.find("content").text.find("del")>=0:
            interesantes+=1

print "Nº imágenes " + str(imagenes)
print "Nº noticias " + str(noticias)
print "Nº noticias con térmito interesante " + str(noticias)

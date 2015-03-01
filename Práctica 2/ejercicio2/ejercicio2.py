#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Averigüe el mecanismo más habitual que ofrece web.py para servir contenidos estáticos tales como
imágenes u hojas de estilo. Añada algunas imágenes estáticas a su aplicación y compruebe que el
cliente es capaz de acceder a ellas directamente a través de una URL.
Aunque el método habitual para servir p ́aginas web de web.py es el uso de templates, modifique el ejemplo original del punto
anterior para generar en vez de simplemente el código Hello, World!, generar un fichero HTML correcto en
el que se incluya, entre los demás elementos necesarios, una página de estilo CSS
y alguna imagen estática.
''''


import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'

        web = '<!doctype html>\n \
        		<html>\n\
        			<head>\n\
        				 <link href="static/style.css" media="all" rel="stylesheet" type="text/css" />\n\
        				<title>Hola</title>\n\
        			</head>\n\
        			<body>\n\
        				<p>' + name + '</p>\n\
        				<img src="static/imagen.jpg" />\n\
        			</body>\n\
        		</html>\
        '

        return web;

if __name__ == "__main__":
    app.run()

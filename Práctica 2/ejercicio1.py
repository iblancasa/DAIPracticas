#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
En la página web oficial de web.py podemos encontrar un ejemplo mini-malista ("Hola Mundo") en el que se utiliza el framework para crear un apli-
cación web extremadamente sencilla que saluda al usuario. Copie dicho codigo, ejecútelo, compruebe que funciona e intente entender cada parte de dicho pro-
grama.'''


import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()

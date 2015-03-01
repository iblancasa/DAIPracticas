#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Averigüe el mecanismo de web.py para el análisis y manejo de distintas
URLs. Cree una nueva aplicación web en la que distintas clases manejen distintas URLs para servir
páginas distintas dependiendo de la URL introducida.
Asimismo, sería conveniente ser capaces de obtener los parámetros de una llamada GET.
Por último, defina una página para el caso en que una URL no
esté definida.
'''

import web

urls = (
    '/hello', 'hello',
    '/bye', 'bye',
    '/(.*)', 'error404'
)
app = web.application(urls, globals())


class hello:
    def GET(self):
    	entrada = web.input(parametro="No insertado")
        return 'Hello, world! '+ entrada.parametro

class bye:
    def GET(self):
    	entrada = web.input(parametro="No insertado")
        return 'Bye, world!'+ entrada.parametro


class error404:
    def GET(self, name):
        return 'Error 404. Web no encontrada'




if __name__ == "__main__":
    app.run()

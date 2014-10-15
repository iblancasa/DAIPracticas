#!/usr/bin/env python
# -*- coding: utf-8 -*- 

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
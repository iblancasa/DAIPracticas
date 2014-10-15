#!/usr/bin/env python
# -*- coding: utf-8 -*- 

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
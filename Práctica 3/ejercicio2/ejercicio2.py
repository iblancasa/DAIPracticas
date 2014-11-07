#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import web
from web.contrib.template import render_mako

urls = (
        '/', 'index'
        )

app = web.application(urls, globals(), autoreload=True)
render = render_mako(
        directories=['templates'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )

class index:
    def GET(self):
    	nombre = "paco"
        return render.index(name=nombre)

if __name__ == "__main__":
    app.run()
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import web
from web import form
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

myform = form.Form(
        form.Textbox('user', description="User"),
        form.Password('password',description="Pass"),
        form.Button('Enviar',type="submit")
    )


class index:
    def GET(self):
        form = myform()
        cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        return render.index(form=cabecera)


    def POST(self):
        form = myform()
        if not form.validates() or form.d.user!="dai" or form.d.password !="dai": 
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form><p>EL LOGIN FALLO</p>"
        else:
            cabecera = "Bienvenido "+ form.d.user
        return render.index(form=cabecera)

if __name__ == "__main__":
    app.run()
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import web
from web import form

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form( 
    form.Textbox("texto", description="Inserte texto"),
    form.Button("enviar",type="submit",value="Enviar"),
    )

class index: 
    def GET(self): 
        form = myform()
        return "<html><body><form name=\"main\" method=\"post\"> "+form.render()+"</form></body></html>"

    def POST(self):
        form = myform() 

        if not form.validates(): 
            return "<html><body><form name=\"main\" method=\"post\"> "+form.render()+"</form></body></html>"
        else:
            return "<html><body>Su texto es: %s</body></html>" % (form['texto'].value)



if __name__=="__main__":
    app.run()
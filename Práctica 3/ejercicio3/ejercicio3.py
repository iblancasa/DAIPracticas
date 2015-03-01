#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
En toda aplicación web es necesario gestionar información que se mantenga
entre las distintas páginas que visita el usuario. Para ello se hace uso de las
sesiones. En web.py las sesiones se manejan mediante la clase Session.
En esta práctica adaptaremos nuestra página web para que el formulario de
login anteriormente citado funcione correctamente y se muestre distinto con-
tenido si el usuario está ya identificado o no (a esta alturas la comprobación
de un usuario único estará codificada "a pelo" en la aplicación, en el siguiente
apartado guardaremos distintos usuarios usando persistencia). Por ejemplo, el
formulario de login de la cabecera solo debe aparecerle a los usuario no identificados, mientras que a los
identificados debe mostrárseles el típico mensaje de
"Bienvenido xxxx" y un enlace para hacer logout.
Además, implementaremos en nuestra aplicación (y utilizando exclusivamente sesiones) un "menu"
que muestre -y permita acceder- a las últimas 3 páginas del sitio visitadas
(lo podemos incluir en el menú de la izquierda).
'''


import web
from web import form
from web.contrib.template import render_mako

urls = (
        '/web1','web1',
        '/web2','web2',
        '/web3','web3',
        '/web4','web4',
        '/salir','logout',
        '/', 'index'
        )

app = web.application(urls, globals(), autoreload=False)


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

session = web.session.Session(app, web.session.DiskStore('sessions'),initializer={'iniciado': False})


def addWeb(web):
        if session.get('iniciado') != True:
            session.visitadas2="http://google.es"
            session.visitadas1="http://google.es"
            session.visitadas0="http://google.es"
            session.iniciado = True
            print session.iniciado

        session.visitadas2=session.get('visitadas1')
        session.visitadas1=session.get('visitadas0')
        session.visitadas0=web

        session.enlaces = "<ul><li><a href=\""+session.get('visitadas0')+"\">"+session.get('visitadas0')+"</a></li>\
        <li><a href=\""+session.get('visitadas1')+"\">"+session.get('visitadas1')+"</a></li>\
        <li><a href=\""+session.get('visitadas2')+"\">"+session.get('visitadas2')+"</a></li></ul>"




class index:
    def GET(self):
        form = myform()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a>"
        addWeb("/")
        return render.index(form=cabecera,enlaces=session.get('enlaces'))



    def POST(self):
        form = myform()
        if (not form.validates() or form.d.user!="dai" or form.d.password !="dai") and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form><p>EL LOGIN FALLO</p>"
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a>"
        addWeb("/")
        print session.get('enlaces')
        return render.index(form=cabecera,enlaces=session.get('enlaces'))




class web1:
    def GET(self):
        form = myform()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a>"
        self.addWeb("web1")
        return render.pagina1(form=cabecera,enlaces=session.get('enlaces'))

    def addWeb(self,web):
        if session.iniciado==False:
            session.visitadas2="http://google.es"
            session.visitadas1="http://google.es"
            session.visitadas0="http://google.es"
            session.iniciado = True
            print session.iniciado

        session.visitadas2=session.get('visitadas1')
        session.visitadas1=session.get('visitadas0')
        session.visitadas0=web

        session.enlaces = "<ul><li><a href=\""+session.get('visitadas0')+"\">"+session.get('visitadas0')+"</a></li>\
        <li><a href=\""+session.get('visitadas1')+"\">"+session.get('visitadas1')+"</a></li>\
        <li><a href=\""+session.get('visitadas2')+"\">"+session.get('visitadas2')+"</a></li></ul>"

    def POST(self):
        form = myform()
        if (not form.validates() or form.d.user!="dai" or form.d.password !="dai") and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form><p>EL LOGIN FALLO</p>"
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a>"
        addWeb("web1")
        return render.pagina1(form=cabecera,enlaces=session.get('enlaces'))

class web2:
    def GET(self):
        form = myform()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a>"
        addWeb("web2")
        return render.pagina2(form=cabecera,enlaces=session.get('enlaces'))




    def POST(self):
        form = myform()
        if (not form.validates() or form.d.user!="dai" or form.d.password !="dai") and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form><p>EL LOGIN FALLO</p>"
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a>"
        addWeb("web2")

        return render.pagina2(form=cabecera,enlaces=session.get('enlaces'))

class web3:
    def GET(self):
        form = myform()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a>"
        addWeb("web3")
        return render.pagina3(form=cabecera,enlaces=session.get('enlaces'))



    def POST(self):
        form = myform()
        if (not form.validates() or form.d.user!="dai" or form.d.password !="dai") and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form><p>EL LOGIN FALLO</p>"
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a>"
        addWeb("web3")

        return render.pagina3(form=cabecera,enlaces=session.get('enlaces'))

class web4:
    def GET(self):
        form = myform()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a>"
        addWeb("web4")
        return render.pagina4(form=cabecera,enlaces=session.get('enlaces'))




    def POST(self):
        form = myform()
        if (not form.validates() or form.d.user!="dai" or form.d.password !="dai") and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form><p>EL LOGIN FALLO</p>"
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a>"
        addWeb("web4")
        return render.pagina4(form=cabecera,enlaces=session.get('enlaces'))




class logout:
    def GET(self):
        session.kill()
        raise web.seeother('/')


if __name__ == "__main__":
    app.run()

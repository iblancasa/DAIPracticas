#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Basándonos en lo aprendido en los puntos anteriores, añadamos a nuestra
web (de la práctica 3) algún cuadro en donde se muestren los últimos feeds de
alguna fuente web que nos interese (periódico o web).
Sería conveniente, por no abusar del proveedor del RSS, no consultarlo con
demasiada frecuencia (por ejemplo como máximo cada 10 minutos). Para ello
podemos hacer algún tipo de caché en nuestra base de datos (o en disco) de los
RSS que vayamos a mostrar.
'''

import web
from web import form
from web.contrib.template import render_mako
import time
import DataBase
import urllib
import feedparser
import datetime

urls = (
        '/web1','web1',
        '/web2','web2',
        '/web3','web3',
        '/web4','web4',
        '/salir','logout',
        '/modificar','modificar',
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
        form.Password('contrasena',description="Pass"),
        form.Button('Enviar',type="submit")
    )


vemail = form.regexp(r".*@.*", "Debe ser un email valido")
vvisa = form.regexp(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", "Debe ser una visa valida")
vpass = form.regexp('.{7,}', "Debe tener 7 caracteres o mas")

registro = form.Form(
    form.Textbox('nombre',form.Validator("El nombre no puede estar vacio", lambda i: i !=""),description="Nombre"),
    form.Textbox('apellidos',form.Validator("Los apellidos no pueden estar vacios", lambda i: i !=""),description="Apellidos"),
    form.Textbox('correo',vemail,description="Correo"),
    form.Dropdown('dianacimiento',[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
     (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'),
     (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')],description="Dia de nacimiento"),
     form.Dropdown('mesnacimiento',[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
     (9, '9'), (10, '10'), (11, '11'), (12, '12')],description="Mes de nacimiento"),
    form.Dropdown('anonacimiento',[(1993,'1993'),(1992,'1992'),(1991,'1991')],description="Ano nacimiento"),
    form.Textarea('direccion',form.Validator("La direccion no puede estar vacia", lambda i: i !=""),description="Direccion"),
    form.Password('password',vpass,description="Password"),
    form.Password('password2',vpass,description="Verificacion"),
    form.Textbox('visa',vvisa,description="Numero visa"),
    form.Radio('formapago',['Contra reembolso','Tarjeta Visa']),
    form.Checkbox('aceptacion', form.Validator("Acepta las clausulas", lambda i: i == 'true'), value='true'),
    form.Button('submit',type="submit", description="Enviar"),
    validators = [
        form.Validator("Las pass no coinciden", lambda i: i.password == i.password2)]
)



session = web.session.Session(app, web.session.DiskStore('sessions'),initializer={'iniciado': False})
ultimahora=datetime.datetime.now()
rss=""
urlrss="http://ep00.epimg.net/rss/elpais/portada.xml"

def login(usuario,contrasena):
	if usuario=="" or contrasena=="" or usuario==None or contrasena==None:
		return False
	elif usuario == DataBase.getNombre(usuario) and contrasena == DataBase.getPassword(usuario):
		return True
	else:
		return False


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

        session.enlaces = "<ul id=\"rss\"><li><a href=\""+session.get('visitadas0')+"\">"+session.get('visitadas0')+"</a></li>\
        <li><a href=\""+session.get('visitadas1')+"\">"+session.get('visitadas1')+"</a></li>\
        <li><a href=\""+session.get('visitadas2')+"\">"+session.get('visitadas2')+"</a></li></ul>"




class index:
    def GET(self):
        form = myform()
        nuevousuario = registro()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
        addWeb("/")
        formularioRegistro =  "<form name=\"main\" method=\"post\"> "+nuevousuario.render()+"</form>"

        global rss
        global ultimahora
        global urlrss
        ultimahora=datetime.datetime.now()
        if datetime.datetime.now()-ultimahora>=datetime.timedelta(minutes=10) or rss=="":
            ultimahora=datetime.datetime.now()
            feed = feedparser.parse(urlrss)
            entradas = feed.entries
            rss="<ul>"
            for entrada in entradas:
                rss+="<li><a href=\""+entrada.link+"\">"+entrada.title+"</a></li>"
            rss+="</ul>"

        print rss
        return render.index(form=cabecera,enlaces=session.get('enlaces'),registro=formularioRegistro,rss=rss)



    def POST(self):
        form = myform()
        nuevousuario = registro()
        if (not form.validates() or not login(form.d.user,form.d.contrasena)) and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
            if not nuevousuario.validates():
            	formularioRegistro =  "<form name=\"main\" method=\"post\"> "+nuevousuario.render()+"</form>"
            else:
            	formularioRegistro=""
            	DataBase.insertar(nuevousuario.d.nombre,nuevousuario.d.apellidos,nuevousuario.d.correo,nuevousuario.d.dianacimiento,nuevousuario.d.mesnacimiento,
            		nuevousuario.d.anonacimiento,nuevousuario.d.direccion,nuevousuario.d.password,nuevousuario.d.visa,nuevousuario.d.formapago)
            	DataBase.close()
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
            formularioRegistro=""

        addWeb("/")

        global rss
        global ultimahora
        global urlrss
        ultimahora=datetime.datetime.now()
        if datetime.datetime.now()-ultimahora>=datetime.timedelta(seconds=10) or rss==None:
            ultimahora=datetime.datetime.now()
            feed = feedparser.parse(urlrss)
            entradas = feed.entries
            rss="<ul>"
            for entrada in entradas:
                rss+="<li><a href=\""+entrada.link+"\">"+entrada.title+"</a></li>"
            rss+="</ul>"

        return render.index(form=cabecera,enlaces=session.get('enlaces'),registro=formularioRegistro,rss=rss)




class web1:
    def GET(self):
        form = myform()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
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
       	if (not form.validates() or not login(form.d.user,form.d.contrasena)) and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
        addWeb("web1")

        return render.pagina2(form=cabecera,enlaces=session.get('enlaces'))


class web2:
    def GET(self):
        form = myform()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
        addWeb("web2")
        return render.pagina2(form=cabecera,enlaces=session.get('enlaces'))




    def POST(self):
        form = myform()
       	if (not form.validates() or not login(form.d.user,form.d.contrasena)) and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
        addWeb("web2")

        return render.pagina2(form=cabecera,enlaces=session.get('enlaces'))

class web3:
    def GET(self):
        form = myform()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
        addWeb("web3")
        return render.pagina3(form=cabecera,enlaces=session.get('enlaces'))



    def POST(self):
        form = myform()
        if (not form.validates() or not login(form.d.user,form.d.contrasena)) and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
        addWeb("web3")

        return render.pagina3(form=cabecera,enlaces=session.get('enlaces'))

class web4:
    def GET(self):
        form = myform()
        if session.get('usuario') == None:
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
        addWeb("web4")
        return render.pagina4(form=cabecera,enlaces=session.get('enlaces'))




    def POST(self):
        form = myform()
       	if (not form.validates() or not login(form.d.user,form.d.contrasena)) and (not hasattr(session, 'usuario')):
            cabecera = "<form name=\"main\" method=\"post\"> "+form.render()+"</form>"
        else:
            session.usuario = form.d.user
            cabecera = "Bienvenido "+session.usuario+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
        addWeb("web4")
        return render.pagina4(form=cabecera,enlaces=session.get('enlaces'))



class modificar:

	registro = form.Form(
		    form.Textbox('nombre',form.Validator("El nombre no puede estar vacio", lambda i: i !=""),description="Nombre",value=DataBase.getNombre(session.get('usuario'))),
		    form.Textbox('apellidos',form.Validator("Los apellidos no pueden estar vacios", lambda i: i !=""),description="Apellidos",value=DataBase.getApellidos(session.get('usuario'))),
		    form.Textbox('correo',vemail,description="Correo",value=DataBase.getCorreo(session.get('usuario'))),
		    form.Dropdown('dianacimiento',[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
		     (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'),
		     (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')],description="Dia de nacimiento",value=DataBase.getDiaNacimiento(session.get('usuario'))),
		     form.Dropdown('mesnacimiento',[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
		     (9, '9'), (10, '10'), (11, '11'), (12, '12')],description="Mes de nacimiento",value=DataBase.getMesNacimiento(session.get('usuario'))),
		    form.Dropdown('anonacimiento',[(1993,'1993'),(1992,'1992'),(1991,'1991')],description="Ano nacimiento",value=DataBase.getAnoNacimiento(session.get('usuario'))),
		    form.Textarea('direccion',form.Validator("La direccion no puede estar vacia", lambda i: i !=""),description="Direccion",value=DataBase.getDireccion(session.get('usuario'))),
		    form.Password('password',vpass,description="Password"),
		    form.Password('password2',vpass,description="Verificacion"),
		    form.Textbox('visa',vvisa,description="Numero visa",value=DataBase.getNumeroVisa(session.get('usuario'))),
		    form.Radio('formapago',['Contra reembolso','Tarjeta Visa'],value=DataBase.getFormaPago(session.get('usuario'))),
		    form.Checkbox('aceptacion', form.Validator("Acepta las clausulas", lambda i: i == 'true'), value='true'),
		    form.Button('submit',type="submit", description="Enviar"),
		    validators = [
		        form.Validator("Las pass no coinciden", lambda i: i.password == i.password2)]
		)

	def GET(self):
		cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
		self.registro = form.Form(
		    form.Textbox('nombre',form.Validator("El nombre no puede estar vacio", lambda i: i !=""),description="Nombre",value=DataBase.getNombre(session.get('usuario'))),
		    form.Textbox('apellidos',form.Validator("Los apellidos no pueden estar vacios", lambda i: i !=""),description="Apellidos",value=DataBase.getApellidos(session.get('usuario'))),
		    form.Textbox('correo',vemail,description="Correo",value=DataBase.getCorreo(session.get('usuario'))),
		    form.Dropdown('dianacimiento',[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
		     (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'),
		     (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')],description="Dia de nacimiento",value=DataBase.getDiaNacimiento(session.get('usuario'))),
		     form.Dropdown('mesnacimiento',[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
		     (9, '9'), (10, '10'), (11, '11'), (12, '12')],description="Mes de nacimiento",value=DataBase.getMesNacimiento(session.get('usuario'))),
		    form.Dropdown('anonacimiento',[(1993,'1993'),(1992,'1992'),(1991,'1991')],description="Ano nacimiento",value=DataBase.getAnoNacimiento(session.get('usuario'))),
		    form.Textarea('direccion',form.Validator("La direccion no puede estar vacia", lambda i: i !=""),description="Direccion",value=DataBase.getDireccion(session.get('usuario'))),
		    form.Password('password',vpass,description="Password"),
		    form.Password('password2',vpass,description="Verificacion"),
		    form.Textbox('visa',vvisa,description="Numero visa",value=DataBase.getNumeroVisa(session.get('usuario'))),
		    form.Radio('formapago',['Contra reembolso','Tarjeta Visa'],value=DataBase.getFormaPago(session.get('usuario'))),
		    form.Checkbox('aceptacion', form.Validator("Acepta las clausulas", lambda i: i == 'true'), value='true'),
		    form.Button('submit',type="submit", description="Enviar"),
		    validators = [
		        form.Validator("Las pass no coinciden", lambda i: i.password == i.password2)]
		)

		formulariomodificar = self.registro()
		return render.modificar(form=cabecera,enlaces=session.get('enlaces'),modificar="<form name=\"main\" method=\"post\"> "+formulariomodificar.render()+"</form>")



	def POST(self):
		formulariomodificar = self.registro()
		cabecera = "Bienvenido "+session.get('usuario')+"   <a href=\"salir\">SALIR</a><a href=\"modificar\">Modificar</a>"
		if formulariomodificar.validates():
			DataBase.insertar(formulariomodificar.d.nombre,formulariomodificar.d.apellidos,formulariomodificar.d.correo,formulariomodificar.d.dianacimiento,formulariomodificar.d.mesnacimiento,
    			formulariomodificar.d.anonacimiento,formulariomodificar.d.direccion,formulariomodificar.d.password,formulariomodificar.d.visa,formulariomodificar.d.formapago)
		        return render.modificar(form=cabecera,enlaces=session.get('enlaces'),modificar="<p>TODO INSERTADO</p><form name=\"main\" method=\"post\"> "+formulariomodificar.render()+"</form>")
		else:
			return render.modificar(form=cabecera,enlaces=session.get('enlaces'),modificar="<form name=\"main\" method=\"post\"> "+formulariomodificar.render()+"</form>")




class logout:
    def GET(self):
        session.kill()
        raise web.seeother('/')




if __name__ == "__main__":
    app.run()

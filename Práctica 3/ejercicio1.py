#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import web
from web import form

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox('nombre',description="Nombre"),
	form.Textbox('apellidos',description="Apellidos"),
    form.Textbox('correo',description="Correo"),
    form.Dropdown('dianacimiento',[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
     (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), 
     (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')],description="Dia de nacimiento"),
     form.Dropdown('mesnacimiento',[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
     (9, '9'), (10, '10'), (11, '11'), (12, '12')],description="Mes de nacimiento"),
    form.Dropdown('anonacimiento',[(1993,'1993'),(1992,'1992'),(1991,'1991')],description="Ano nacimiento"),
    form.Textarea('direccion',description="Direccion"),
    form.Password('password',description="Password"),
    form.Textbox('visa',description="Numero visa"),
    form.Password('verificacion',description="Verificacion"),
    form.Radio('formapago',['Contra reembolso','Tarjeta Visa']),
    form.Checkbox('aceptacion', form.Validator("Acepta las clausulas", lambda i: i == 'true'), value='true'),
    form.Button('submit',type="submit", description="Enviar")
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
	    	return "hello";

if __name__ == "__main__":
    app.run()
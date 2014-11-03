#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import web
        
urls = (
    '/(.*)', 'index'
)
app = web.application(urls, globals())

login = form.Form(
    form.Textbox('nombre',description="Nombre"),
    form.Textbox('apellidos',description="Apellidos"),
    form.Textbox('correo',description="Correo"),
    form.Dropdown('dianacimiento',description="Dia de nacimiento",[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
     (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), 
     (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')]),
    form.Dropdown('mesnacimiento',description="Mes de nacimiento",[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'),
     (9, '9'), (10, '10'), (11, '11'), (12, '12')]),
    form.Dropdown('anonacimiento',description="Ano nacimiento",[(1993,'1993'),(1992,'1992'),(1991,'1991')]),
    form.Textarea('direccion',description="Direccion"),
    form.Password('password',description="Password"),
    form.Textbox('visa',description="Numero visa"),
    form.Password('verificacion',description="Verificacion"),
    form.Radio('formapago',['Contra reembolso','Tarjeta Visa']),
    form.Checkbox('aceptacion'),
    form.Button('submit',type="submit", description="Enviar")
)




class index:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'



if __name__ == "__main__":
    app.run()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
En la práctica anterior empezamos a manejar la sub-biblioteca Form de web.py para manejar formularios.
Dicha biblioteca contiene opciones interesantes que pueden facilitarnos el introducir información en una página web,
así como su posterior manejo. En este punto de la práctica vamos realizar un formulario algo
más complejo que los vistos hasta ahora:
+ El formulario debe preguntar los siguientes datos personales a los usuarios
de la web: nombre, apellidos, DNI, correo electrónico, fecha de nacimiento, dirección, contraseña,
verificación de la contraseña, forma de pago preferida (contra reembolso o tarjeta VISA), número de la tarjeta VISA,
aceptación de las clausulas de protección de datos, botón de mandar.

Los campos del formulario deben ser del tipo:
• Nombre, apellidos, correo electr ́onico, número de VISA: textbox.
• Fecha de nacimiento: dropdown (x3, día, mes, año).
• Dirección: textarea.
• Contraseña y verificación: password.
• Forma de pago: radio.
• Aceptación clausulas: checkbox.
• Botón: button.


El formulario debe verificarse utilizando los mecanismos que nos ofrece la biblioteca (validators).
Probablemente haga falta utilizar alguna función lambda de Python. Particularmente hay que asegurarse de que:
• Ningún campo de texto esté vacío
• El correo electrónico sea "válido"
• Que el número de la tarjeta VISA sea correcto (4 grupos de 4 dígitos separados por un espacio o -).
• Que la fecha de nacimiento sea una fecha válida.
• Que la contraseña y su validación coincidan y tengan más de 7 caracteres.
• Que las clausulas se hayan aceptado.

Nota: La validación de un elemento tipo checkbox es un poco "especial" debido a como se implementa en HTML
(las dificultades en su uso vienen heredadas de HTML, no es problema especial de web.py). Para no malgastar
mucho tiempo buscando soluciones, se puede usar el siguiente validador (cortesía de E. Serrano):
form.Checkbox("accept_license",
form.Validator("Acepta las clausulas", lambda i: i == ’true’),
value='true'
)
'''




import web
from web import form

urls = ('/', 'index')
app = web.application(urls, globals())

vemail = form.regexp(r".*@.*", "Debe ser un email valido")
vvisa = form.regexp(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", "Debe ser una visa valida")
vpass = form.regexp('.{7,}', "Debe tener 7 caracteres o mas")

myform = form.Form(
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


class index:
    def GET(self):
    	form = myform()
    	return "<html><body><form name=\"main\" method=\"post\"> "+form.render()+"</form></body></html>"


    def POST(self):
	    form = myform()
	    if not form.validates():
	    	return "<html><body><form name=\"main\" method=\"post\"> "+form.render()+"</form></body></html>"
	    else:
	    	return "<html><body>Gracias por sus datos "+form['nombre'].value+"</body></html>";

if __name__ == "__main__":
    app.run()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Cuando desarrollamos una aplicaci ́on web (por ejemplo con web.py) no es
buena idea incluir el código HTML de las páginas dentro de nuestra aplicación
Python. Utilizando plantillas (templates) conseguiremos simplificar mucho todas
las tareas repetitivas, así como separar correctamente el aspecto de la aplicación
(vista) de su lógica interna (controlador).
Una biblioteca potente de templates para Python es Mako, utilizada en
sitios masivos en producción como http://reddit.com. En esta práctica vamos
a familiarizarnos con esta biblioteca. Para ello tendremos que construir varias
páginas usando esta biblioteca.
Dichas páginas deberán mostrar un sitio web en el que haya (al menos) una
cabecera, dos columnas y un pie de página. En la cabecera habrá una imagen
de logo del sitio, el nombre del mismo, un subtítulo y un mini-formulario de
login. En la columna izquierda habrá opciones (como por ejemplo menús),
la columna de la derecha contendrá el cuerpo principal de la página y el pie
contendrá información sobre el autor de la página y los derechos de la misma
(licencia). En caso de no querer hacer el diseño de la página desde cero, podemos
optar por descargar alguna plantilla web ya creada y adaptarla para poder
presentar los contenidos dinámicos de la aplicación.
Debemos intentar seguir el paradigma modelo, vista, controlador lo más fielmente posible,
de tal manera que sea posible, por ejemplo, cambiar radicalmente
el aspecto de la aplicación web modificando únicamente los templates.
'''


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

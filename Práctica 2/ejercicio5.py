#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A estas alturas debemos ser capaces de hacer un sitio web dinámico sencillo
(probablemente no muy bonito hasta que no utilicemos templates). Pese a que
muchísimos sitios dinámicos solo cambian su código HTML dependiendo de las
entradas de los usuarios, en este último apartado vamos a ir un paso más allá: se creará contenido gráfico dinámico.
La idea de este ejercicio es crear una aplicación web dinámica que a partir de ciertos parámetros sea capaz de
generar en directo una imagen fractal. Para esta tarea podemos reutilizar el código de los ejercicios de la primera sesión
de prácticas (ejercicio sobre el fractal de Mandelbrot). La aplicación web debe
contar con al menos estas características:
+ Mediante un formulario web debe preguntar al menos los siguientes parámetros para calcular el fractal: recuadro del
plano complejo sobre el que se calculará el fractal (x 1 , y 1 ) - (x 2 , y 2 ) y anchura de la imagen resultante
(en píxeles).
+ Una vez obtenidos dichos datos debe calcularse y dibujarse el fractal. Se podrá usar alguna función similar a las
del gui ́on de prácticas 1 o bien usar las funciones del fichero mandelbrot.py.
+ La imagen completamente creada debe mostrarse al usuario usando el formato PNG.

Adicionalmente, si se quiere mejorar la aplicaci ́on, se puede:
+ Añadir algunos parámetros al formulario como la paleta de color a utilizar
cuando se dibuje el fractal y el número máximo de iteraciones a ejecutar
cuando se calcula el fractal.
+ Implementar algún tipo de caché de la aplicación que evite recalcular el
mismo fractal en caso de que se hagan dos peticiones idénticas (ahorrando ciclos de cómputo). Para conseguirlo, por ejemplo,
se pueden guardar en disco los fractales con un nombre que identifiquen los parámetro utilizados
para el cálculo. Cada vez que se solicite un nuevo fractal lo primero que
realizará la aplicación será comprobar si el fichero con dichos parámetros
ya ha sido creado. En caso afirmativo se servirá tal cual. En caso negativo,
se realizarán los cálculos del fractal oportunos.
+ Mejorar el sistema de cach ́e propuesto para que las imágenes de más de
un día se borren para evitar colapsar el disco duro del servidor en caso de
que se soliciten muchas imágenes fractales.
'''


import time
import png
import os
import web
from web import form

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox("x1", description="X1"),
    form.Textbox("x2", description="X2"),
    form.Textbox("y1", description="Y1"),
    form.Textbox("y2", description="Y2"),
    form.Textbox("ancho", description="ancho"),
    form.Textbox("iteraciones", description="iteraciones"),
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
        nuevo = Mandelbrot(float(form['x1'].value), float(form['y1'].value), float(form['x2'].value), float(form['y2'].value), int(form['ancho'].value),int(form['iteraciones'].value), "fich.png");
        nuevo.pintaMandelbrot();
        return "<html><body><img src=\"static/fich.png\"/></body></html>"


class Mandelbrot:
  __x1=0
  __x2=0
  __y1=0
  __y2=0
  __ancho=0
  __alto=0
  __iteraciones=0
  __nombre=""



  def __init__(self,xa, ya, xb, yb, anchoim, iteracionesadar, nombrefichero):
    self.__x1=xa
    self.__x2=xb
    self.__y1=ya
    self.__y2=yb
    self.__ancho=anchoim
    self.__alto = int(abs (self.__y2 - self.__y1) * self.__ancho / abs(self.__x2 - self.__x1))

    if iteracionesadar > 1000:
      self.__iteraciones=1000;
    elif iteracionesadar<1:
      self.__iteraciones=1;
    else:
      self.__iteraciones=iteracionesadar



  def pintaMandelbrot(self):


    xa = self.__x1
    xb = self.__x2
    ya = self.__y1
    yb = self.__y2
    maxIt = self.__iteraciones
    # image size
    imgx = self.__ancho
    imgy = int(abs (self.__y2 - self.__y1) * self.__ancho / abs(self.__x2 - self.__x1));

    p=[]

    completado = 0

    it = 0

    for y in range(imgy):
      zy = y * (yb - ya) / (imgy - 1)  + ya
      a = ()
      for x in range(imgx):
        zx = x * (xb - xa) / (imgx - 1)  + xa
        z = zx + zy * 1j
        c = z
        for i in range(maxIt):
          it = it + 1
          if abs(z) > 2.0: break
          z = z * z + c
        i = maxIt - i
        a = a + (i%10*25, i%16*16, i%8*32);

      p.append(a)
      completado = int(100*y/imgy)

      if completado%10 ==0:
        os.system('clear')
        print str(completado) + "%"


    f = open("static/fich.png", 'wb')
    w = png.Writer(imgy, imgx)
    w.write(f, p) ;
    f.close()




if __name__ == "__main__":
  app.run()

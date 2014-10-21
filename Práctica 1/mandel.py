#!/usr/bin/python
# -*- coding: utf-8 -*-

# Practicas de Desarrollo de Aplicaciones para Internet (DAI)
# Copyright (C) 2013 - Zerjillo (zerjioi@ugr.es)
#    
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#   
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#   
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
import png
import os

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
    self.__alto=int(abs (self.__y2 - self.__y1) * self.__ancho / abs(self.__x2 - self.__x1))

    if iteracionesadar > 1000:
      self.__iteraciones=1000;
    elif iteracionesadar<1:
      self.__iteraciones=1;
    else:
      self.__iteraciones=iteracionesadar
    
    self.__nombre=nombrefichero


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

    f = open('swatch.png', 'wb')
    w = png.Writer(imgy, imgx)
    w.write(f, p) ; 
    f.close()
    print type(p)
    print 400*400
    print it

    
        
if __name__ == "__main__":
    nuevo = Mandelbrot(-0.7, -0.7, -0.4, -0.4, 400, 255, "fich.png");
    nuevo.pintaMandelbrot();

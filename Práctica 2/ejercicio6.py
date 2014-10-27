#!/usr/bin/python
# -*- coding: utf-8 -*-

import drawSVG
import random
import web
from web import form

urls = ('/', 'index')
app = web.application(urls, globals())


class index: 
  def GET(self): 
    generarFigura();
    return  "<html><body><img src=\"static/test.svg\"/></html></body>"


def generarFigura():
  numero = random.randrange(1, 4, 1) 

  if numero==1:
    my_svg = drawSVG.SVG({'width':200, 'height':100})
    my_svg.addStyle('rect', {'fill': 'green', 'stroke-width': 2, 'stroke': 'black'})
    my_svg.addChildElement('rect', {'x':20, 'y':40, 'width':80, 'height':50})
    my_svg.addChildElement('circle', {'cx':120, 'cy':40, 'r':25})
  elif numero==2:
    my_svg = drawSVG.SVG({'width':200, 'height':100})
    my_svg.addStyle('rect', {'fill': 'blue', 'stroke-width': 2, 'stroke': 'green'})
    my_svg.addChildElement('rect', {'x':50, 'y':40, 'width':10, 'height':24})
    my_svg.addChildElement('circle', {'cx':120, 'cy':40, 'r':25})
  else:
    my_svg = drawSVG.SVG({'width':200, 'height':100})
    my_svg.addStyle('rect', {'fill': 'green', 'stroke-width': 2, 'stroke': 'green'})
    my_svg.addChildElement('rect', {'x':50, 'y':40, 'width':10, 'height':24})
    my_svg.addChildElement('rect', {'x':40, 'y':80, 'width':10, 'height':88})
    my_svg.addChildElement('rect', {'x':20, 'y':90, 'width':10, 'height':5})
    my_svg.addChildElement('rect', {'x':10, 'y':100, 'width':100, 'height':24})
    my_svg.addChildElement('circle', {'cx':120, 'cy':40, 'r':25})
  
  my_svg.outputToFile('static/test.svg')
  print numero

if __name__ == "__main__":
  app.run();
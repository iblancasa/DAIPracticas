#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web import form
from web.contrib.template import render_mako


urls = (
        '/','index'
        )

app = web.application(urls, globals(), autoreload=False)

render = render_mako(
        directories=['templates'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )


class index:
    def GET(self):
        graf="$(document).ready(function() { \n\
                var options = { \n\
                  chart: { \n\
                    type: 'column', \n\
                    renderTo: 'container', \n\
                    margin: 75, \n\
                    options3d: { \n\
                      enabled: true, \n\
                      alpha: 15, \n\
                      beta: 15, \n\
                      depth: 110 \n\
                    } \n\
                  }, \n\
                  title: { \n\
                    text: 'Demanda académica: extraordinaria de septiembre 2013' \n\
                  }, \n\
                  xAxis: { \n\
                    categories: [] \n\
                  }, \n\
                  yAxis: { \n\
                    title: { \n\
                      text: 'Solicitudes' \n\
                    } \n\
                  }, \n\
                  series: [] \n\
                }; \n\
                $.get('http://opendata.ugr.es/dataset/7f5a6a24-d1ab-42dc-a497-b429413760c6/resource/88c7eb60-d29a-4833-95da-8338ea64d1b2/download/pruebadeaccesoconvocatoriaextraordinariadeseptiembre.csv', function(data) { \n\
                  var lines = data.split('\\n'); \n\
                  var contar=0; \n\
                  $.each(lines, function(lineNo, line) { \n\
                    var items = line.split(',');\n\
                    if (lineNo == 0) {\n\
                      $.each(items, function(itemNo, item) {\n\
                        if (itemNo > 0) options.xAxis.categories.push(item);\n\
                      });\n\
                    }\n\
                    else {\n\
                      var series = {\n\
                        data:[],\n\
                      };\n\
                      $.each(items, function(itemNo, item) {\n\
                        if(item!=""){\n\
                          if (itemNo == 0) {\n\
                            series.name = item;\n\
                          } else{\n\
                            series.data.push(parseFloat(item.substring(1, item.length - 2)));\n\
                          }\n\
                        }\n\
                      });\n\
                      contar++;\n\
                      if(contar<=lines.length-2)\n\
                      options.series.push(series);\n\
                    }\n\
                  });\n\
                  var chart = new Highcharts.Chart(options);\n\
                });\n\
              });"


        return render.index(grafico=graf)



if __name__ == "__main__":
    app.run()

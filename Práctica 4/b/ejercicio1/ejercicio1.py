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
        graf="$(function () { \n\
            $('#container').highcharts({\n\
                chart: {\n\
                    type: 'column',\n\
                    margin: 75,\n\
                    options3d: {\n\
        				enabled: true,\n\
                        alpha: 15,\n\
                        beta: 15,\n\
                        depth: 110\n\
                    }\n\
                },\n\
                plotOptions: {\n\
                    column: {\n\
                        depth: 40,\n\
                        stacking: true,\n\
                        grouping: false,\n\
                        groupZPadding: 10\n\
                    }\n\
                },\n\
                series: []\n\
            });\n\
        });"


        return render.index(grafico=graf)



if __name__ == "__main__":
    app.run()

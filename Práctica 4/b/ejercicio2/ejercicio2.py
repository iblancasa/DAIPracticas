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
        return render.index()



if __name__ == "__main__":
    app.run()

import os

import cherrypy


class Endpoint(object):
    @cherrypy.expose
    def health(self):
        return "I'm up"

    @cherrypy.expose
    def upload(self):
        return "Crunching"


if __name__ == '__main__':
    static_dir = os.path.dirname(os.path.abspath(__file__)) + "/static"

    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8001,
    })
    conf = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': static_dir,
            'tools.staticdir.index': 'index.html'
        }
    }

    cherrypy.quickstart(Endpoint(), '/', config=conf)  # ..and LAUNCH ! :)

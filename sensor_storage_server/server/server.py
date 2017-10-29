from aiohttp import web

from sensor_storage_server.routes.routes import setup_routes

class Server:
    def __init__(self):
        self.app = web.Application()
        setup_routes(self.app)

    def run(self, host='127.0.0.1', port=8000):
        web.run_app(self.app, host=host, port=port)
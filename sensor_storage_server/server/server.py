from aiohttp import web

class Server:
    def __init__(self, host='127.0.0.1', port=8000):
        self.app = web.Application();
        web.run_app(self.app, host, port);
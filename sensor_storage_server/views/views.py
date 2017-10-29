from aiohttp import web

async def get_value_handler(request):
    return web.Response(text="Hello");

async def set_value_handler(request):
    return web.Response(text="Hello");
from sensor_storage_server.views.views import get_value_handler, set_value_handler

def setup_routes(app):
    app.router.add_get('/get_values', get_value_handler);
    app.router.add_post('/set_value/{time}/{value}/{unit}', set_value_handler);

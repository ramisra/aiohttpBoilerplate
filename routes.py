from controllers import test_controller


def setup_routes(app):
    app.router.add_get('/', test_controller.hello)


import asyncio
from aiohttp import web
from routes import setup_routes
from middleware import test_middleware

loop = asyncio.get_event_loop()
app = web.Application(loop=loop, middlewares=[test_middleware.authentication_middleware, test_middleware.error_middleware])
setup_routes(app)
web.run_app(app, host='127.0.0.1', port=8080)
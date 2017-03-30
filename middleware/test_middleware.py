import json
from aiohttp import web


def json_error(message):
    return web.Response(
        body=json.dumps({'error': message}).encode('utf-8'),
        content_type='application/json')

async def error_middleware(app, handler):
    async def middleware_handler(request):
        try:
            response = await handler(request)
            if response.status == 404:
                return json_error(response.message)
            return response
        except web.HTTPException as ex:
            if ex.status == 404:
                return json_error(ex.reason)
            raise
    return middleware_handler

# async def authentication_middleware(app,handler):
#     async def authentication_handler(request):
#         try:
#             if request.headers:
#                 raise Exception({"error": "Authentication failed"})
#         except Exception as ex:
#             return json_error("Authentication failed")
#     return authentication_handler

async def validation_middleware(app, handler):
    async def validation_handler(request):
        try:
            response = await handler(request)
            if response.status == 404:
                return json_error(response.message)
            return response
        except web.HTTPException as ex:
            if ex.status == 404:
                return json_error(ex.reason)
            raise
    return validation_handler

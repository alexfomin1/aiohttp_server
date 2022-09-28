import aiohttp_jinja2
import jinja2
from aiohttp import web

from app.store.database.accessor import PostgresAccessor
from app.settings import config, BASE_DIR

# config file
def setup_config(application):
    application['config'] = config

# url-routes
def setup_routes(application):
    from app.forum.routes import setup_routes as setup_forum_routes
    setup_forum_routes(application)

# templates dir
def setup_external_libraries(application: web.Application) -> None:
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader(f'{BASE_DIR}/templates'))

# db connect to app
def setup_accessors(application):
    application['db'] = PostgresAccessor()
    application['db'].setup(application)

# setup of the whole app
def setup_app(application):
    setup_config(application)
    setup_accessors(application)
    setup_external_libraries(application)
    setup_routes(application)

# create web-app
app = web.Application()

if __name__ == '__main__':
    setup_app(app)
    web.run_app(app, port=config['common']['port']) # run app
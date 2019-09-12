from .resources import TodoItem
from base import configure

api_bp, api = configure()
api.add_resource(TodoItem, 'todo')

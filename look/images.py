import falcon
import json


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


class Resource(object):
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(self, req, resp):
        # resp.data = msgpack.packb({'message': 'Hello world!'})#jsonify(tasks)
        resp.content_type = 'application/json'
        resp.body = json.dumps(dict(tasks = tasks))#'{"message": "Hello world!"}'
        # resp.data = msgpack.packb({'message': 'Hello world!'})
        # resp.content_type = 'application/msgpack'
        resp.status = falcon.HTTP_200

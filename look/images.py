import falcon

class Resource(object):

    def on_get(self, req, resp):
        resp.body = '{"message": "Hello world!"}'
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200

## Server that insert and select messages
from flask import Flask, request
from flask_restful import Api, Resource
import handler

app = Flask(__name__)
api = Api(app)

api.add_resource(handler.index, '/')
api.add_resource(handler.createMessage, '/message/new')
api.add_resource(handler.allMessages, '/message/show/all')
api.add_resource(handler.oneMessage, '/message/show/<id>')
api.add_resource(handler.updateMessage, '/message/edit/<id>')

if __name__ == '__main__':
    app.run(debug=True)

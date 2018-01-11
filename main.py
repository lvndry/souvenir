## Server that insert and select messages
from flask import Flask, request
from flask_restful import Api, Resource
import handler

## Api
app = Flask(__name__)
api = Api(app)

## Routes
api.add_resource(handler.index, '/')
api.add_resource(handler.createMessage, '/message/new')
api.add_resource(handler.allMessages, '/message/show/all', '/messages')
api.add_resource(handler.oneMessage, '/message/show/<id>')
api.add_resource(handler.updateMessage, '/message/edit/<id>')
api.add_resource(handler.deleteMessage, '/message/delete/<id>')

if __name__ == '__main__':
    app.run(debug=True)

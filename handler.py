## Handler files where all the functions of routes are called
from flask_restful import Resource, reqparse
import psycopg2
import json

conn = psycopg2.connect("dbname=feed user=postgres")
cur = conn.cursor()
parser = reqparse.RequestParser()
parser.add_argument('content')

class index(Resource):
    def get(self):
        print(cur.connection)
        return {'Response': 'Index page', 'Status': 200}

class createMessage(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            print(args)
            content = str(args['content'])
            cur.execute("INSERT INTO messages (content) VALUES (%s) RETURNING id", (content,))
            id = cur.fetchone()[0]
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return {'Id': id, 'Content': content, 'Status': 201}

class allMessages(Resource):
    def get(self):
        try:
            cur.execute("SELECT * FROM messages")
            data = cur.fetchall()
            json.dumps(data)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return {'Data': data, 'Status': 200}

class oneMessage(Resource):
    def get(self, id):
        try:
            cur.execute("SELECT * FROM messages WHERE id=%s", (id,))
            message = cur.fetchone()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return {'Message': message, 'Status': 201}

class updateMessage(Resource):
    def post(self, id):
        try:
            args = parser.parse_args()
            content = str(args['content'])
            cur.execute("UPDATE messages SET content=%s WHERE id=%s", (content, id))
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return {'Update': content, 'Status': 201}

class deleteMessage(Resource):
    def delete(self, id):
        try:
            cur.execute("DELETE FROM messages WHERE id=%s", (id,))
            row = cur.rowcount
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return {'Delete': row, 'Status': 201}

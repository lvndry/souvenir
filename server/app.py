"""
Keep your memories intact
Simple CRUD implementation with Flask
"""
from flask import Flask, request, render_template, make_response, jsonify
import json
import psycopg2
import datetime

conn = psycopg2.connect('dbname=souvenir user=postgres')
cur = conn.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    headers = {'Content-Type': 'text/html'}
    return render_template('new.html', title='Souvenir'), 200, headers

@app.route('/memory/new', methods=['POST'])
def createMessage():
    print(request)
    try:
        if request.form['memory']:
            memory = request.form['memory']
            date = request.form['date']
            print(memory)
            print(date)
            print(type(date))
            cur.execute('INSERT INTO memories (memory, date) VALUES (%s, %s) RETURNING id', (memory, date))
            id = cur.fetchone()[0]
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return jsonify(memory=memory, status=200)

@app.route('/memory/show/all', methods=['GET'])
def getAllMessages():
    try:
        cur.execute('SELECT id, memory, date FROM memories')
        data = cur.fetchall()
        json.dumps(data)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return make_response(render_template('all.html', memories=data), 200)

@app.route('/memory/show/<id>', methods=['GET'])
def showOne(id):
    try:
        cur.execute('SELECT * FROM memories WHERE id=%s', (id,))
        memory = cur.fetchone()
        json.dumps(memory)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return make_response(render_template('single.html', memory=memory), 200)

@app.route('/memory/edit/<id>', methods=['PUT'])
def editMessage(id):
    try:
        memory = request.form['memory']
        date = request.form['memory']
        cur.execute('UPDATE memories SET content=%s WHERE id=%s', (memory, id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return jsonify(memory=memory, status=200)

@app.route('/memory/delete/<id>', methods=['DELETE'])
def deleteMessage(id):
    try:
        cur.execute('DELETE FROM memories WHERE id=%s', (id,))
        row = cur.rowcount
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return jsonify(delete=row, status=200)

if __name__ == '__main__':
    app.run(debug=True)

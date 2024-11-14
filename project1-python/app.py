from flask import Flask, request
from dbquery import insert, select, update
import sqlite3 as sql

app = Flask(__name__)

# CRUD - Create, Read (Return), Update, Delete

# GET /articles         - Return all articles
# GET /articles/id      - Return specific article 
# all filtering needs to be in the body of the request
# TODO currently only supports AND filtering
# TODO currently only supports one filter per key
# TODO does not handle mis-named column filters
@app.route("/articles/", methods=['GET'])
@app.route("/articles/<id>", methods=['GET'])
def get_article(id=None):
        data = request.get_json() if request.is_json else {}
        if id: data.update({'id':int(id)})
        return select('database.db', 'articles', **data)

# POST /articles        - Create new article
@app.route("/articles/", methods=['POST'])
def post_article():
        data = request.get_json()
        return insert('database.db', 'articles', data)

# PUT /articles         - Create new article
# PUT /articles/id      - Create/update article where id=id
@app.route("/articles/", methods=['PUT'])
@app.route("/articles/<id>", methods=['PUT'])
def update_article(id=None):
        data = request.get_json()
        data.update({'id':int(id)})
        print(data)
        if not id :
                print ('no id presented, creating new article:')
                return insert('database.db', 'articles', data)
        exists = select('database.db', 'articles', id=int(id))
        if exists[1] != 200:
                print('error while getting article')
                return exists
        elif not exists[0] : 
                print('id DOES NOT exist in db')
                return insert('database.db','articles',data)
        else: 
                print('id exists in db, updating entry')
                return update('database.db','articles', id, data)

# DELETE /articles/id   - Delete a single article
@app.route("/pets/<id>", methods=['DELETE'])
def delete_article(id):
        return delete('database.db', 'articles', int(id))

from flask import Flask, request
from dbquery import insert, select, update, delete
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
def get_article():
        data = request.get_json() if request.is_json else {}
        data.update(request.args.to_dict())
        return select('database.db', 'articles', **data)

# POST /articles        - Create new article
@app.route("/articles/", methods=['POST'])
def post_article():
        data = request.get_json() if request.is_json else {}
        data.update(request.args.to_dict())
        return insert('database.db', 'articles', data)

# PUT /articles         - Create new article
# PUT /articles?id      - Create/update article where id=id
@app.route("/articles/", methods=['PUT'])
def update_article():
        data = request.get_json() if request.is_json else {}
        data.update(request.args.to_dict())
        
        id = data.get('id')
        
        if not id :
                return insert('database.db', 'articles', data)

        exists = select('database.db', 'articles', id=id)

        if exists[1] != 200:
                return exists
        elif not exists[0] : 
                return insert('database.db','articles',data)
        else: 
                return update('database.db','articles', id, data)

# DELETE /articles/id   - Delete a single article
@app.route("/articles/<id>", methods=['DELETE'])
def delete_article(id):
        return delete('database.db', 'articles', id)

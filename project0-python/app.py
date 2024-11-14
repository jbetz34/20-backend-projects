from flask import Flask, request
from dbquery import new_pet, new_owner, select
import sqlite3 as sql

app = Flask(__name__)

@app.route("/pets/", methods=['POST'])
def add_pet():
        data = request.get_json()
        return select('database.db', 'pets', **data)

@app.route("/owners/", methods=['POST'])
def add_owner():
        data = request.get_json()
        return select('database.db', 'owners', **data)

@app.route("/owners/", methods=['GET'])
@app.route("/owners/<id>", methods=['GET'])
def get_owners(id=None):
        args = {'id':id} if id else {}
        return select('database.db', 'owners', **args)

@app.route("/pets/", methods=['GET'])
@app.route("/pets/<id>", methods=['GET'])
def get_pets(id=None):
        args = {'id':id} if id else {}
        return select('database.db', 'pets', **args)

@app.route("/owners/<id>/pets/", methods=['GET'])
def get_owner_pets(id):
        return select('database.db', 'pets', owner_id=id)

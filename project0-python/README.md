# Pet Tracker API

Pet Tracker API is meant to track pets and their owners. The relationship between owners and pets is one to many. 

![pet tracker diagram](/docs/images/pet_tracker.jpeg)

*Technical Details*
- The API http routing is built using python Flask
- The database behind the API is built using sqlite3

*Directory Description*
- app.py : defines the http routing functionality
- dbconfig.ini : an attempt to define the database schemas using configparser
- dbinit.py : python script that initializes the database.db file
- dbquery.py : generalized sql query/insert functions used in app.py
- database.db (created on-demand) : database file that tracks POST requests

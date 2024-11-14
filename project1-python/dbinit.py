import sqlite3 as sql
import configparser

# Read database configuration from config file
config = configparser.ConfigParser()
config.read('dbconfig.ini')

db_name = config.get('database', 'name')

# Create a connection to the database (creates the db if it doesn't exist)
conn = sql.connect(db_name)
cursor = conn.cursor()

# Create tables based on config file (if needed)
auto_columns = [ f"{key} {value}" for key, value in config.items('_auto') ] if '_auto' in config else []

for section in config.sections():
    if section != 'database' and section != '_auto':
        table_name = section
        columns = [] + auto_columns
        for key, value in config.items(section):
            columns.append(f"{key} {value}")
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        cursor.execute(create_table_query)

# Commit changes and close connection
conn.commit()
conn.close()

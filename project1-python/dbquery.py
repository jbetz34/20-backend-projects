import sqlite3 as sql

def delete(database, table, id):
        '''
        Generic insert function that attempts to connect to the database and insert a new record
        Parameters: 
                database [string]       - database file or :memory:
                table    [string]       - table to delete from
                id       [integer]      - article id to delete
        Returns:
                204 - on success
                500 - on failure
        '''
        sql_statement = 'DELETE FROM %s WHERE id = %s' % (table, id)
        print("DELETE:")
        print(sql_statement)
        try: 
                with sql.connect(database, detect_types=1) as conn:
                        cur = conn.cursor()
                        cur.execute(sql_statement, data)
                        conn.commit()
                return select('database.db', table, id=cur.lastrowid)[0], 200
        except sql.OperationalError as e:
                return "Failed to delete record:" + str(e), 500
        
                

def update(database, table, id, data):
        '''
        Generic insert function that attempts to connect to the database and insert a new record
        Parameters: 
                database [string]       - database file or :memory:
                table    [string]       - table to insert values into
                id       [integer]      - article id to update
                data     [dict]         - data to insert into the table record
        Returns:
                204 - on success
                500 - on failure
        '''
        sql_statement = 'UPDATE OR REPLACE %s ' % table
        sql_statement += 'SET ' + ', '.join([str(k) + ' = "' + str(v) + '" ' for k,v in data.items()])
        sql_statement += 'WHERE id = ' + str(id)
        # pls god find a way to make this cleaner
        print("UPDATE:")
        print(sql_statement)
        try: 
                with sql.connect(database, detect_types=1) as conn:
                        cur = conn.cursor()
                        cur.execute(sql_statement, data)
                        conn.commit()
                return select('database.db', table, id=cur.lastrowid)[0], 200
        except sql.OperationalError as e:
                return "Failed to update record:" + str(e), 500

def insert(database, table, data):
        '''
        Generic insert function that attempts to connect to the database and insert a new record
        Parameters: 
                database [string]       - database file or :memory:
                table    [string]       - table to insert values into
                data     [dict]         - data to insert into the table record
        Returns:
                201 - on success
                500 - on failure
        '''
        sql_statement = 'INSERT INTO '
        sql_statement += table + ' ( ' + ', '.join(data.keys()) + ') ' # column names
        sql_statement += 'VALUES ( :' + ', :'.join(data.keys()) + ') ' # column values
        print("INSERT:")
        print(sql_statement)
        try: 
                with sql.connect(database, detect_types=1) as conn:
                        cur = conn.cursor()
                        cur.execute(sql_statement, data)
                        conn.commit()
                return select('database.db', table, id=cur.lastrowid)[0], 201
        except sql.OperationalError as e:
                return "Failed to create new record:" + str(e), 500

def select(database, table, **kwargs):
        '''
        Generic select function that attempts to connect to the database and run a query
        Parameters: 
                database [string]       - database file or :memory:
                table    [string]       - table to insert values into
                kwargs   [dict]         - dict used to build WHERE clause
        Returns:
                200 - on success
                500 - on failure
        '''
        sql_statement = 'SELECT * FROM %s' % table
        print("SELECT:")
        print(kwargs)
        if kwargs:
                sql_statement += ' WHERE ' + ' AND '.join(["%s = %s" % (x) for x in kwargs.items()]) 
        print(sql_statement)
        try:
                with sql.connect(database) as conn:
                        conn.row_factory = sql.Row
                        cur = conn.cursor()
                        data = [ dict(x) for x in cur.execute(sql_statement) ]
                return data , 200
        except sql.OperationalError as e:
                return "Failed to retrieve record:" + str(e), 500

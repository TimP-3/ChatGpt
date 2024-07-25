import sqlite3 

class ChatGPTDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        '''

        creates a new table in the database with given name and column

        '''

        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name}({columns})"
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def insert_record(self, table_name, colums, record):
        '''
        Insert a record to a target with values separate by comm
        '''
        sql = f'INSERT INTO {table_name} ({colums}) VALUES ({record})'
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    # def create_table(self, table_name, columns):
    #     "Creates a new table in the database with the given name. The columns parameter should be a comma-separated string"
    #     create_table_sq1 = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    #     self.cursor.execute(create_table_sq1)
    #     self.conn.commit()

    # def insert_record(self, table_name, columns, record):
    #     "Insert a record to target table with values separate by a comma"
    #     sq1 = f'INSERT INTO {table_name} ({columns}) VALUES ({record})'
    #     self.cursor.execute(sq1)
    #     self.conn.commit()

    # def retrieve_records(self, table_name, conditions=None):
    #     "Retrieves all records from the specified table in the database. The conditions parameter should be a string that represents a SQ"

    #     select_sq1 = f"SELECT * FROM {table_name}"
    #     if conditions: 
    #         select_sq1 += f" WHERE {conditions}"
    #     self.cursor.execute(select_sq1)
    #     return self.cursor.fetchall()
    
    # def close(self):
    #     self.cursor.close()
    #     self.conn.close()
    
    # def __exit__(self, exc_type, exc_value, trace):
    #     print('close')
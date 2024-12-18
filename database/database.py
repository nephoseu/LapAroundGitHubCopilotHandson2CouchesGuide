import psycopg2

class Database:
    def __init__(self,connection_string):
        self.conn = None
        self.cursor = None
        self.connection_string = connection_string
        self.connect()

    ## __enter__ and __exit__ methods are used to make the Database class a context manager
    ## This will be mandatory if copilot generates code to use with self.db  which requires the Database class to be a context manager

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()  # Rollback on error
        else:
            self.conn.commit()  # Commit on success
        pass

    def connect(self):
        self.conn = psycopg2.connect(self.connection_string)
        self.conn.autocommit = False
        self.cursor = self.conn.cursor()
        
    def execute(self, query, params=()):
        with self.conn:
            self.cursor.execute(query, params)
        return self

    def fetchall(self): 
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

import os
import sqlite3

DATA_BASE_PATH = "./database/pedrada.db"
SQL_PATH = "./database/pedrada.sql"

class SQLite_Connector:
    """Provides methods to connect to a SQLite database, 
        create tables, execute SQL queries, and close the 
        database connection  
    """

    def __init__(self, db_name:str = DATA_BASE_PATH) -> None:
        self.db_name = db_name
        self.connection : sqlite3.Connection = None 
        self.cursor : sqlite3.Cursor = None 
        self.db_exit = os.path.isfile(self.db_name)
        self.sqlite_connect()
        self.create_tables()
         
        
    def create_tables(self) -> None:
        """Reads an SQL script from a file, 
            executes the script using the SQLite connection  
        """
        if not os.path.isfile(SQL_PATH):
            print("[FATAL ERROR] SQL script not found")
            exit(-1)

        sql_file = open(SQL_PATH)
        sql_as_string = sql_file.read()
        self.cursor.executescript(sql_as_string)
        print("[INFO] All tables Created")

    def sqlite_connect(self) -> None:
        """Connect to a database, if it does not exist it will be created
        """
        print("[INFO] Start database connection")

        try:
            self.connection = sqlite3.connect(self.db_name, check_same_thread=False)
        except sqlite3.Error:
            print("[FATAL ERROR] Database connection error")
            exit(-1)
        self.cursor = self.connection.cursor()

    def execute_sql_query(self, query: str, apply_data_schema) -> list:
        """Takes an SQL query as input and applies a data schema 
            to the results fetched by the cursor object
        """
        results = self.cursor.execute(query)
        self.connection.commit()

        return apply_data_schema(results.fetchall())
    
    def close_db(self) -> None:
        """Commits any pending changes to the database 
            and closes the connection
        """
        self.connection.commit()
        self.connection.close()



from flask import Response
from database.db_connector import SQLite_Connector
from schemas.schemas import Schema
from src.erro_message import ErrorMessage
from src.success_message import SuccessMessage
from dotenv import load_dotenv

class Community(SQLite_Connector):
    def __init__(self, db_name: str = ...) -> None:
        super().__init__()
    
    def get_community(self, public_id: str = None) -> Response:
        # if public_id:
        #     sql_query = f"SELECT * FROM community WHERE public_id='{public_id}"
        #     users = self.execute_sql_query(sql_query, Schema.user)
        # else:
        #     sql_query = "SELECT * FROM user"
        #     users = self.execute_sql_query(sql_query, Schema.user)

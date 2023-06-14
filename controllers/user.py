from flask import Response
from sqlite3 import IntegrityError
from database.db_connector import SQLite_Connector
from schemas.schemas import Schema
from src.erro_message import ErrorMessage
from src.success_message import SuccessMessage

import bcrypt
import uuid
import datetime


class UserController(SQLite_Connector):
    def __init__(self, db_name: str = ...) -> None:
        super().__init__()
    
    def get_user(self, filter: str , filter_type: str) -> Response:

        if filter_type:
            sql_query = f"SELECT * FROM user WHERE {filter_type}=?"
            query_values = (filter,)
            users = self.execute_sql_query(sql_query, query_values, Schema.user)
        else:
            sql_query = "SELECT * FROM user"
            users = self.execute_sql_query(sql_query,(),Schema.user)
            
        return Schema.api_response(status=200, data=users)

    def create_user(self, user_data:dict) -> Response:
        pseudonym = user_data["pseudonym"]
        user_password = user_data["user_password"]
        email = user_data["email"]

        public_id = str(uuid.uuid4())
        hash_password = bcrypt.hashpw(user_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        registration_date =  datetime.datetime.now().date().strftime("%Y-%m-%d")
        
        sql_query = f"""
            INSERT INTO user (public_id, pseudonym, email, user_password,registration_date) 
            VALUES (?,?,?,?,?);
            """
        query_values = (public_id,pseudonym,email,hash_password,registration_date)

        try:
            new_user = self.execute_sql_query(sql_query,query_values,Schema.user)
        except IntegrityError as error:
            if "UNIQUE constraint failed: user.pseudonym" == str(error):
                return Schema.api_response(
                    status=403, #500 
                    error_message=[ErrorMessage.pseudonym_already_exist.value]
                )

            if "UNIQUE constraint failed: user.email" == str(error):
                return Schema.api_response(
                    status=403,
                    error_message=[ErrorMessage.email_already_exist.value]
                )      
        return  Schema.api_response(status=201, success_message=[SuccessMessage.new_user.value])

        
       
from flask import Response
from sqlite3 import IntegrityError
from database.db_connector import DATA_BASE_PATH, SQLite_Connector
from schemas.schemas import Schema
from src.erro_message import ErrorMessage
from src.success_message import SuccessMessage
from src.token_manager import get_public_id

import datetime

#Post types
IDENTIFIED = "identified"
COMMUNITY = "community" 

class PostController(SQLite_Connector):
    def __init__(self, db_name: str = ...) -> None:
        super().__init__()
    
    def get_post(self, public_id) -> Response:
        if public_id:
            sql_query = f"SELECT * FROM post WHERE public_id=?"
            query_values = (public_id,)
            posts = self.execute_sql_query(sql_query, query_values,Schema.posts)
        else:
            sql_query = "SELECT * FROM post"
            posts = self.execute_sql_query(sql_query,(),Schema.posts)
        
        return Schema.api_response(status=200, data=posts)
    
    def create_post(self, data: dict) -> Response:
        token = data["token"]
        owner_public_id = get_public_id(token)
        identified_public_id = data["identified_public_id"]
        community_public_id = data["community_public_id"]
        post_description = data["post_description"]
        post_type = data["post_type"]
        post_time = datetime.datetime.utcnow()
        post_date = post_time.date().strftime("%Y-%m-%d")

        if post_type == IDENTIFIED:
            sql_query = f"""
            INSERT INTO post (owner_public_id, identified_public_id, post_description, post_time, post_date,post_type) 
            VALUES (?,?,?,?,?,?);"""
            query_values = (owner_public_id, identified_public_id, post_description, post_time, post_date,post_type)
            new_post = self.execute_sql_query(sql_query,query_values,Schema.posts)

            return Schema.api_response(status=200, success_message=[SuccessMessage.new_identified_post.value])

        elif post_type == COMMUNITY:
            sql_query = f"""
            INSERT INTO post (owner_public_id, community_public_id, post_description, post_time, post_date,post_type) 
            VALUES (?,?,?,?,?,?);"""
            query_values = (owner_public_id, community_public_id, post_description, post_time, post_date,post_type)
            new_post = self.execute_sql_query(sql_query,query_values,Schema.posts)

            return Schema.api_response(status=200, success_message=[SuccessMessage.new_community_post.value])
        
        #confirmar status code 
        return Schema.api_response(status=403,error_message=[ErrorMessage.invalid_post_type.value])



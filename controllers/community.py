from flask import Response
from sqlite3 import IntegrityError
from database.db_connector import SQLite_Connector
from schemas.schemas import Schema
from src.erro_message import ErrorMessage
from src.success_message import SuccessMessage
from src.token_manager import get_public_id

import uuid
import datetime
class CommunityController(SQLite_Connector):
    def __init__(self, db_name: str = ...) -> None:
        super().__init__()
    
    def get_community_by_name(self, name: str = None) -> Response:
        if name:
            sql_query = f"SELECT * FROM community WHERE community_name=?"
            query_values = (name,)
            community = self.execute_sql_query(sql_query, query_values,Schema.community)

            if not community:
                return Schema.api_response(status=404)

            sql_query = f"SELECT * FROM post WHERE community_public_id=?"
            query_values = (community[0]["public_id"],)
            community_posts = self.execute_sql_query(sql_query, query_values,Schema.posts)
            return Schema.api_response(status=200, data=[community,community_posts])
        else:
            sql_query = "SELECT * FROM community"
            community = self.execute_sql_query(sql_query,(),Schema.community)
            return Schema.api_response(status=200, data=community)
        
    def get_community_by_id(self,public_id: str = None) -> Response:
        if public_id:
            sql_query = f"SELECT * FROM community WHERE public_id=?"
            query_values = (public_id,)
            community = self.execute_sql_query(sql_query, query_values,Schema.community)

            if not community:
                return Schema.api_response(status=404)

            sql_query = f"SELECT * FROM post WHERE community_public_id=?"
            query_values = (public_id,)
            community_posts = self.execute_sql_query(sql_query, query_values,Schema.posts)
            return Schema.api_response(status=200, data=[community,community_posts])
        else:
            sql_query = "SELECT * FROM community"
            community = self.execute_sql_query(sql_query,(),Schema.community)
            return Schema.api_response(status=200, data=community)
        
    
    def create_community(self, community_data:dict) -> Response:
        token = community_data["token"]
        community_name = community_data["community_name"]
        founder_id = get_public_id(token)
        community_description = community_data["community_description"]
        public_id = str(uuid.uuid4())
        foundation_date =  datetime.datetime.now().date().strftime("%Y-%m-%d")
        
        sql_query = f"""
            INSERT INTO community (community_name, founder_id, community_description, public_id, foundation_date) 
            VALUES (?,?,?,?,?);"""
        query_values = (community_name, founder_id, community_description, public_id, foundation_date)
        try:
            new_community = self.execute_sql_query(sql_query,query_values,Schema.community)
        except IntegrityError as error:
            if "UNIQUE constraint failed: community.community_name" == str(error):
                return Schema.api_response(
                    status=403, #500 
                    error_message=[ErrorMessage.community_already_exist.value]
                )
        return  Schema.api_response(status=201, success_message=[SuccessMessage.new_community.value])

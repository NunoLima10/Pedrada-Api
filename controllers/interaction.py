from flask import Response
from sqlite3 import IntegrityError
from database.db_connector import DATA_BASE_PATH, SQLite_Connector
from schemas.schemas import Schema
from src.erro_message import ErrorMessage
from src.success_message import SuccessMessage


class InteractionController(SQLite_Connector):
    def __init__(self, db_name: str = ...) -> None:
        super().__init__()
    
    def get_interaction(self, post_public_id) -> Response:
        sql_query = f"SELECT * FROM post_interaction WHERE post_id=?"
        query_values = (post_public_id,)
    
        interaction = self.execute_sql_query(sql_query, query_values,Schema.interaction)
        return  Schema.api_response(status=200, data=interaction)
    
    def create_post_interaction(self, interaction_data: dict) -> Response:
        token = interaction_data["token"]
        user_id = "9fecfe88-043c-4334-ad8d-de4dc3a5b17e"
        post_id = interaction_data["post_id"]
        interaction = interaction_data["interaction"]

        sql_query = f"""
            INSERT OR REPLACE INTO post_interaction (post_id, user_id, interaction) 
            VALUES (?,?,?);"""
        query_values = (post_id,user_id,interaction)
        self.execute_sql_query(sql_query, query_values,Schema.interaction)
        return  Schema.api_response(status=201, success_message=[SuccessMessage.new_interaction.value])



    

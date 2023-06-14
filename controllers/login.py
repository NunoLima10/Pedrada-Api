from database.db_connector import SQLite_Connector
from schemas.schemas import Schema
from src.erro_message import ErrorMessage
from src.success_message import SuccessMessage
from src.token_manager import generate_token,validade_token

from flask import Response
import bcrypt


class LoginController(SQLite_Connector):
    def __init__(self, db_name: str = ...) -> None:
        super().__init__()

    def validade_token(self, token: str) -> Response:
        if validade_token(token):
            token_status = {"is_valid": True}
            return Schema.api_response(status=200, data=token_status, success_message=[SuccessMessage.valid_token.value])
        else:
            token_status = {"is_valid": False}
            return Schema.api_response(status=401, data=token_status, error_message=[ErrorMessage.invalid_token.value])
       
    def validade_login(self, login_data :dict) -> Response :
        pseudonym :str =  login_data["pseudonym"]
        user_password :str =  login_data["user_password"]
        
        sql_query = f"SELECT * FROM user WHERE pseudonym=?"
        query_values =  (pseudonym,)
        user = self.execute_sql_query(sql_query,query_values, Schema.user)
        
        if not user:
            return Schema.api_response(status=403,
                error_message=[ErrorMessage.failed_login.value]
            )
        
        valide_password = bcrypt.checkpw(
            user_password.encode("utf-8"),
            user[0]["user_password"].encode("utf-8")
        )
        
        if valide_password:
            
            self.token  = generate_token(user[0]["public_id"])
            return Schema.api_response(status=200,data={"token": self.token},
                    success_message=[SuccessMessage.login.value]
            )
        else:
            return Schema.api_response(status=403,
                    error_message=[ErrorMessage.failed_login.value]
            )
        
            

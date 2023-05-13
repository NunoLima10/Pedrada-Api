from database.db_connector import SQLite_Connector
from schemas.schemas import Schema
from src.erro_message import ErrorMessage
from src.success_message import SuccessMessage
from dotenv import load_dotenv

import jwt
import bcrypt
import datetime
import os

load_dotenv("./.env")
SECRETE_KEY = os.getenv("SECRETE_KEY")

class LoginController(SQLite_Connector):
    def __init__(self, db_name: str = ...) -> None:
        super().__init__()
    
    def generate_token_payload(self, pseudonym: str) -> dict:
        duration = 1
        expiry_time = datetime.datetime.utcnow() + datetime.timedelta(days=duration)
        return {"pseudonym": pseudonym, "expiry_time": expiry_time.timestamp()}
    
    def validade_login(self, login_data :dict)-> dict:
        pseudonym :str =  login_data["pseudonym"]
        user_password :str =  login_data["user_password"]
        
        sql_query = f"SELECT * FROM user WHERE pseudonym=?"
        query_values =  (pseudonym,)
        user = self.execute_sql_query(sql_query,query_values,Schema.user)
        
        if not user:
            return Schema.api_response(
                status=403,
                error_message=[ErrorMessage.failed_login.value]
            )
        
        valide_password = bcrypt.checkpw(
            user_password.encode("utf-8"),
            user[0]["user_password"].encode("utf-8")
        )
        
        if valide_password:
            token_payload = self.generate_token_payload(user[0]["pseudonym"])
            token = jwt.encode(token_payload,SECRETE_KEY)

            return Schema.api_response(
                status=200,
                data={"token":token},
                success_message=[SuccessMessage.login.value]
            )
        else:
            return Schema.api_response(
                status=403,
                error_message=[ErrorMessage.failed_login.value]
            )
            

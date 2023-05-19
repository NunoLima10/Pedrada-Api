from database.db_connector import SQLite_Connector
from schemas.schemas import Schema
from src.erro_message import ErrorMessage
from src.success_message import SuccessMessage
from dotenv import load_dotenv

import jwt
from flask import Response
import bcrypt
import datetime
import os

load_dotenv("./.env")
SECRETE_KEY = os.getenv("SECRETE_KEY")
ALGORITHM = "HS256"

class LoginController(SQLite_Connector):
    def __init__(self, db_name: str = ...) -> None:
        super().__init__()
    
    def generate_token_payload(self, pseudonym: str) -> dict:
        duration = 1
        expiry_time = datetime.datetime.utcnow() + datetime.timedelta(days=duration)
        return {"pseudonym": pseudonym, "expiry_time": expiry_time.timestamp()}

    def validade_token(self, token: str) -> Response:
        try:
            payload = jwt.decode(jwt=token, key=SECRETE_KEY,verify=True,algorithms=[ALGORITHM])
            token_status = {
                "is_valid": payload['expiry_time'] > datetime.datetime.utcnow().timestamp()
            }
            return Schema.api_response(status=200, data=token_status,success_message=[SuccessMessage.valid_token.value])
        
        except jwt.InvalidTokenError:
            token_status = {"is_valid": False}
            return Schema.api_response(status=401, data=token_status,error_message=[ErrorMessage.invalid_token.value])
       
    def validade_login(self, login_data :dict)-> Response :
        pseudonym :str =  login_data["pseudonym"]
        user_password :str =  login_data["user_password"]
        
        sql_query = f"SELECT * FROM user WHERE pseudonym='{pseudonym}'"
        user = self.execute_sql_query(sql_query, Schema.user)
        
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
            token = jwt.encode(payload=token_payload,key=SECRETE_KEY,algorithm=ALGORITHM)
            self.token  = token
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
        
            

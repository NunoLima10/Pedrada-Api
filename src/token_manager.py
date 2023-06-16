from dotenv import load_dotenv
import jwt
import datetime
import os

load_dotenv("./.env")
SECRETE_KEY = os.getenv("SECRETE_KEY") or "SECRETE_KEY"
ALGORITHM = "HS256"
VALID_DURATION_TIME = 1 #days

def generate_token(public_id: str) -> dict:
        expiry_time = datetime.datetime.utcnow() + datetime.timedelta(days=VALID_DURATION_TIME)
        token_payload = {"public_id": public_id, "expiry_time": expiry_time.timestamp()}
        return jwt.encode(payload=token_payload,key=SECRETE_KEY,algorithm=ALGORITHM)

def validade_token(token: str) -> bool:
        try:
            payload = jwt.decode(jwt=token, key=SECRETE_KEY,verify=True,algorithms=[ALGORITHM])
            return  payload['expiry_time'] > datetime.datetime.utcnow().timestamp()
        except jwt.InvalidTokenError:
            return False

def get_public_id(token: str) -> str:
        payload = jwt.decode(jwt=token, key=SECRETE_KEY,verify=True,algorithms=[ALGORITHM])
        return  payload['public_id']
      
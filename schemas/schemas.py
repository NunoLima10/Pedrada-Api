from flask import make_response, Response

class Schema:
    
    @staticmethod
    def user(data: tuple) -> list:
        return [
        {"id": dt[0],
        "public_id": dt[1],
        "pseudonym": dt[2],
        "e_mail": dt[3],
        "user_password": dt[4],
        "registration_date":dt[5],
        }  for dt in data] 
    
    @staticmethod
    def api_response(status: int, data=[], success_message=[], error_message=[]) -> Response:
        response =  {
            "success_message": [{index+1: message} for index, message in enumerate(success_message)],
            "error_message": [{index+1: error} for index, error in enumerate(error_message)],
            "data": data
        }
        return make_response(response,status)
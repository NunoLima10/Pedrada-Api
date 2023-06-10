from flask import make_response, Response

class Schema:
    
    @staticmethod
    def user(data: tuple) -> list:
        return [
        {
        "public_id": dt[1],
        "pseudonym": dt[2],
        "e_mail": dt[3],
        "user_password": dt[4],
        "registration_date":dt[5],
        }  for dt in data][0] 
    @staticmethod
    def community(data: tuple) -> list:
        return[
        {
        "community_name": dt[1],
        "public_id": dt[2],
        "founder_id": dt[3],
        "foundation_date": dt[4],
        "community_description":dt[5],
        }  for dt in data]
    
    @staticmethod
    def posts(data: tuple) -> list:
        if not data: return []
        return [
            {
            "owner_public_id":dt[1],
            "identified_public_id":dt[2],
            "community_public_id":dt[3],
            "post_description": dt[4],
            "post_time": dt[5],
            "post_date":dt[6],
            "post_type":dt[7]
        }
        for dt in data]

    @staticmethod
    def api_response(status: int, data=[], success_message=[], error_message=[]) -> Response:
        response =  {
            "success_message": [{index+1: message} for index, message in enumerate(success_message)],
            "error_message": [{index+1: error} for index, error in enumerate(error_message)],
            "data": data
        }
        return make_response(response,status)
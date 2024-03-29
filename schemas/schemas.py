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
        }  for dt in data]
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
        return [
            {
            "owner_public_id":dt[1],
            "public_id":dt[2],
            "identified_public_id":dt[3],
            "community_public_id":dt[4],
            "post_description": dt[5],
            "post_time": dt[6],
            "post_date":dt[7],
            "post_type":dt[8]
        }
        for dt in data]
    def interaction(data: tuple) -> list:
        return [
            {
            "post_id":dt[1],
            "user_id":dt[2],
            "interaction":dt[3],
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
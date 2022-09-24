import datetime
import time
from typing import Any , Dict , Optional , List
import jwt 
from jwt.exceptions import ExpiredSignatureError

class GenerateToken:
    #! Generating new refresh and access token pair with the given arguments  
    def encode(
        payload: Dict[str, Any],
        key: str,
        algorithm: Optional[str] = "HS256", 
        headers: Optional[Dict[str, Any]] = None,
        ):
        payload_data = payload.copy()
        payload_data.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(days=2)})
        access_token = jwt.api_jwt.encode(payload,key,algorithm,headers)
        refresh_token = jwt.api_jwt.encode(payload_data,key,algorithm,headers)
        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}") 

    #! Evaluate if the refresh token has expired or not
    def evaluate_refresh_token(
        token: str,
        key: str = "",
        algorithms: Optional[List[str]] = None,
        ):
        token = jwt.api_jwt.decode(token,key,algorithms)
        current_time = time.mktime(datetime.datetime.utcnow().timetuple())
        if token["exp"] < current_time:
            raise ExpiredSignatureError
        else:
            expiration_dt = datetime.datetime.utcnow() + datetime.timedelta(minutes=50)
            td_to_timestamp = time.mktime(expiration_dt.timetuple()) 
            td_to_timestamp = int(td_to_timestamp)
            token["exp"] = td_to_timestamp
            access_token = GenerateToken.encode(token,key,"HS256")
            return("Done!")

            
            
#! First write a payload then key and after that algorithm for signing token, finally run the program
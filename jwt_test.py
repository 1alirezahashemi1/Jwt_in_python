import jwt
from cryptography.hazmat.primitives import serialization

# Generation a simple symmetrical token == HS256 
# scenario 1
payload_data = {
    "name": "alireza",
    "age":20
}

# token = jwt.api_jwt.encode(
#     payload=payload_data,
#     key = "38j8edj9934jh834hu4gh74gb478g3983ye8dfrjh456k97m",
# ) 
# print(token)



#? Generating a token with asymmetrical algorithm == RS256
#? scenario 2

private_key = open("Jwt","r").read()

key = serialization.load_ssh_private_key(
    private_key.encode(),
    password= b''
)

token = jwt.api_jwt.encode(
    payload= payload_data,
    key = key,
    algorithm="RS256" 
)
print(token)
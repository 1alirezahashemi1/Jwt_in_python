import jwt 
from cryptography.hazmat.primitives import serialization

#! Uncomment every part of program than you want to execute



# #! Decoding token (it will work if the token has verified)

# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYWxpcmV6YSIsImFnZSI6MjB9.2Iwh8AGc61N2firG72zYjwfzl8FGnUxMiEQo7p320JY"
# token_decoded = jwt.api_jwt.decode(
#             token,
#             key = "38j8edj9934jh834hu4gh74gb478gdfrjh456k97m",
#             algorithms=["HS256" , ]
# )
# print(token_decoded)



#! Looking for the header of unverified token

# token =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiYWxpcmV6YSIsImFnZSI6MjB9.2Iwh8AGc61N2firG72zYjwfzl8FGnUxMiEQo7p320JY"

# tokens_header = jwt.get_unverified_header(token)
# print(tokens_header)



#! Decoding a token with RS258 algorithm

# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYW1lIjoiYWxpcmV6YSIsImFnZSI6MjB9.EU10B7CY9bJ2D-eTPWc6YCk8F33ikebyd7iQKRk0OKoAisY7LzttWZPssIj_IGdx4Y9TTpsbNJrqXqVH1QYanvd8Xkch39ATAaY5dXkSt8Iw4_iOJjt8zq7BPXeQ158oLUObtnHzvENocnKdoEUl_BWE2dXMt7MFx9NH7sTJKMKTihX4-Lpsv0V1QY3cZfHyZKfXmttjxr59ZOltx0mPxLq3paO57tHxW4rBXESitk45jANAQQ6zK7OatfgKFwmQ_pt_JHgksL0awLWFFzLqsWkSO5PyfR3n1FEPdrPXeu0AiA1WmCdSOC2DX8fiScJvYPUphy-m1_WGV27MbxjUh0EuktQVfY0ypfWnPKH84iOBnyl1010VCPMKTMqPMsN51Jx9-cT8N_oGwqg5087T3Sc0Yx273EwYY8Z-PDJmtxJmT31BEbUC28xPEy1-NvcaxBjlCmxvDJCesnh5Y1d9cQdGtvmuBp6ur3NpXCUpfYauXskO-f377GIgKwTFoNpD"
# public_key = open("Jwt.pub","r").read()
# key = serialization.load_ssh_public_key(public_key)
# decode_token = jwt.api_jwt.decode(jwt=token,key=key,algorithms=["RS256",])
# print(decode_token)




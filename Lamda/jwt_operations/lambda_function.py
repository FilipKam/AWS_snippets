import json
import jwt

def lambda_handler(event, context):
    access_token_jwt_encoded = event['headers']['x-amzn-oidc-accesstoken'] # get jwt from header
    access_token_jwt_decoded = jwt.decode(access_token_jwt_encoded, options={"verify_signature": False}) # decode jwt
    
    identity_token_jwt_encoded = event['headers']['x-amzn-oidc-data'] # get jwt from header
    identity_token_jwt_decoded = jwt.decode(identity_token_jwt_encoded, options={"verify_signature": False}) # decode jwt
    
    # create a json object
    output_json =  {"Original-Event":"","Access-token-encoded-JWT":"", "Access-token-decoded-JWT":"", "Identity-token-encoded-JWT":"", "Identity-token-decoded-JWT":""}

    output_json['Original-Event'] = event # add original event to json object
    output_json['Access-token-encoded-JWT'] = access_token_jwt_encoded # add encoded jwt to json object
    output_json['Access-token-decoded-JWT'] = access_token_jwt_decoded # add decoded jwt to json object
    
    output_json['Identity-token-encoded-JWT'] = identity_token_jwt_encoded # add encoded jwt to json object
    output_json['Identity-token-decoded-JWT'] = identity_token_jwt_decoded # add decoded jwt to json object
    

    
    return {
        'headers':{
            "Content-Type":"application/json"
        },
        'statusCode': 200,
        'body': json.dumps(output_json)
    }

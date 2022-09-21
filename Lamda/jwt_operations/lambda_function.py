import json
import jwt

def lambda_handler(event, context):
    jwt_encoded = event['headers']['x-amzn-oidc-accesstoken'] # get jwt from header
    jwt_decoded = jwt.decode(jwt_encoded, options={"verify_signature": False}) # decode jwt
    
    output_json =  {"Original-Event":"","Encoded-JWT":"", "Decoded-JWT":""} # create a json object

    output_json['Original-Event'] = event # add original event to json object
    output_json['Encoded-JWT'] = jwt_encoded # add encoded jwt to json object
    output_json['Decoded-JWT'] = jwt_decoded # add decoded jwt to json object

    return {
        'headers':{
            "Content-Type":"application/json"
        },
        'statusCode': 200,
        'body': json.dumps(output_json)
    }
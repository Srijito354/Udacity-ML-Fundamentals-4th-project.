import boto3
import json
import sagemaker
import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model

ENDPOINT = "image-classification-2023-10-20-05-37-03-467"## TODO: fill in

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])

    # Instantiate a Predictor
    predictor = sagemaker.predictor.Predictor(ENDPOINT) ## TODO: fill in

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    #Image_data_serializer
    #predictor.serializer = Image_data_serializer("image/png")
    # Make a prediction:
    inferences = predictor.predict(image) ## TODO: fill in
    
    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
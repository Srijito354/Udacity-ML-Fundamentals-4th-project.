import json

def lambda_handler(event, context):
    
    THRESHOLD = 0.93
    
    # Grab the inferences from the event
    inferences = event.get('body')["inferences"]## TODO: fill in
    
    # Check if any values in our inferences are above THRESHOLD
    #meets_threshold = [str(x > THRESHOLD for x in inferences)]## TODO: fill in
    
    for i in inferences:
        if i> THRESHOLD:
            meets_threshold = True
            break
        else:
            meets_threshold = False
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
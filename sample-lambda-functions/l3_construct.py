def lambda_handler(event, context):
    message = 'API Call Successful : L3 Construct'
    return {
        'statusCode': 200,
        'headers': {
            "Content-Type": "application/json"
        },         
        'body' : message
    }

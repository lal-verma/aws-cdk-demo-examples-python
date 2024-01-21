import json
import boto3
import os

def handler(event, context):

    todo_db_name = os.environ['TODO_DB_TABLE_NAME']
    dynamodb = boto3.resource('dynamodb')

    if (event['httpMethod'] == 'GET'): 
            table = dynamodb.Table(todo_db_name)
            response = table.scan()
            message = json.dumps(response['Items'])
    elif (event['httpMethod'] == 'POST'): 
            table = dynamodb.Table(todo_db_name)
            response = table.put_item(
                Item={
                    'id': event['body']['id'],
                    'title': event['body']['title'],
                    'description': event['body']['description'],
                    'status': event['body']['status']
                }
            )
            message = json.dumps(response)
    elif (event['httpMethod'] == 'DELETE'):    
            table = dynamodb.Table(todo_db_name)
            response = table.delete_item(
                Key={
                    'id': event['body']['id']
                }
            )
            message = json.dumps(response)
    elif ():
            response = "Method not allowed"


    return {
        'statusCode': 200,
        'headers': {
            "Content-Type": "application/json"
        },         
        'body' : message
    }

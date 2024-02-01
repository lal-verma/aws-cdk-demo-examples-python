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
            input_todo_item = event['body'] 
            if isinstance(event['body'], str):
                input_todo_item = json.loads(event['body'])
            table = dynamodb.Table(todo_db_name)
            response = table.put_item(
                Item={
                    'id': input_todo_item['id'],
                    'title': input_todo_item['title'],
                    'description': input_todo_item['description'],
                    'status': input_todo_item['status']
                }
            )
            message = json.dumps(response)
    elif (event['httpMethod'] == 'DELETE'):    
            table = dynamodb.Table(todo_db_name)
            input_todo_item = event['body'] 
            if isinstance(event['body'], str):
                input_todo_item = json.loads(event['body'])
            response = table.delete_item(
                Key={
                    'id':input_todo_item['id']
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
import json
import boto3
import os
import ulid

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'Inventory')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        
        item_id = str(ulid.new())
        item = {
            'id': item_id,
            'name': body['name'],
            'description': body['description'],
            'qty': int(body['qty']),
            'price': float(body['price']),
            'location_id': int(body['location_id'])
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 201,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'message': 'Item added', 'id': item_id})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

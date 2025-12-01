import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'Inventory')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        
        table.delete_item(Key={'id': item_id})
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'message': 'Item deleted'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})

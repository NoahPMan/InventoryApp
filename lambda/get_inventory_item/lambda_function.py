import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'InventoryApp')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Extract ID from path parameters
        item_id = event['pathParameters']['id']
        
        # Get item from DynamoDB
        response = table.get_item(Key={'id': item_id})
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Item not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

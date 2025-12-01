import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'InventoryApp')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        location_id = int(event['pathParameters']['id'])
        
        response = table.query(
            IndexName='LocationIndex',  # Replace with your GSI name
            KeyConditionExpression='location_id = :loc',
            ExpressionAttributeValues={':loc': location_id}
        )
        
        items = response.get('Items', [])
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(items)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

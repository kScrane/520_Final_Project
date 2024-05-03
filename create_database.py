import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.client('dynamodb')

db = boto3.resource('dynamodb', aws_access_key_id="xxx",
                        aws_secret_access_key="xxx",
                        region_name="us-east-1",
                        endpoint_url="http://localhost:8000")

def delete_user_database():
    table = db.Table('Users')
    table.delete()

def create_user_database(dyn_resource=None):
    table = db.create_table(
        TableName = 'Users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions = [
            {
                "AttributeName": "username", 
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits':10,
            'WriteCapacityUnits' :10
        }
    )
    return 

def return_user_database():
    return db.Table("Users")


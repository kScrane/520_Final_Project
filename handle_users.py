
import hashlib
from create_database import *
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.client('dynamodb')

db = boto3.resource('dynamodb', aws_access_key_id="xxx",
                        aws_secret_access_key="xxx",
                        region_name="us-east-1",
                        endpoint_url="http://localhost:8000")

"""User authentication and authorization.
There are two types of users: 
- one uses the system   
- one manages the system (referred to as administrators). 
Both need to log in to use the system. Users need to register before using the system or be added to
the system by administrators. The default administrator has the username is as and password as
admin. After the first login, the system should prompt admin to change the password. The
default administrator has the privilege to add new administrators and users. Administrators can
retrieve all users’ evaluations and compute the average score for each perspective across the
entire user base or selected users"""

def return_user_database():
    return db.Table("Users")

def create_user(username, password, organization="none", is_admin=0):
    table = return_user_database()
    #TODO: Check if username exists
    #TODO: check if organization exists
    if get_user(username) != 0:
        print("User already exists")
        return 0
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()   
    response = table.put_item(Item= {'username': username, 'password': hashed_password, 'organization': organization, 'is_admin': is_admin})
    if get_user(username) == 0:
        print("Error creating user")
        return 0
    return 1

def create_new_org(organization):
    #TODO: Figure how to save organizations
    return 0

def delete_user(username):
    table = return_user_database()
    response = table.get_item(Key={'username': username})
    if 'Item' not in response:
        print("User not present")
        return 0
    else:
        print("User deleted")
        response = table.delete_item(Key={'username': username})
        return 1

def get_user(username):
    table = return_user_database()
    response = table.get_item(Key={'username': username})
    if 'Item' in response:
        r = (response['Item']['username'], response['Item']['organization'], response['Item']['is_admin'])
        print(r)
        return r
    else:
        return 0

def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()   
    table = return_user_database()
    response = table.query(
        KeyConditionExpression=Key('username').eq(username),
        FilterExpression=Attr('password').eq(hashed_password)
    )
    if response['Count'] == 1:
        print("Successful login")
        organization = response['Items'][0]['organization']
        is_admin = response['Items'][0]['is_admin']
        r = (organization, is_admin)
        return r
    else:
        print("User doesn't exist")
        return 0

def print_values():
    table = return_user_database()
    users = table.scan()
    data = users['Items']
    for u in data:
        print(u)

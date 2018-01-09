from flask import Blueprint, json
from Util.default_serializers import default
import boto3

productservice = Blueprint('productservice', __name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Products')


@productservice.route('/getAllProducts', methods=['GET'])
def get_all_products():
    response = table.scan()
    return json.dumps(response['Items'], default=default)


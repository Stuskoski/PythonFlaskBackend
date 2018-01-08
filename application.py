#!flask/bin/python
from flask import Flask, jsonify, json
from flaskrun import flaskrun
from flask_cors import CORS
from decimal import Decimal
import boto3



application = Flask(__name__)
CORS(application)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Products')


@application.route('/', methods=['GET'])
def get():
    return '{"Output":"Hello World"}'


@application.route('/', methods=['POST'])
def post():
    return '{"Output":"Hello World"}'


@application.route('/getAllProducts', methods=['GET'])
def get_all_products():
    response = table.scan()
    return json.dumps(response['Items'], default=default)


def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)


if __name__ == '__main__':
    flaskrun(application)

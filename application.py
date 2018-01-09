#!flask/bin/python
from flask import Flask
from flaskrun import flaskrun
from flask_cors import CORS
import boto3

from Services.product_service import productservice

application = Flask(__name__)
CORS(application)
application.register_blueprint(productservice)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Products')


@application.route('/', methods=['GET'])
def get():
    return '{"Output":"Hello World"}'


@application.route('/', methods=['POST'])
def post():
    return '{"Output":"Hello World"}'


if __name__ == '__main__':
    flaskrun(application)

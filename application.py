#!flask/bin/python
from flask import Flask, jsonify
from flaskrun import flaskrun
from flask_cors import CORS
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
    return jsonify(response['Items'])


if __name__ == '__main__':
    flaskrun(application)

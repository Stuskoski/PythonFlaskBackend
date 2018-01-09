from flask import Blueprint, json, request
from Util.default_serializers import DecimalEncoder
import boto3
from boto3.dynamodb.conditions import Key, Attr

productservice = Blueprint('productservice', __name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Products')


@productservice.route('/getAllProducts', methods=['GET'])
def get_all_products():
    response = table.scan()
    return json.dumps(response['Items'], cls=DecimalEncoder)


@productservice.route('/getProductInformation', methods=['POST'])
def get_product_info_with_id():

    product_id = request.get_json()['productID']
    response = table.query(
        ProjectionExpression="#Desc, HAS_OFFERS, ID, IMAGE_URL",
        ExpressionAttributeNames={"#Desc": "DETAIL"},
        KeyConditionExpression=Key('ID').eq(product_id)
    )

    return json.dumps(response['Items'], cls=DecimalEncoder)


@productservice.route('/getProductsWithOffers', methods=['GET'])
def get_products_with_offers():
    response = table.scan()

    has_offer_items = list(filter(lambda items: items['HAS_OFFERS'], response['Items']))

    return json.dumps(has_offer_items, cls=DecimalEncoder)


@productservice.route('/getProductsWithoutOffers', methods=['GET'])
def get_products_without_offers():
    response = table.scan()

    has_offer_items = list(filter(lambda items: not items['HAS_OFFERS'], response['Items']))

    return json.dumps(has_offer_items, cls=DecimalEncoder)


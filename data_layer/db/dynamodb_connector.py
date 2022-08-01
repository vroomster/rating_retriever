from .connector import Connector
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


class DynamoDbConnector(Connector):

    def __init__(self):
        self.dynamodb_client = boto3.resource(
            "dynamodb",
            aws_access_key_id="AKIAJOHFQYFXUTG5NLJA",
            aws_secret_access_key="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",
            region_name="us-east-1"
        )#, endpoint_url="http://localhost:8000")
        #self.clients_table = self.dynamodb_client.Table('clients')

    def get_item(self, table_name, key_name, key_value):
        table = self.dynamodb_client.Table(table_name)
        try:
            response = table.get_item(
                Key={
                    key_name: key_value,
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            item = response['Item']
            #print("GetItem succeeded:")
            #print(json.dumps(item, indent=4, cls=DecimalEncoder))
            return json.dumps(item, indent=4, cls=DecimalEncoder)

    def scan_items(self, table_name):
        items = []
        table = self.dynamodb_client.Table(table_name)

        response = table.scan()
        for i in response['Items']:
            items.append(json.dumps(i, cls=DecimalEncoder))

        while 'LastEvaluatedKey' in response:
            response = table.scan(
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
            for i in response['Items']:
                items.append(json.dumps(i, cls=DecimalEncoder))

        return items


# Helper class to convert a DynamoDB item to JSON.

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

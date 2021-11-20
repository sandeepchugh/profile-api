import logging

import boto3 as boto3
from boto3.dynamodb.conditions import Key

from app.config import Config
from app.request import ProfileRequest
from app.response import Profile

logger = logging.getLogger(__name__)





class ProfileHandler:

    def __init__(self):
        self._config = Config()
        self._profile_table = self._get_dynamodb_table()
        logger.setLevel(self._config.log_level)

    def get_profile(self, profile_request: ProfileRequest) -> Profile:
        return self._get_dybnamodb_profile(profile_request.customer_id)

    def _get_dybnamodb_profile(self,customer_id):
        response = self._profile_table.query(
            KeyConditionExpression=Key('customer_id').eq(customer_id))
        data = response.get("Items", {})
        profile = Profile(customer_id=customer_id,
                          first_name= data.get('first_name'),
                          last_name = data.get('last_name'))
        return profile

    def _get_dynamodb_table(self):
        if self._config.profile_table_endpoint is None:
            return boto3.resource('dynamodb', self._config.region)\
                .Table(self._config.profile_table_name)
        else:
            return boto3.resource('dynamodb', self._config.region,
                                  endpoint_url= self._config.profile_table_endpoint) \
                .Table(self._config.profile_table_name)
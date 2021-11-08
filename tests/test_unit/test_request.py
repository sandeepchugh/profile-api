import json
import pathlib

import pytest

from app.request import Request


@pytest.fixture(params=[("api_gateway_proxy_event.json")])
def load_api_gateway_request(request):
    request_json = json.dumps( json.loads(
        (
            pathlib.Path(__file__).parent.parent.absolute()
            / "fixtures"
            / request.param
        ).read_bytes()))
    return request_json


def test_can_create_request_model(load_api_gateway_request):
    request_json = load_api_gateway_request
    request_json = request_json.replace("queryStringParameters", "query_parameters")\
        .replace("pathParameters", "path_parameters")\
        .replace("customer-id", "customer_id")\
        .replace("httpMethod", "http_method")

    request_dict = json.loads(request_json)

    request = Request(**request_dict)
    assert request is not None
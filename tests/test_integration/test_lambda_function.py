from app.lambda_function import lambda_handler


def test_lambda_handler_returns_response():
    profile = lambda_handler(None,None)
    assert profile is not None
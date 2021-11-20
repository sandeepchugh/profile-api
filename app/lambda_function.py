import json
import logging
from functools import lru_cache

from app import request
from app.config import Config
from app.profile_handler import ProfileHandler

logger = logging.getLogger(__name__)


@lru_cache(maxsize=None)
def create_profile_handler():
    return ProfileHandler()


def format_response(profile):
    return {"statusCode": 200, "body": json.dumps(profile.json())}


def lambda_handler(event, context):
    config = Config()
    logger.setLevel(config.log_level)
    logger.info(event)

    profile_handler = create_profile_handler()
    profile_request = request.create(event)
    logger.debug(profile_request)
    profile = profile_handler.get_profile(profile_request)
    logger.info(profile)

    return format_response(profile)

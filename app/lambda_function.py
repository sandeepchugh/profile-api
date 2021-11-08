import json

from app.encoder import UUIDEncoder
from app.response import Profile


def lambda_handler(event, context):
    profile = Profile(first_name = "Sam",
                      last_name = "Raimy",
                      customer_id = "CB23A3E7-6055-43CC-9B43-03D9B529E3FB")
    print(f"{profile.first_name} {profile.last_name}")
    return profile.dict()

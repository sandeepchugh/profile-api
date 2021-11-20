import os


class Config:

    def __init__(self):
        self._log_level = os.getenv('LogLevel', 'INFO')
        self._region = os.getenv('Region', 'us-east-1')
        self._profile_table_name = os.getenv('ProfileTableName', 'profile')
        self._profile_table_endpoint = os.getenv('ProfileTableEndpoint', None)

    @property
    def log_level(self):
        return self._log_level

    @property
    def region(self):
        return self._region

    @property
    def profile_table_name(self):
        return self._profile_table_name

    @property
    def profile_table_endpoint(self):
        return self._profile_table_endpoint

import os


class Config:
    TEST_DB_CONNECTION = "psql..//"
    DEFAULT = "..."


class ConfigTest(Config):
    TEST_DB_CONNECTION = "TEST psql..//"


class ConfigDev(Config):
    TEST_DB_CONNECTION = "DEV psql..//"


def run_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return ConfigDev
    elif env == "TEST":
        return ConfigTest
    else:
        return Config

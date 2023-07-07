import os


class Config:
    DEBUG = os.environ['DEBUG']
    TESTING = os.environ['TESTING']

import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f2gh3n3s9dfs5nj4fsu32js2hf3sj1'

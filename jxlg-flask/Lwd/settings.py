import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_database_uri(DATABASE):
    db = DATABASE.get('DATABASE') or 'mysql'
    driver = DATABASE.get('DRIVER') or 'pymysql'
    user = DATABASE.get('USER') or 'lwd'
    password = DATABASE.get('PASSWORD') or '123456'
    host = DATABASE.get('HOST') or '127.0.0.1'
    port = DATABASE.get('PORT') or '3306'
    databasename = DATABASE.get('DATABASENAME') or 'FlaskDays03'

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver, user, password, host, port, databasename)

# 配置基类
class BaseConfig():
    DEBUG = False
    TESTING = False
    # 秘钥 session
    SECRET_KEY = '%^&*(456789fghj123asdq123123'
    # flask-session 持久化
    SESSION_TYPE = 'redis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 开发环境(默认环境)
class DevelopConfig(BaseConfig):
    DEBUG = True
    # 数据库
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'develop.db')

# 测试环境
class TestingConfig(BaseConfig):
    TESTING = True
    # 数据库
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'testing.db')

# 演示环境
class StagingConfig(BaseConfig):
    # 数据库
    SQLALCHEMY_DATABASE_URI ='sqlite:////' + os.path.join(BASE_DIR, 'stating.db')

# 线上环境(生成环境)
class ProductConfig(BaseConfig):
    # 数据库配置
    DATABASE = {
        'DATABASE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'lwd',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'DATABASENAME': 'FlaskDays03'
    }

    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)


config = {
    'develop': DevelopConfig,    # 开发环境
    'testing': TestingConfig,    # 测试环境
    'staging': StagingConfig,    # 演示环境
    'product': ProductConfig,    # 线上环境
    'default': DevelopConfig,    # 默认开发环境
}
from flask import Flask

from Lwd.ext import init_ext
from Lwd.settings import config
from Lwd.views import init_blue


def createapp(env_name=None):
    # 创建应用
    app = Flask(__name__)

    # 联通    settings.py
    app.config.from_object(config.get(env_name or 'default'))


    # 蓝图注册
    init_blue(app)

    # 扩展初始化
    init_ext(app)


    return app


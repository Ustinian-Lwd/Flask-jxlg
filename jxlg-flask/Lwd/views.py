from flask import Blueprint, render_template

# 创建蓝图对象
blue = Blueprint('lwd', __name__)


# 初始化蓝图
def init_blue(app):
    app.register_blueprint(blueprint=blue)


# 测试联通
@blue.route('/hello/')
def hello():
    return 'Hello World!'


# 首页
@blue.route('/index/')
def index():
    return render_template('index.html')


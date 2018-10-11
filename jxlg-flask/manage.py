from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager
from Lwd import createapp


# 创建了应用
app = createapp()
# 实现命令行参数接受
manager = Manager(app)
# 实现migrate迁移绑定
manager.add_command('db', MigrateCommand)





if __name__ == '__main__':
    manager.run()

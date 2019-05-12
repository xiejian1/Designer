from flask import Flask
from flask_script import Manager

from flask_migrate import Migrate,MigrateCommand
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://xq:123456@127.0.0.1:3306/flaskdemo?charset=utf8"
# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

manager = Manager(app)
# 要使用flask-migrate，必须先绑定db和app
migrate = Migrate(app, db)
# 将MigrateCommand添加到manager中，"db"是自定义命令
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
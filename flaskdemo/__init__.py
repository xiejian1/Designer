# -*- coding: utf-8 -*-

# # #创建项目对象
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#工程函数
from flaskdemo.utils.config import UPLOAD_FOLDER
from flaskdemo.utils.filters import lovecount, commentcount, foodpic, picturepic


def create_app():
    from flaskdemo.utils.config import RegexConverter
    from flaskdemo.utils.filters import cut_desc, cut_descs, toStr
    app = Flask(__name__, static_url_path='')
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://xq:123456@127.0.0.1:3306/designer?charset=utf8"
    # 动态追踪修改设置，如未设置只会提示警告
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_POOL_SIZE'] = 100
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20


    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.url_map.converters['regex'] = RegexConverter

    app.add_template_filter(cut_desc, 'cut_desc')
    app.add_template_filter(cut_descs, 'cut_descs')
    app.add_template_filter(toStr, 'string')
    app.add_template_filter(lovecount, 'lovecount')
    app.add_template_filter(commentcount, 'commentcount')
    app.add_template_filter(foodpic,'foodpic')
    app.add_template_filter(picturepic,'picturepic')
    db = SQLAlchemy(app)
    return app

# #
# # #加载配置文件内容
# app.config.from_object('setting')     #模块下的setting文件名，不用加py后缀
# # app.config.from_envvar('FLASKR_SETTINGS')   #环境变量，指向配置文件setting的路径
# #
# # #创建数据库对象
# db = SQLAlchemy(app)
# #
# # #生成数据方法
# # #from blog2 import db
# # #db.create_all()


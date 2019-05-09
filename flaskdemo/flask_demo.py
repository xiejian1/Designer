from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskdemo.controller.demo import ShowUsers, JsonTest, JsonData, UserView
from flaskdemo.controller.entity import createtable, add, delete, update
from flaskdemo.controller.food import Foodlist, Fooddetail
from flaskdemo.controller.pictrue import Pictruelist, Picturedetail

app = Flask(__name__,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://xq:123456@127.0.0.1:3306/flaskdemo?charset=utf8"
# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.add_url_rule(rule='/', view_func=ShowUsers.as_view('show_users'))
    app.add_url_rule(rule='/foodlist/',view_func=Foodlist.as_view('foodlist'))
    app.add_url_rule(rule='/fooddetail/',view_func=Fooddetail.as_view('fooddetail'))
    app.add_url_rule(rule='/picturelist/',view_func=Pictruelist.as_view('pictruelist'))
    app.add_url_rule(rule='/picturedetail/',view_func=Picturedetail.as_view('picturedetail'))
    app.add_url_rule(rule='/jsontest/', view_func=JsonTest.as_view('json_test'))
    app.add_url_rule(rule='/json/', view_func=JsonData.as_view('json_demo'))
    app.add_url_rule(rule='/list/', view_func=UserView.as_view('list_users'))
    app.add_url_rule(rule='/db/', view_func=createtable.as_view('createtable'))
    app.add_url_rule(rule='/add/',view_func=add.as_view('add'))
    app.add_url_rule(rule='/delete/',view_func=delete.as_view('delate'))
    app.add_url_rule(rule='/update/',view_func=update.as_view('update'))
    app.run(debug=True, host='localhost', port=8000)

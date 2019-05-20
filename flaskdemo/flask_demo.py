
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskdemo.controller.admin import  PictureEdit, Foodedit
from flaskdemo.controller.contentedit import ContentEdit, ImageUpload, EditeUpload
from flaskdemo.controller.demo import ShowUsers, JsonTest, JsonData, UserView
from flaskdemo.controller.entity import createtable, add, delete, update
from flaskdemo.controller.food import Foodlist, Fooddetail
from flaskdemo.controller.pictrue import Pictruelist, Picturedetail
from flaskdemo.controller.test import Upload,Yulan, Multiple, EditerUplaod
from flaskdemo.utils.config import UPLOAD_FOLDER, RegexConverter
from flaskdemo.utils.filters import cut_desc, cut_descs, toStr

BASE_DIR = os.path.abspath(os.path.dirname(__name__))
app = Flask(__name__,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://xq:123456@127.0.0.1:3306/flaskdemo?charset=utf8"
# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.url_map.converters['regex'] = RegexConverter

app.add_template_filter(cut_desc,'cut_desc')
app.add_template_filter(cut_descs,'cut_descs')
app.add_template_filter(toStr,'string')
db = SQLAlchemy(app)



def main():
    app.add_url_rule(rule='/upload/', view_func=Upload.as_view('upload'))
    app.add_url_rule(rule='/yulan/', view_func=Yulan.as_view('yulan'))
    app.add_url_rule(rule='/editerUplaod/', view_func=EditerUplaod.as_view('editer'))
    app.add_url_rule(rule='/multiple/', view_func=Multiple.as_view('multiple'))

    app.add_url_rule(rule='/', view_func=ShowUsers.as_view('index'))
    app.add_url_rule(rule='/food/home/', view_func=Foodlist.as_view('foodlist'))
    app.add_url_rule(rule='/fooddetail/<string:id>', view_func=Fooddetail.as_view('fooddetail'))

    app.add_url_rule(rule='/picture/cutout/', view_func=Pictruelist.as_view('pictruelist'))
    app.add_url_rule(rule='/picturedetail/<string:id>', view_func=Picturedetail.as_view('picturedetail'))

    app.add_url_rule(rule='/admin/', view_func=Foodedit.as_view('admin'))
    app.add_url_rule(rule='/pictureedit/', view_func=PictureEdit.as_view('pictureedit'))
    app.add_url_rule(rule='/contentedit/<string:type>/<string:id>', view_func=ContentEdit.as_view('contentedit'))
    app.add_url_rule(rule='/editeupload/', view_func=EditeUpload.as_view('editupload'))
    app.add_url_rule(rule='/imageupload/', view_func=ImageUpload.as_view('imageupload'))

    app.add_url_rule(rule='/jsontest/', view_func=JsonTest.as_view('json_test'))
    app.add_url_rule(rule='/json/', view_func=JsonData.as_view('json_demo'))
    app.add_url_rule(rule='/list/', view_func=UserView.as_view('list_users'))
    app.add_url_rule(rule='/db/', view_func=createtable.as_view('createtable'))
    app.add_url_rule(rule='/add/', view_func=add.as_view('add'))
    app.add_url_rule(rule='/delete/', view_func=delete.as_view('delate'))
    app.add_url_rule(rule='/update/', view_func=update.as_view('update'))
    app.run(debug=True, host='localhost', port=8000)


if __name__ == "__main__":
   main()
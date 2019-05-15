import os
import uuid

from flask import render_template, request, url_for
from flask.views import MethodView, View
from werkzeug.utils import secure_filename, redirect

from flaskdemo.model.models import Food, FoodPic, Picture, PicturePic
from flaskdemo.utils.config import UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class Foodedit(MethodView):

    def get(self):
        print('get请求')
        return render_template('microblog/foodedit.html')

    def post(self):
        print('foodedit post 请求')
        food_type = request.form.get('food_type')
        food_title = request.form.get('food_title')
        food_desc = request.form.get('food_desc')
        food_abstract = request.form.get('food_abstract')
        id = str(uuid.uuid3(uuid.NAMESPACE_URL,food_title))
        id = id.replace("-",'')
        food_pics = []

        files = request.files.getlist("files")
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print('打印文件的名字', filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                picurl = '/img/upload/'+filename
                food_pics.append(picurl)
                print('打印图片路径',food_pics)
        food = Food()
        food.id = id
        food.food_type = food_type
        food.food_title = food_title
        food.food_abstract = food_abstract
        food.food_desc = food_desc
        food.save()

        for pic in food_pics:
            foodpic = FoodPic()
            foodpic.pic_url = pic
            foodpic.food_id = id
            foodpic.save()

        print('打印id值',id)
        print('打印美食类型',food_type)
        print('打印美食标题', food_title)
        print('打印美食的描述', food_abstract)
        print('打印美食描述', food_desc)
        print('打印美食图片路径', food_pics)


        return redirect(url_for('contentedit',id=id,type=food_type))

class PictureEdit(MethodView):
    """图片编辑"""

    def get(self):
        return render_template('microblog/pictureedit.html')

    def post(self):
        print('foodedit post 请求')
        pic_type = request.form.get('pic_type')
        pic_title = request.form.get('pic_title')
        pic_abstract = request.form.get('pic_abstract')
        pic_desc = request.form.get('pic_desc')
        id = str(uuid.uuid3(uuid.NAMESPACE_URL, pic_title))
        id = id.replace("-",'')
        picture_pics = []
        files = request.files.getlist("files")
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print('打印文件的名字', filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                picurl = '/img/upload/' + filename
                picture_pics.append(picurl)
                print('打印图片路径', picture_pics)
        picture = Picture()
        picture.id = id
        picture.pic_type = pic_type
        picture.pic_title = pic_title
        picture.pic_abstract = pic_abstract
        picture.pic_desc = pic_desc
        picture.save()

        for pic in picture_pics:
            picturepic = PicturePic()
            picturepic.pic_url = pic
            picturepic.picture_id = id
            picturepic.save()

        print('打印id值', id)
        print('打印美食类型', pic_type)
        print('打印美食标题', pic_title)
        print('打印美食描述', pic_desc)
        print('打印美食图片路径', picture_pics)

        return redirect(url_for('contentedit',id=id,type=pic_type))

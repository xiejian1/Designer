import json
import os

from flask import render_template, request, Response, url_for
from flask.views import MethodView, View
from werkzeug.utils import secure_filename, redirect

from flaskdemo.model.models import FoodContent, Picture, PictureContent
from flaskdemo.utils.config import UPLOAD_FOLDER
from flaskdemo.utils.label import foodtype, pictype

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

class ContentEdit(View):

    def dispatch_request(self,type,id):
        print('文本编辑')
        print('打印id值',id)
        return render_template('microblog/contentedit.html',id=id,type=type)


class EditeUpload(MethodView):

    def post(self):
        print('富文本post请求')
        data = request.get_data()
        data = json.loads(data)
        content = data.get('content')
        id = data.get('id')
        content_type = data.get('content_type')
        if content_type in foodtype:
            foodContent = FoodContent()
            foodContent.food_id = id
            foodContent.content = content
            print('打印数据', content)
            print('打印id值', id)
            foodContent.save()
            return Response(json.dumps({'msg':'ok'}),content_type='application/json')
        elif content_type in pictype:
            picContent = PictureContent()
            picContent.picture_id = id
            picContent.content = content
            print('打印数据', content)
            print('打印id值', id)
            picContent.save()
            return Response(json.dumps({'msg': 'ok'}), content_type='application/json')

class ImageUpload(MethodView):

    def post(self):
        print('图片上传')
        file = request.files['file']
        print('打印文件的名字',file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            urlpath = '/img/upload/'+filename
            print('打印返回的路径',urlpath)
        return Response(json.dumps({"error":0,"data":[urlpath]}))
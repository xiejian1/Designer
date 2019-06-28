import os
from flask import request, Response, render_template,url_for
from flask.views import View, MethodView
import json

from werkzeug.utils import secure_filename, redirect

from flaskdemo.utils.config import UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# class Upload(MethodView):
#
#     def get(self):
#          print('DET请求')
#          return render_template('microblog/test.html')
#
#     def post(self):
#          print('进入请求')
#          foodname = request.form.get('foodname')
#          print('打印食物名字', foodname)
#          description = request.form.get('description')
#          print('打印说明', description)
#          file = request.files['file']
#          filename = file.filename
#          print('打印文件的名字', filename)
#          return Response(json.dumps({'msg': 'ok'}))
class Editor(MethodView):
    def get(self):
        """富文本编辑测试"""
        print('富文本进行测试')
        return render_template('microblog/editor.html')
    def post(self):
        print('图片上传')
        file = request.files['files']
        filetype = request.args.get('dir')
        print("打印类型",filetype)
        print('打印文件的名字', file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            urlpath = '/img/upload/' + filename
            print('打印返回的路径', urlpath)
            print('打印类型',type(urlpath))
            respose_upload = {
                "error": 0,
                "url": urlpath
            }
        return Response(json.dumps(respose_upload))

class EditerUplaod(MethodView):

    def post(self):
        print('post请求')
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                return redirect(url_for('editerUplaod',
                                        filename=filename))
    def get(self):
        print('GET请求')
        return render_template('microblog/contentedit.html')

class Upload(MethodView):

    def post(self):
        """获取富文本的数据"""
        print('post请求')
        data = request.values.get('content')
        print('打印数据',data)
        return Response(json.dumps({'msg':'ok'}))

class EditeUpload(MethodView):
    def post(self):
        print('post请求')
        data = request.get_data()
        data = json.loads(data)
        content = data.get('content')
        print('打印数据',content)
        return Response(json.dumps({'msg':'ok'}))

class ImageUpload(MethodView):

    def post(self):
        print('图片上传')
        file = request.files['files']
        print('打印文件的名字',file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            urlpath = '/img/upload/'+filename
            print('打印返回的路径',urlpath)
        return Response(json.dumps({"error":0,"data":[urlpath]}))

class Yulan(MethodView):
    """图片上传前预览"""
    def get(self):
        print('图片上传前预览')
        return render_template('microblog/uploadtest.html')

    def post(self):
        print('post 接收数据')
        title = request.form.get('title')
        print('打印标题',title)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('打印图片的名字',filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            return Response(json.dumps({'msg':'ok'}))

class Multiple(MethodView):

    def get(self):
        print('多文件上传')
        return render_template('microblog/multiupload.html')
    def post(self):
        print('保存多张图图片')
        uploaded_files = request.files.getlist("files")
        filenames = []
        for file in uploaded_files:
            # Check if the file is one of the allowed types/extensions
            if file and allowed_file(file.filename):
                # Make the filename safe, remove unsupported chars
                filename = secure_filename(file.filename)
                # Move the file form the temporal folder to the upload
                # folder we setup
                print('打印文件的名字',filename)
                #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # Save the filename into a list, we'll use it later
                filenames.append(filename)
                # Redirect the user to the uploaded_file route, which
                # will basicaly show on the browser the uploaded file
        # Load an html page with a link to each uploaded file
        return Response(json.dumps({'msg':'ok'}))
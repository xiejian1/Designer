import json

from flask import render_template, request, jsonify, Response
from flask.views import View

class ShowUsers(View):

    def dispatch_request(self):
        print("程序执行到此处！")
        return render_template("microblog/index.html")

class ListView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def get_objects(self):
        raise NotImplementedError

    def dispatch_request(self):
        print("打印请求的地址")
        print(request.method)
        print("提取用户上传的数据",request.args['name'])
        context = {'posts': self.get_objects()}
        return self.render_template(context)

class UserView(ListView):

    def get_template_name(self):
        return 'microblog/index.html'

    def get_objects(self):
        return [
            {
                'author': {'nickname': 'John'},
                'body': 'Beautiful day in Portland!'
            },
        ]
class JsonTest(View):
    def dispatch_request(self):
        return jsonify({'a': 1, 'b': 5})
class JsonData(View):
    def dispatch_request(self):
       return render_template('microblog/test.html')

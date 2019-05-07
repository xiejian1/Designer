from flask import Response
from flask.views import View
from kombu import uuid
from flaskdemo.model.models import User
import json
from flaskdemo.model.models import db
class createtable(View):

    def dispatch_request(self):
        """创建所有的表"""
        print("创建所有的表")
        user = User.query.filter_by(name='xieqiang').first()
        print('打印获取的数据')
        print(user.name)
        print(user.id)
        users = User.query.all()
        for u in users:
            print('打印获取的id值: ',u.id)
        return Response(json.dumps({'msg':user.id}),content_type='application/json')

class add(View):

    def dispatch_request(self):
        print('向数据库添加数据')
        user = User()
        user.id = uuid().replace('-','')
        user.name = '小建'
        user.email = 'xqiang7553@163.com'
        user.password = user.set_password(password='xq123456')
        db.session.add(user)
        db.session.commit()

        return Response(json.dumps({'msg':'success'}),content_type='application/json')
class delete(View):
    """删除数据库"""
    def dispatch_request(self):
        print('对数据进行删除操作')
        user = User.query.filter(User.id=='d1bbf91ccbb04423849cb53d8a0e017d').first()
        db.session.delete(user)
        db.session.commit()
        return Response(json.dumps({'msg':'ok'}))
class update(View):
    """对数据进行修改"""
    def dispatch_request(self):
        print('对数据进行修改')
        user = User.query.filter(User.id =='edd47b6a04dc47848bd15ff8fcf67a64').first()
        user.name = 'xieqiang'
        user.password = user.set_password(password='xq123456')
        db.session.add(user)
        db.session.commit()

        return Response(json.dumps({'msg':'ok'}))




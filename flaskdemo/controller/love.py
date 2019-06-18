import datetime
import json

from flask import request, Response
from flask.views import MethodView

from flaskdemo.model.models import PictureLove


class AddLove(MethodView):
    """添加关注"""
    def post(self):
        print('接收前端传递的数据')
        data = request.get_data()
        data = json.loads(data)
        print('打印json数据',data)
        id = data.get('id')
        ip = data.get('ip')
        area = data.get('place')
        date = datetime.date.today()
        print('打印获取的ip地址',area)
        pictureLove = PictureLove()

        pictureLove.picture_id = id
        pictureLove.remote_addr =ip
        pictureLove.remote_area = area
        pictureLove.picture_time = date

        pictureLove.save()

        count = PictureLove.query.count()
        return Response(json.dumps({"msg":'ok',"count":count,"loveid":pictureLove.id}),content_type='application/json')

class DelLove(MethodView):
    """删除关注"""
    def get(self,loveid):
        pictureLove = PictureLove.query.get(loveid)
        pictureLove.delete()
        count  = PictureLove.query.count()
        return Response(json.dumps({"mag":'ok',"count":count}),content_type='application/json')
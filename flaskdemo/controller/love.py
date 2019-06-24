import datetime
import json

from flask import request, Response
from flask.views import MethodView

from flaskdemo.model.models import PictureLove, FoodLove


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

        count = PictureLove.query.filter_by(picture_id=id).count()
        return Response(json.dumps({"msg":'ok',"count":count,"loveid":pictureLove.id}),content_type='application/json')

class DelLove(MethodView):
    """删除关注"""
    def get(self,loveid):
        pictureLove = PictureLove.query.get(loveid)
        pictureLove.delete()
        count  = PictureLove.query.filter_by(picture_id=loveid).count()
        return Response(json.dumps({"mag":'ok',"count":count}),content_type='application/json')

#美食添加关注
class FoodAddLove(MethodView):
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
        foodLove = FoodLove()

        foodLove.food_id = id
        foodLove.remote_addr =ip
        foodLove.remote_area = area
        foodLove.love_time = date

        foodLove.save()

        count = FoodLove.query.filter_by(food_id=id).count()
        return Response(json.dumps({"msg":'ok',"count":count,"loveid":foodLove.id}),content_type='application/json')

class FoodDelLove(MethodView):
    """删除关注"""
    def get(self,loveid):
        data = request.args.get('id')
        print('打印id数据', data)
        foodLove = FoodLove.query.get(loveid)
        foodLove.delete()
        count  = FoodLove.query.filter_by(food_id=data).count()
        return Response(json.dumps({"mag":'ok',"count":count}),content_type='application/json')
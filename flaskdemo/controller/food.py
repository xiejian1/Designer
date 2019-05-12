import json

from flask import render_template, request, Response
from flask.views import View, MethodView

from flaskdemo.model.models import Food, FoodContent


class Foodlist(View):
    """美食list集合"""
    def dispatch_request(self):
        print('获取美食专题列表')
        foods = Food.query.all()

        return render_template('microblog/home.html',foods=foods)



class Fooddetail(MethodView):
    """美食制作详细过程页"""
    def get(self,id):

        return render_template('microblog/fooddetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        # data = request.get_data()
        # data = json.loads(data)
        # id = data.get('id')
        foodcontent = FoodContent.query.filter_by(food_id=id).first()
        print(foodcontent.content)
        return Response(json.dumps({'html':str(foodcontent.content),'msg':'ok'}),content_type='application/json')
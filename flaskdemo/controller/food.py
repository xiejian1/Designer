import json

from flask import render_template, request, Response
from flask.views import View, MethodView

from flaskdemo.model.models import Food, FoodContent


class Foodlist(View):
    """美食list集合"""
    def dispatch_request(self):
        print('get food home type！')
        print('the request url is ',request.url)
        print('获取远程的ip地址',request.remote_addr)
        if not 'page' in request.args:
            print('默认不传参数')
            print('the request path is ', request.path)
            foodtype = str(request.path).rsplit('/',2)[1]
            print('print the type', foodtype)
            page = int(1)
            per_page = int(8)
            # paginate = Food.query.paginate(page, per_page, error_out=False)
            paginate = Food.query.filter(Food.food_type=='home').order_by(Food.food_date.desc())\
                .paginate(page, per_page, error_out=False)
            foods = paginate.items
            return render_template('microblog/home.html',paginate=paginate,foods=foods)
        else:
            print('传入参数')
            print('the request path is ',request.path)
            page = int(request.args.get('page'))
            per_page = int(8)
            foodtype = str(request.path).split('/',2)[1]
            print('print the type', foodtype)
            # paginate = Food.query.paginate(page, per_page, error_out=False)
            paginate = Food.query.filter(Food.food_type == foodtype).order_by(Food.food_date.desc()) \
                .paginate(page, per_page, error_out=False)
            foods = paginate.items
            return render_template('microblog/home.html', paginate=paginate, foods=foods)

class Fooddetail(MethodView):
    """美食制作详细过程页"""
    def get(self,id):
        return render_template('microblog/fooddetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        foodcontent = FoodContent.query.filter_by(food_id=id).first()
        print(foodcontent.content)
        return Response(json.dumps({'html':str(foodcontent.content),'msg':'ok'}),content_type='application/json')

#蔬菜分类
class Vegetablelist(View):
    """美食list集合"""
    def dispatch_request(self):
        print('get food home type！')
        print('the request url is ',request.url)
        if not 'page' in request.args:
            print('默认不传参数')
            print('the request path is ', request.path)
            foodtype = str(request.path).rsplit('/',2)[1]
            print('print the type', foodtype)
            page = int(1)
            per_page = int(8)
            # paginate = Food.query.paginate(page, per_page, error_out=False)
            paginate = Food.query.filter(Food.food_type==foodtype).order_by(Food.food_date.desc())\
                .paginate(page, per_page, error_out=False)
            foods = paginate.items
            return render_template('microblog/food/vegetables.html',paginate=paginate,foods=foods)
        else:
            print('传入参数')
            print('the request path is ',request.path)
            page = int(request.args.get('page'))
            per_page = int(8)
            foodtype = str(request.path).split('/',2)[1]
            print('print the type', foodtype)
            # paginate = Food.query.paginate(page, per_page, error_out=False)
            paginate = Food.query.filter(Food.food_type == foodtype).order_by(Food.food_date.desc()) \
                .paginate(page, per_page, error_out=False)
            foods = paginate.items
            return render_template('microblog/food/vegetables.html', paginate=paginate, foods=foods)


class Vegetabledetail(MethodView):
    """美食制作详细过程页"""
    def get(self,id):
        return render_template('microblog/fooddetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        foodcontent = FoodContent.query.filter_by(food_id=id).first()
        print(foodcontent.content)
        return Response(json.dumps({'html':str(foodcontent.content),'msg':'ok'}),content_type='application/json')

#小吃分类
#蔬菜分类
class Snacklist(View):
    """美食list集合"""
    def dispatch_request(self):
        print('get food home type！')
        print('the request url is ',request.url)
        if not 'page' in request.args:
            print('默认不传参数')
            print('the request path is ', request.path)
            foodtype = str(request.path).rsplit('/',2)[1]
            print('print the type', foodtype)
            page = int(1)
            per_page = int(8)
            # paginate = Food.query.paginate(page, per_page, error_out=False)
            paginate = Food.query.filter(Food.food_type==foodtype).order_by(Food.food_date.desc())\
                .paginate(page, per_page, error_out=False)
            foods = paginate.items
            return render_template('microblog/food/snack.html',paginate=paginate,foods=foods)
        else:
            print('传入参数')
            print('the request path is ',request.path)
            page = int(request.args.get('page'))
            per_page = int(8)
            foodtype = str(request.path).split('/',2)[1]
            print('print the type', foodtype)
            # paginate = Food.query.paginate(page, per_page, error_out=False)
            paginate = Food.query.filter(Food.food_type == foodtype).order_by(Food.food_date.desc()) \
                .paginate(page, per_page, error_out=False)
            foods = paginate.items
            return render_template('microblog/food/snack.html', paginate=paginate, foods=foods)


class Snackdetail(MethodView):
    """美食制作详细过程页"""
    def get(self,id):
        return render_template('microblog/fooddetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        foodcontent = FoodContent.query.filter_by(food_id=id).first()
        print(foodcontent.content)
        return Response(json.dumps({'html':str(foodcontent.content),'msg':'ok'}),content_type='application/json')

#汤类分类
class Souplist(View):
    """美食list集合"""
    def dispatch_request(self):
        print('get food home type！')
        print('the request url is ',request.url)
        print('获取远程的ip地址',request.remote_addr)
        if not 'page' in request.args:
            print('默认不传参数')
            print('the request path is ', request.path)
            foodtype = str(request.path).rsplit('/',2)[1]
            print('print the type', foodtype)
            page = int(1)
            per_page = int(8)
            # paginate = Food.query.paginate(page, per_page, error_out=False)
            paginate = Food.query.filter(Food.food_type==foodtype).order_by(Food.food_date.desc())\
                .paginate(page, per_page, error_out=False)
            foods = paginate.items
            return render_template('microblog/food/soup.html',paginate=paginate,foods=foods)
        else:
            print('传入参数')
            print('the request path is ',request.path)
            page = int(request.args.get('page'))
            per_page = int(8)
            foodtype = str(request.path).split('/',2)[1]
            print('print the type', foodtype)
            # paginate = Food.query.paginate(page, per_page, error_out=False)
            paginate = Food.query.filter(Food.food_type == foodtype).order_by(Food.food_date.desc()) \
                .paginate(page, per_page, error_out=False)
            foods = paginate.items
            return render_template('microblog/food/soup.html', paginate=paginate, foods=foods)


class Soupdetail(MethodView):
    """美食制作详细过程页"""
    def get(self,id):
        return render_template('microblog/fooddetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        foodcontent = FoodContent.query.filter_by(food_id=id).first()
        print(foodcontent.content)
        return Response(json.dumps({'html':str(foodcontent.content),'msg':'ok'}),content_type='application/json')

from flask import render_template
from flask.views import View

from flaskdemo.model.models import Food, Picture


class ShowUsers(View):

    def dispatch_request(self):
        print("回到首页！")
        food = Food.query.order_by(Food.food_date.desc()).limit(3)
        print('获取值!',food)
        picture = Picture.query.order_by(Picture.pic_date.desc()).limit(3)
        return render_template("microblog/index.html",\
                               foods=food,pictures=picture)
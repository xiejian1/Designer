from flask import render_template
from flask.views import View


class Foodlist(View):
    """美食list集合"""
    def dispatch_request(self):
        print('获取美食专题列表')
        return render_template('microblog/foodlist.html')
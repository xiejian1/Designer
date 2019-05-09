from flask import render_template
from flask.views import View


class Foodlist(View):
    """美食list集合"""
    def dispatch_request(self):
        print('获取美食专题列表')
        return render_template('microblog/foodlist.html')



class Fooddetail(View):
    """美食制作详细过程页"""
    def dispatch_request(self):

        return render_template('microblog/fooddetail.html')
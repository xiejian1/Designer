from flask import render_template
from flask.views import View


class Pictruelist(View):
    """图片列表"""
    def dispatch_request(self):

        print('获取图片列表')
        return render_template('microblog/picturelist.html')

class Picturedetail(View):
    """图片设计详细信息"""
    def dispatch_request(self):
        print('获取图片设计详情页')
        return render_template('microblog/picturedetail.html')
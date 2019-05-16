import json

from flask import render_template, request, Response
from flask.views import View, MethodView

from flaskdemo.model.models import Picture, PictureContent


class Pictruelist(View):
    """图片列表"""
    """美食list集合"""
    def dispatch_request(self):
        print('获取美食专题列表')
        if not 'page' in request.args:
            print('默认不传参数')
            page = int(1)
            per_page = int(8)
            paginate = Picture.query.paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picturelist.html', paginate=paginate, pictures=pics)
        else:
            print('传入参数')
            page = int(request.args.get('page'))
            per_page = int(8)
            paginate = Picture.query.paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picturelist.html',paginate=paginate,pictures = pics)


class Picturedetail(MethodView):
    """美食制作详细过程页"""
    def get(self,id):
        return render_template('microblog/picturedetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        picturecontent = PictureContent.query.filter_by(picture_id=id).first()
        print(picturecontent.content)
        return Response(json.dumps({'html':str(picturecontent.content),'msg':'ok'}),content_type='application/json')
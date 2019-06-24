import json

from flask import render_template, request, Response
from flask.views import MethodView

from flaskdemo.model.models import Picture, PictureComment, Food, FoodComment
import datetime

class PictureComments(MethodView):
    """对内容进行评论"""
    def get(self,pictureid):
        picture = Picture.query.get(pictureid)
        comments = PictureComment.query.filter(PictureComment.picture_id==pictureid).order_by(PictureComment.comment_time.desc()).all()

        return render_template('microblog/picture/comments.html',picture=picture,comments=comments)


class PComment(MethodView):
    """文章评论"""
    def post(self):

        data = request.get_data()
        data = json.loads(data)
        qq = data.get('qq')
        qqname = data.get('qqname')
        ip = data.get('ip')
        area = data.get('area')
        content = data.get('content')
        comment_time = datetime.date.today()
        id = data.get('pictureid')
        pictureComment = PictureComment()

        pictureComment.picture_id = id
        pictureComment.qq = qq
        pictureComment.qqname = qqname
        pictureComment.remote_area = area
        pictureComment.remote_addr = ip
        pictureComment.comment_time = comment_time
        pictureComment.comment_content = content

        pictureComment.save()

        return Response(json.dumps({'msg':'ok'}),content_type='application/json')
#美食的评论
class FoodComments(MethodView):
    """对内容进行评论"""
    def get(self,pictureid):
        picture = Food.query.get(pictureid)
        comments = FoodComment.query.filter(FoodComment.food_id==pictureid).order_by(FoodComment.comment_time.desc()).all()

        return render_template('microblog/food/comments.html',picture=picture,comments=comments)


class FComment(MethodView):
    """文章评论"""
    def post(self):

        data = request.get_data()
        data = json.loads(data)
        qq = data.get('qq')
        qqname = data.get('qqname')
        ip = data.get('ip')
        area = data.get('area')
        content = data.get('content')
        comment_time = datetime.date.today()
        id = data.get('pictureid')
        pictureComment = FoodComment()

        pictureComment.food_id = id
        pictureComment.qq = qq
        pictureComment.qqname = qqname
        pictureComment.remote_area = area
        pictureComment.remote_addr = ip
        pictureComment.comment_time = comment_time
        pictureComment.comment_content = content

        pictureComment.save()

        return Response(json.dumps({'msg':'ok'}),content_type='application/json')
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
            print('print the request url',request.url)
            picturetype = str(request.path).rsplit('/',2)[1]
            print('print the picture type',picturetype)
            paginate = Picture.query.filter(Picture.pic_type == picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picturelist.html', paginate=paginate, pictures=pics)
        else:
            print('传入参数')
            print('print the request url',request.url)
            page = int(request.args.get('page'))
            per_page = int(8)
            print('print the request path',request.path)
            picturetype = str(request.path).rsplit('/',2)[1]
            print('print the type ',picturetype)
            paginate = Picture.query.filter(Picture.pic_type==picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picturelist.html',paginate=paginate,pictures = pics)


class Picturedetail(MethodView):

    """美食制作详细过程页"""
    def get(self,id):
        print('print the url',request.url)
        print('print the path',request.path)
        return render_template('microblog/picturedetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        print('print the url',request.url)
        print('print the path',request.path)
        picturecontent = PictureContent.query.filter_by(picture_id=id).first()
        print(picturecontent.content)
        return Response(json.dumps({'html':str(picturecontent.content),'msg':'ok'}),content_type='application/json')

class Palettelist(View):
    """图片列表"""
    """美食list集合"""
    def dispatch_request(self):
        print('获取美食专题列表')
        if not 'page' in request.args:
            print('默认不传参数')
            page = int(1)
            per_page = int(8)
            print('print the request url',request.url)
            picturetype = str(request.path).rsplit('/',2)[1]
            print('print the picture type',picturetype)
            paginate = Picture.query.filter(Picture.pic_type == picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/palette.html', paginate=paginate, pictures=pics)
        else:
            print('传入参数')
            print('print the request url',request.url)
            page = int(request.args.get('page'))
            per_page = int(8)
            print('print the request path',request.path)
            picturetype = str(request.path).split('/',2)[1]
            print('print the type ',picturetype)
            paginate = Picture.query.filter(Picture.pic_type==picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/palette.html',paginate=paginate,pictures = pics)


class Palettedetail(MethodView):

    """美食制作详细过程页"""
    def get(self,id):
        print('print the url',request.url)
        print('print the path',request.path)
        return render_template('microblog/picturedetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        print('print the url',request.url)
        print('print the path',request.path)
        picturecontent = PictureContent.query.filter_by(picture_id=id).first()
        print(picturecontent.content)
        return Response(json.dumps({'html':str(picturecontent.content),'msg':'ok'}),content_type='application/json')

class Finishinglist(View):
    """图片列表"""
    """美食list集合"""
    def dispatch_request(self):
        print('获取图片专题列表')
        if not 'page' in request.args:
            print('默认不传参数')
            page = int(1)
            per_page = int(8)
            print('print the request url',request.url)
            picturetype = str(request.path).rsplit('/',2)[1]
            print('print the picture type',picturetype)
            paginate = Picture.query.filter(Picture.pic_type == picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/finishing.html', paginate=paginate, pictures=pics)
        else:
            print('传入参数')
            print('print the request url',request.url)
            page = int(request.args.get('page'))
            per_page = int(8)
            print('print the request path',request.path)
            picturetype = str(request.path).split('/',2)[1]
            print('print the type ',picturetype)
            paginate = Picture.query.filter(Picture.pic_type==picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/finishing.html',paginate=paginate,pictures = pics)


class Finishingdetail(MethodView):

    """美食制作详细过程页"""
    def get(self,id):
        print('print the url',request.url)
        print('print the path',request.path)
        return render_template('microblog/picturedetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        print('print the url',request.url)
        print('print the path',request.path)
        picturecontent = PictureContent.query.filter_by(picture_id=id).first()
        print(picturecontent.content)
        return Response(json.dumps({'html':str(picturecontent.content),'msg':'ok'}),content_type='application/json')

class Photographylist(View):
    """图片列表"""
    """美食list集合"""
    def dispatch_request(self):
        print('获取图片专题列表')
        if not 'page' in request.args:
            print('默认不传参数')
            page = int(1)
            per_page = int(8)
            print('print the request url',request.url)
            picturetype = str(request.path).rsplit('/',2)[1]
            print('print the picture type',picturetype)
            paginate = Picture.query.filter(Picture.pic_type == picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/photography.html', paginate=paginate, pictures=pics)
        else:
            print('传入参数')
            print('print the request url',request.url)
            page = int(request.args.get('page'))
            per_page = int(8)
            print('print the request path',request.path)
            picturetype = str(request.path).split('/',2)[1]
            print('print the type ',picturetype)
            paginate = Picture.query.filter(Picture.pic_type==picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/photography.html',paginate=paginate,pictures = pics)


class Photographydetail(MethodView):

    """美食制作详细过程页"""
    def get(self,id):
        print('print the url',request.url)
        print('print the path',request.path)
        return render_template('microblog/picturedetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        print('print the url',request.url)
        print('print the path',request.path)
        picturecontent = PictureContent.query.filter_by(picture_id=id).first()
        print(picturecontent.content)
        return Response(json.dumps({'html':str(picturecontent.content),'msg':'ok'}),content_type='application/json')

class Illustrationlist(View):
    """图片列表"""
    """美食list集合"""
    def dispatch_request(self):
        print('获取图片专题列表')
        if not 'page' in request.args:
            print('默认不传参数')
            page = int(1)
            per_page = int(8)
            print('print the request url',request.url)
            picturetype = str(request.path).rsplit('/',2)[1]
            print('print the picture type',picturetype)
            paginate = Picture.query.filter(Picture.pic_type == picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/illustration.html', paginate=paginate, pictures=pics)
        else:
            print('传入参数')
            print('print the request url',request.url)
            page = int(request.args.get('page'))
            per_page = int(8)
            print('print the request path',request.path)
            picturetype = str(request.path).split('/',2)[1]
            print('print the type ',picturetype)
            paginate = Picture.query.filter(Picture.pic_type==picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/illustration.html',paginate=paginate,pictures = pics)


class Illustrationdetail(MethodView):

    """美食制作详细过程页"""
    def get(self,id):
        print('print the url',request.url)
        print('print the path',request.path)
        return render_template('microblog/picturedetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        print('print the url',request.url)
        print('print the path',request.path)
        picturecontent = PictureContent.query.filter_by(picture_id=id).first()
        print(picturecontent.content)
        return Response(json.dumps({'html':str(picturecontent.content),'msg':'ok'}),content_type='application/json')


class Artistlist(View):
    """图片列表"""
    """美食list集合"""
    def dispatch_request(self):
        print('获取图片专题列表')
        if not 'page' in request.args:
            print('默认不传参数')
            page = int(1)
            per_page = int(8)
            print('print the request url',request.url)
            picturetype = str(request.path).rsplit('/',2)[1]
            print('print the picture type',picturetype)
            paginate = Picture.query.filter(Picture.pic_type == picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/artist.html', paginate=paginate, pictures=pics)
        else:
            print('传入参数')
            print('print the request url',request.url)
            page = int(request.args.get('page'))
            per_page = int(8)
            print('print the request path',request.path)
            picturetype = str(request.path).split('/',2)[1]
            print('print the type ',picturetype)
            paginate = Picture.query.filter(Picture.pic_type==picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/artist.html',paginate=paginate,pictures = pics)


class Artistdetail(MethodView):

    """美食制作详细过程页"""
    def get(self,id):
        print('print the url',request.url)
        print('print the path',request.path)
        return render_template('microblog/picturedetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        print('print the url',request.url)
        print('print the path',request.path)
        picturecontent = PictureContent.query.filter_by(picture_id=id).first()
        print(picturecontent.content)
        return Response(json.dumps({'html':str(picturecontent.content),'msg':'ok'}),content_type='application/json')

class Posterslist(View):
    """图片列表"""
    """美食list集合"""
    def dispatch_request(self):
        print('获取图片专题列表')
        if not 'page' in request.args:
            print('默认不传参数')
            page = int(1)
            per_page = int(8)
            print('print the request url',request.url)
            picturetype = str(request.path).rsplit('/',2)[1]
            print('print the picture type',picturetype)
            paginate = Picture.query.filter(Picture.pic_type == picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/posters.html', paginate=paginate, pictures=pics)
        else:
            print('传入参数')
            print('print the request url',request.url)
            page = int(request.args.get('page'))
            per_page = int(8)
            print('print the request path',request.path)
            picturetype = str(request.path).split('/',2)[1]
            print('print the type ',picturetype)
            paginate = Picture.query.filter(Picture.pic_type==picturetype).order_by(Picture.pic_date.desc())\
                .paginate(page, per_page, error_out=False)
            pics = paginate.items
            return render_template('microblog/picture/posters.html',paginate=paginate,pictures = pics)


class Postersdetail(MethodView):

    """美食制作详细过程页"""
    def get(self,id):
        print('print the url',request.url)
        print('print the path',request.path)
        return render_template('microblog/picturedetail.html',id=id)

    def post(self,id):
        """返回内容"""
        print('food 详细信息')
        print('print the url',request.url)
        print('print the path',request.path)
        picturecontent = PictureContent.query.filter_by(picture_id=id).first()
        print(picturecontent.content)
        return Response(json.dumps({'html':str(picturecontent.content),'msg':'ok'}),content_type='application/json')
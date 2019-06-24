

from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash,check_password_hash



#数据库操作基本类
# from flaskdemo import create_app
from flaskdemo.model.exts import db
# from flask_sqlalchemy import SQLAlchemy
# app = create_app()
# db = SQLAlchemy(app)
class ModelBase:
    # 添加一条数据
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()  # 提交 默认开启了事物
        except:
            db.session.rollback()  # 回滚

    # 添加多条数据
    @staticmethod
    def saveAll(*args):
        try:
            db.session.add_all(args)
            db.session.commit()  # 提交 默认开启了事物
        except:
            db.session.rollback()  # 回滚

    # 删除一条数据
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()  # 提交 默认开启了事物
        except:
            db.session.rollback()  # 回滚

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36),primary_key=True)
    email = db.Column(db.String(50),unique = True)
    name = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # def __int__(self,id,email,name,password):
    #     self.id = id
    #     self.email = email
    #     self.name = name
    #     self.password = password

    def set_password(self,password):
        """对明文的密码进行加密，返回加密的密码"""
        return generate_password_hash(password)

    def check_password(self,password):
        """检查密码。传入明文的密码，将明文密码进行加密然后进行比对"""
        return check_password_hash(self.password,password)
    def __repr__(self):
        return "Role: %s %s" % (self.id, self.name)


# class Role(db.Model):
#     # 定义表名
#     __tablename__ = 'roles'
#     # 定义列对象
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     #描述方法
#     us = db.relationship('User', backref='role')
#
#     # repr()方法显示一个可读字符串
#     def __repr__(self):
#         return 'Role:%s' % self.name


class Food(ModelBase,db.Model):
    """美食数据模型"""
    __tablename__ = 'food'
    id = db.Column(db.String(32),primary_key=True,unique=True,nullable=True)
    food_type = db.Column(db.String(20),nullable=True)
    food_title = db.Column(db.String(200),nullable=True)
    food_desc = db.Column(db.String(500))
    food_abstract = db.Column(db.String(200))
    food_date = db.Column(db.Date,nullable=True)
    # 创建关系属性  relationship("关联的类名", backref="对方表查询关联数据时的属性名")
    foodpic = db.relationship("FoodPic",backref='food',lazy='dynamic',cascade='all,delete-orphan', passive_deletes = True)
    foodcontent = db.relationship("FoodContent",backref=backref("food", uselist=False),lazy="dynamic",cascade='all,delete-orphan', passive_deletes = True)
    foodlove = db.relationship("FoodLove",backref="food",lazy="dynamic",cascade='all,delete-orphan', passive_deletes = True)
    foodcomment = db.relationship("FoodComment",backref="food",lazy="dynamic",cascade='all,delete-orphan', passive_deletes = True)

class FoodPic(ModelBase,db.Model):
    """美食图片保存"""
    __tablename__ = 'foodpic'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    pic_url = db.Column(db.String(50),nullable=True)
    food_id = db.Column(db.String(32),db.ForeignKey("food.id",ondelete='CASCADE'))


class FoodContent(ModelBase,db.Model):
    """美食详细信息"""
    __tablename__ ="foodcontent"
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    content = db.Column(db.Text,nullable=True)
    food_id = db.Column(db.String(32),db.ForeignKey("food.id",ondelete='CASCADE'))

class FoodLove(ModelBase,db.Model):
    """点击关注"""
    __tablename__="foodlove"
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    remote_addr = db.Column(db.String(32),nullable=True)
    remote_area = db.Column(db.String(32), nullable=True)
    love_time = db.Column(db.Date,nullable=True)
    food_id = db.Column(db.String(32),db.ForeignKey("food.id",ondelete='CASCADE'))

class FoodComment(ModelBase,db.Model):
    """评论"""
    __tablename__="foodcomment"
    id = db.Column(db.Integer,autoincrement = True,primary_key = True)
    remote_addr = db.Column(db.String(32),nullable=True)
    comment_content = db.Column(db.String(500),nullable=True)
    comment_time = db.Column(db.Date,nullable=True)
    qq = db.Column(db.String(30),nullable=True)
    qqname = db.Column(db.String(50),nullable=True)
    food_id = db.Column(db.String(32),db.ForeignKey("food.id",ondelete='CASCADE'))


class Picture(ModelBase,db.Model):
    """美食数据模型"""
    __tablename__ = 'picture'
    id = db.Column(db.String(32),primary_key=True,unique=True,nullable=True)
    pic_type = db.Column(db.String(20),nullable=True)
    pic_title = db.Column(db.String(200),nullable=True)
    pic_abstract = db.Column(db.String(200),nullable=True)
    pic_desc = db.Column(db.String(500))
    pic_date = db.Column(db.Date, nullable=True)
    # 创建关系属性  relationship("关联的类名", backref="对方表查询关联数据时的属性名")
    picturepic = db.relationship("PicturePic",backref='picture',lazy='dynamic',cascade='all,delete-orphan',
                               passive_deletes=True)
    picturecontent = db.relationship("PictureContent",backref=backref("picture",uselist=False),cascade='all,delete-orphan',
                               passive_deletes=True)
    picturelove = db.relationship("PictureLove", backref="picture", lazy="dynamic",cascade='all,delete-orphan',
                               passive_deletes=True)
    picturecomment = db.relationship("PictureComment", backref="picture", lazy="dynamic",cascade='all,delete-orphan',
                                  passive_deletes=True)

class PicturePic(ModelBase,db.Model):
    """美食图片保存"""
    __tablename__ = 'picturepic'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    pic_url = db.Column(db.String(50),nullable=True)
    picture_id = db.Column(db.String(32),db.ForeignKey("picture.id",ondelete='CASCADE'))


class PictureContent(ModelBase,db.Model):
    """美食详细信息"""
    __tablename__ ="picturecontent"
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    content = db.Column(db.Text,nullable=True)
    picture_id = db.Column(db.String(32),db.ForeignKey("picture.id",ondelete='CASCADE'))

class PictureLove(ModelBase,db.Model):
    """点击关注"""
    __tablename__="picturelove"
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    remote_addr = db.Column(db.String(32),nullable=True)
    picture_time = db.Column(db.Date,nullable=True)
    remote_area = db.Column(db.String(32),nullable=True)
    picture_id = db.Column(db.String(32),db.ForeignKey("picture.id",ondelete='CASCADE'))

class PictureComment(ModelBase,db.Model):
    """评论"""
    __tablename__="picturecomment"
    id = db.Column(db.Integer,autoincrement = True,primary_key = True)
    remote_addr = db.Column(db.String(32),nullable=True)
    remote_area = db.Column(db.String(50),nullable=True)
    comment_content = db.Column(db.String(500),nullable=True)
    comment_time = db.Column(db.Date,nullable=True)
    qq = db.Column(db.String(30),nullable=True)
    qqname = db.Column(db.String(50),nullable=True)
    picture_id = db.Column(db.String(32),db.ForeignKey("picture.id",ondelete='CASCADE'))


if __name__ =="__main__":
    # db.drop_all()
    db.create_all()
    app.run(debug=True)

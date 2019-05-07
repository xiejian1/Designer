from flask_sqlalchemy import  SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
db = SQLAlchemy()


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

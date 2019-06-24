import sqlalchemy

from flaskdemo.model.models import PictureComment


def cut_desc(desc):
    """自定义过滤器，截取部分长度"""
    if len(desc)>50:
        return desc[:50]
    else:
        return desc[0:len(desc)]
def cut_descs(desc):
    """截取后面部分的字符串"""
    if len(desc):
        return desc[51:101]

def toStr(content):
    """将数据转换为字符串"""
    return str(content)

def lovecount(Love):
    """查询关注点数量"""
    count = Love.count()
    return count

def commentcount(Comment):
    """查询评论的总数"""
    count = Comment.count()
    return count

#首页只取到第一张图片
def foodpic(foodpic):
    """从多张图片中取到第一张图片"""
    print('提取出照片')
    if foodpic.count() > 0:
        pic = foodpic.all()[0]
        return pic.pic_url

#首页只取到第一张图片设计照片
def picturepic(picturepic):
    """从多张图片中取到第一张图片"""
    print('提取出照片')
    if picturepic.count()>0:
        pic = picturepic.all()[0]
        return pic.pic_url
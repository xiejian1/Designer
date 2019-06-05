import os

from werkzeug.routing import BaseConverter

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.abspath(os.path.join(BASE_DIR,'static/img/upload/'))


# 2、自定义类
# 转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(self)
        # print items # (u'[a-z]{3}[A-Z]{3}',)
        # print url_map # URL 的一个MAP对象，类似路由表
        self.regex = items[0]

# 3、要将定义的类注册到APP的url_map中，定义名称
# app.url_map.converters['regex'] = RegexConverter
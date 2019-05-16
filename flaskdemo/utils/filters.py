
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
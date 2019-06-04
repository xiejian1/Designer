from elasticsearch import Elasticsearch

class Elastic():
    """elasticsearch 查询删除文档"""
    def __init__(self,index,doctype):
        self.index = index
        self.doctype = doctype

        self.es = Elasticsearch(['localhost'],http_auth=('smallqiang', 'MuQEX6bhnuJ6c123Xd'),port=9200)
    def conn(self):
        """对elasticseach进行连接"""
        return self.es


    def getdataByid(self,id=''):
        """根据id获取数据"""
        res = self.es.get(index=self.index,id=id,doc_type=self.doctype)
        print('打印查询到的数据',res['_source'])
        print('===================================')
        print('打印标题',res['_source']['tender_title'])

    def getdataBybody(self,id):
        """根据body获取数据"""
        doc = {
            "query":{
                "match":{
                    "id":id
                }
            }
        }
        res = self.es.search(index=self.index,body=doc)
        print('打印获取的数据',res['hits']['total'])
        for data in res['hits']['hits']:
            print('打印真实的数据',data['_source']['tender_title'])
    def deleteById(self,id):
        """根据id删除数据"""
        res = self.es.delete(index=self.index,doc_type=self.doctype,id=id)
        print('打印删除的结果',res)


if __name__ =="__main__":
    obj = Elastic(index='cqcyit_v3',doctype='tender')
    id = 'f690da2627f78f87edc7ccf1f63ff9f68a427a8f'
    obj.deleteById(id=id)

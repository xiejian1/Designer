import time
import datetime
def timechuo():
    """打印时间戳"""

    print('打印原始时间戳:',time.time())
    print('打印整形时间戳',int(time.time()))

    print('打印13位时间戳',int(round(time.time()*10000)))
def getdatenow():
    """获取系统当前时间"""
    datenow = datetime.datetime.now()
    print("打印当前时间",datenow)

def stringdate():
    """将时间格式转换为字符串"""
    datenow = datetime.datetime.now()
    print('打印系统时间年份',datenow.year)
    strdate = datetime.datetime.strftime(datenow,"%Y-%m-%d")
    print(datetime.date.today())
    print('将时间格式转换为字符串',strdate)

def dateTostr():
    """将字符串转换为shijian格式"""
    datestr = '2019-05-10'
    datenow = datetime.datetime.strptime(datestr,"%Y-%m-%d")
    print('取到时间戳的某一部分!')
    print('打印转换后的时间',datenow)
    strdate = datetime.datetime.strftime(datenow,"%Y-%m-%d")
    print('打印转换后的时间',strdate)

def dateStr():
    """打印年月日形式的数据"""
    d = datetime.datetime.date()
    print('打印年月日形式的数据')
    print("打印时间",d)

class Graph(object):
    """图的深度优先算法，
    访问初始顶点v并且标记顶点已经被访问了，
    查找定点v的第一个邻接顶点w，如果w存在，则继续执行，否则就退回v,再找v的另一个未被访问的邻接顶点，
    如定点w未被访问，则访问顶点w，被标记顶点w为已访问，
    继续查找顶点w的下一个邻接顶点wj,返回执行，直到所有的顶点全部被访问过为止"""
    def __init__(self,*args,**kwargs):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self,nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self,node):
        if not node in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self,edge):
        """添加边缘,相互为邻接顶点"""
        u,v = edge
        if(v not in self.node_neighbors[u]) and ( u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if (u!=v):
                self.node_neighbors[v].append(u)
    def nodes(self):
        return self.node_neighbors.keys()

    def depth_first_search(self,root=None):
        """内部装饰器"""
        order = []
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)
        if root:
            dfs(root)

        for node in self.nodes():
            if not node in self.visited:
                dfs(node)
        print(order)
        return order

    def breadth_first_search(self, root=None):
        """广度优先算法,
        顶点v入队列，
        当队列非空时则继续执行，否则结束
        出队列，取得对头顶点v,访问顶点v，并标记顶点v已被访问
        查找顶点v的第一个邻接顶点col,
        若v的邻接顶点col未被访问过，则入col队列
        继续查找顶点v的另一个邻接顶点col"""
        queue = []
        order = []

        def bfs():
            while len(queue) > 0:
                node = queue.pop(0)

                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in queue):
                        queue.append(n)
                        order.append(n)
        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.nodes():
            if not node in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
        print(order)
        return order
if __name__ =="__main__":
    # timechuo()
    # stringdate()
    # g = Graph()
    # g.add_nodes([i + 1 for i in range(8)])
    # g.add_edge((1, 2))
    # g.add_edge((1, 3))
    # g.add_edge((2, 4))
    # g.add_edge((2, 5))
    # g.add_edge((4, 8))
    # g.add_edge((5, 8))
    # g.add_edge((3, 6))
    # g.add_edge((3, 7))
    # g.add_edge((6, 7))
    # print("nodes:", g.nodes())
    # order = g.breadth_first_search(1)
    # order = g.depth_first_search(1)
    #dateStr()
    stringdate()
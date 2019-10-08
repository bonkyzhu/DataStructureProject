from queue import PriorityQueue as PQ

class PriorityQueue(PQ):
  ''' 
  优先队列， 继承 Python 标准类 PriorityQueue， 将按照权值小的排序 
  '''
  def __init__(self, *option):
    super().__init__(*option)

  def put(self, item):
    ''' 
    将结点按照权值在前的放入优先队列

    param item： 要放入队列的边 
    '''
    super().put(item[::-1])

  def get(self):
    ''' 
    删除并得到队列的第一个元素

    return ： 按照原样输出边 （起点, 终点, 权值） （tuple） 
    '''
    return super().get()[::-1]

  def top(self):
    ''' 
    得到第一个元素但不在队列删除

    return top_node： 输出队列第一个元素 （起点, 终点, 权值） （tuple） 
    '''
    size = self.qsize() 
    top_node = self.get() 
    self.put(top_node)

    for i in range(size-1):
      self.put(self.get())
    
    return top_node

class MFSet:
  ''' 
  并查集， 用于存储在 Kruskal 算法产生的树 
  '''
  def __init__(self):
    ''' 
    sets 并查集 
    edge_set 边集
    ''' 
    self.sets = set() 
    self.edge_set = set() 
    
  def Initial(self, item):
    ''' 
    初始化并查集， 将 item 加入并查集 
    
    param item： 加入并查集的元素 (tuple) 
    ''' 
    self.sets.add(frozenset(item)) 
  
  def Merge(self, item_a, item_b):
    ''' 
    合并 a 和 b 两个并查集 

    param item_a, item_b : 需要被合并的两个并查集 （set） 
    ''' 
    a = self.Find(item_a) 
    b = self.Find(item_b) 
    self.sets.remove(a) 
    self.sets.remove(b) 
    self.sets.add(a.union(b)) 
    
  def Find(self, item):
    ''' 
    判断 item 在哪个并查集中
    param item ： 查询的元素 （set） 
    return s ： 返回 item 所包括的集合 
    ''' 
    for s in self.sets:
      if s.issuperset(frozenset(item)):
        return s 
    
    return None
  
  def __str__(self):
    string = ''
    for edge in self.edge_set:
      string += str(edge) 
      string += '\n'
    return string

def Kruskal(G):
  ''' 
  利用优先队列和并查集， 执行 Kruskal 算法

  param G : 带权图 (WeiGraph)

  return all_nodes: 返回用并查集表示的最小生成树 (MFSet) 
  '''

  all_nodes = MFSet()

  for node in G.nodes:
    all_nodes.Initial(node)
  
  queue = PriorityQueue()

  for edge in G.edges:
    queue.put(edge)

  while not queue.empty():
    (u, v, w) = queue.get() 
    if all_nodes.Find(u) != all_nodes.Find(v):
      all_nodes.edge_set.add((u, v, w))
      all_nodes.Merge(u, v)
  
  return all_nodes

def Prim(G):
  ''' 
  利用优先队列， 执行 Prim 算法

  param G : 带权图 (WeiGraph)

  return all_nodes: 返回用集合表示的最小生成树 (set) 
  '''

  all_nodes = set() 
  length = len(G.nodes) 
  total = 1 
  visit = {} 
  s = G.nodes[0]

  queue = PriorityQueue()

  for node in G.nodes:
    visit[node] = 0 
  visit[s] = 1

  while total < length:
    for (node, w) in G.adjs(s):
      if visit[node] == 0:
        nn = (s, node, w) 
        queue.put(nn)

    while not queue.empty() and visit[queue.top()[1]]: # 防止边访问不到的情况 
      queue.get()

    nn = queue.get() 
    all_nodes.add(nn) 
    s = nn[1] 
    visit[s] = 1 
    total += 1

  return all_nodes


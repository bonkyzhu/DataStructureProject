from graphviz import Digraph, Graph

class WeiGraph():
  ''' 
  带权图 
  '''
  def __init__(self, nodes, edges):
    ''' 
    nodes 结点集 
    edges 边集 
    graph 邻接表 
    G Graphviz.Graph 用于可视化图 
    '''
    self.nodes = nodes 
    self.edges = edges 
    self.graph = []

    for node in nodes:
      self.graph.append([(node, 0)])

    for (x, y, w) in edges:
      for n in self.graph:
        if n[0][0] == x:
          n.append((y, w)) 
        if n[0][0] == y:
          n.append((x, w))

    self.G = None

  def adjs(self, node):
    ''' 
    返回邻接表， 用于 Prim 算法
    param node ： 需要寻找邻接点的结点 
    return ： 邻接结点表 
    ''' 
    return list(filter(lambda n: n[0][0] == node, self.graph))[0][1:] #返回以 node 开始的邻接结点表

  def draw(self, color_filter=None):
    ''' 
    可视化所生成的图 
    ''' 
    if color_filter is None:
      color_filter = lambda edge: 'black' #全部为黑色 
    settings = dict(name='Graph', engine='circo', node_attr=dict(shape='circle')) 
    self.G = Graph(**settings) 

    for node in self.nodes:
      self.G.node(str(node), str(node)) 
    for (x, y, w) in self.edges:
      self.G.edge(str(x), str(y), label=str(w), color=color_filter((x, y, w))) 

    return self.G

def cf(tree):
  ''' 
  最小生成树用红色标出 
  ''' 
  def color_filter(edge):
    in_tree = filter(lambda t: t[:2] == edge[:2] or t[:2][::-1] == edge[:2],tree) 
    
    if len(list(in_tree)) > 0:
      return 'red' 
    return 'black' 
    
  return color_filter
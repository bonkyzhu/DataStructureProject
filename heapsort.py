import tkinter as tk 
import tkinter.messagebox as message 
import re

class Heap_Sort:
  ''' 
  执行堆排序 
  '''
  def __init__(self, window, tree):
    ''' 
    t_trees 临时存储 trees 
    trees 存储最小生成的树， 第 0 个元素是()，保证下标从 1 开始 
    tree——size 树的大小 
    '''
    self.window = window 
    self.match = re.compile("\'([a-zA-Z]+)\', \'([a-zA-Z]+)\', ([0-9]+)") 
    self.trees = [()] 
    self.tree_size = 0 
    self.on_hit = False 
    tk.Button(self.window,
              text='对生成树进行堆排序', 
              width=15, height=2, 
              command=self.hit).pack()

  def hit(self):
    '''
    按下按钮操作， 弹出窗口展示结果 
    ''' 
    self.trees = [()] 
    t_trees = [()]+re.findall(self.match, open('tree.txt').read())
    self.tree_size = len(t_trees)-1
    for i in range(1, self.tree_size+1):
      self.trees.append(
          (t_trees[i][0], t_trees[i][1], int(t_trees[i][2])))
    result = self.HeapSort() 
    message._show('堆排序结果', result)

  def HeapAdjust(self, low, high):
    ''' 
    调整堆，使其为大顶堆

    param : 调整的范围（low～high） 
    '''

    t_low = low 
    child = 2 * t_low # left 
    temp = self.trees[low]

    while child <= high:
      if child < high and self.trees[child][2] < self.trees[child + 1][2]:
        child += 1 # right

      if(temp[2] < self.trees[child][2]):
        self.trees[t_low] = self.trees[child] 
        t_low = child 
        child *= 2 
      else:
        break

    self.trees[t_low] = temp

  def HeapSort(self):
    ''' 
    进行对权值的堆排序

    return result : 堆排序的结果 (list) 
    '''
    result = []
    
    for i in range(self.tree_size//2, 0, -1):
      self.HeapAdjust(i, self.tree_size)

    for i in range(self.tree_size, 1, -1):
      self.trees[1], self.trees[i] = self.trees[i], self.trees[1] 
      self.HeapAdjust(1, i-1)

    for edge in self.trees:
      if edge:
        result.append(edge)

    return result
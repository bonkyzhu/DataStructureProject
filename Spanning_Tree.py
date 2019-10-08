import tkinter as tk 
import MFSet
import Visualize_Algorithm as va 
import tkinter.messagebox as message

class Spanning_Tree:
  ''' 
  最小生成树 
  '''
  def __init__(self, window, Graph):
    ''' 
    Gragh 需要生成最小生成树的图 tree 存储所生成的最小生成树 
    '''
    self.window = window 
    self.Graph = Graph 
    self.on_hit = False 
    self.tree = set() 
    tk.Button(window,
              text='可视化最小生成树', 
              width=15, height=2, 
              command=self.hit).pack()

  def hit(self):
    def run_Prim():
      ''' 
      执行 Prim 算法， 并执行最小生成树的可视化 
      '''
      wg = va.WeiGraph(self.Graph.vertex_string, self.Graph.graph) 
      self.tree = set(MFSet.Prim(wg))

      wg.draw(color_filter=va.cf(self.tree)).view() 
      message._show('Prim Spaning Tree', self.tree.__str__())

      with open("tree.txt", 'w') as file:
        file.write(str(self.tree))

    def run_Kruskal():
      ''' 
      执行 Kruskal 算法， 并执行最小生成树的可视化 
      '''
      wg = va.WeiGraph(self.Graph.vertex_string, self.Graph.graph) 
      self.tree = set(MFSet.Kruskal(wg).edge_set)

      wg.draw(color_filter=va.cf(self.tree)).view() 
      message._show('Kruskal Spaning Tree', self.tree.__str__())

      with open("tree.txt", 'w') as file:
        file.write(str(self.tree))
    
    if self.on_hit == False:
      entry_window = tk.Tk() 
      entry_window.title("Spanning Tree") 
      tk.Label(entry_window,
              text='Choosing Algorithm',
              font=('WenQuanYi MicroHei', 10),
              width=40, height=2
              ).pack() 
      entry_window.geometry("200x150")

      tk.Button(entry_window,
                text="Prim", 
                command=run_Prim ).pack()

      tk.Button(entry_window,
                text="Kruskal", 
                command=run_Kruskal ).pack()

      entry_window.mainloop ()
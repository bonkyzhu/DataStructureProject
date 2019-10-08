import tkinter as tk 
import Visualize_Algorithm as va 
from Input_Graph import Input_Graph 
from Spanning_Tree import Spanning_Tree 
from heapsort import Heap_Sort

class Menu:
 def __init__(self):
    ''' 
    生成图形界面
    - 输入图
    - 生成最小生成树
    - 输出堆排序结果 
    '''

    window = tk.Tk() 
    window.title("朱子权-20178859-数据结构课设") 
    window.geometry("400x300") 
    l = tk.Label(window, 
                text='最小生成树模拟程序', 
                font=('WenQuanYi MicroHei', 18), # 字体和字体大小
                width=40, height=2 # 标签长宽 
                ) 
    l.pack() 
    Graph = Input_Graph(window) 
    Tree = Spanning_Tree(window, Graph) 
    Heap_Sort(window, Tree.tree) 
    window.mainloop()

Menu()
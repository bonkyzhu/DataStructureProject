import tkinter as tk 
import Visualize_Algorithm as va 
import re 
import tkinter.messagebox as message 
import tkinter.filedialog as tkfile

class Input_Graph:
  '''
  输入图 
  '''
  def __init__(self, window):
    ''' 
    vertex_string 输入结点 （字符串表示）
    graph 边的集合 
    match 正则表达式匹配的 pattern 
    '''
    self.window = window 
    self.on_hit = False 
    self.vertex_string = '' 
    self.graph = set() 
    tk.Button(window,
              text='输入图',
              width=15, height=2,
              command=self.hit).pack() 
    self.match = re.compile("([a-zA-Z]+),([a-zA-Z]+),([0-9]+)")

  def hit(self):
    def match_case_and_print(string):
      ''' 
      对于输入的形式（‘str’, 'str', ‘str’），进行（‘str’, 'str', int）形式转化存入 graph 
      '''
      matched = re.findall(self.match, string) 

      if matched: 
        a = (matched[0][0], matched[0][1], int(matched[0][2])) 
        self.graph.add(a) 
        t.insert('end', '起始点：' + a[0]) 
        t.insert('end', '\t 终点：' + a[1]) 
        t.insert('end', '\t 权重：'+str(a[2])+'\n')
      else:
        message.showwarning('输入不合法', '按照起始点，终点，权重， 中间用逗号隔开格式输入')

    def get_vertex():
      ''' 
      得到结点列表， 并输出 
      '''
      self.vertex_string = er.get()
      if self.vertex_string:
        t.insert('end', '结点序号：\t'+self.vertex_string+'\n')

    def insert_end():
      ''' 
      得到边， 并输出 
      '''
      var = e.get() 
      match_case_and_print(var)

    def visualize():
      ''' 
      可视化所输入的图 
      '''
      wg = va.WeiGraph(self.vertex_string, self.graph) 
      wg.draw().view()

    def file_read():
      ''' 
      利用文件输入的方式输入图 
      '''
      file_name = tkfile.askopenfilename()
      judge = message.askyesno('警告', '选择文件输入会覆盖原有手动输入结果，确定 要执行此操作吗')
      if judge:
        file = open(file_name).read().split('\n') 
        self.graph = set() 
        self.vertex_string = file[0] 
        if self.vertex_string:
          t.insert('end', '结点序号：\t'+self.vertex_string+'\n')
        for i in range(1, len(file)):
          match_case_and_print(file[i])

    if self.on_hit == False:
      entry_window = tk.Tk() 
      entry_window.title("请输入你的图")
      entry_window.geometry("400x450")

    tk.Label(entry_window,
            text='输入图', 
            font=('WenQuanYi MicroHei', 18), 
            width=40, height=2 ).pack()
    frm = tk.Frame(entry_window) 
    frm.pack() 
    frm_l = tk.Frame(frm) 
    frm_r = tk.Frame(frm) 
    frm_l.pack(side='left') 
    frm_r.pack(side='right')

    tk.Label(frm_l, text='输入结点的字符串').pack() 
    er = tk.Entry(frm_r, show=None) 
    er.pack()

    tk.Label(frm_l, text='输入边的信息').pack() 
    e = tk.Entry(frm_r, show=None) 
    e.pack()

    tk.Label(entry_window, text='起始点，终点，权重(中间用逗号隔开)').pack()

    t = tk.Text(entry_window, height=10, width=40) 
    t.pack()

    tk.Button(entry_window,
              text="文件导入数据", 
              command=file_read ).pack()

    tk.Button(entry_window,
              text="插入结点", 
              command=get_vertex ).pack()

    tk.Button(entry_window,
              text="插入边", 
              command=insert_end ).pack()

    tk.Button(entry_window,
              text="生成预览", 
              command=visualize ).pack()

    entry_window.mainloop()
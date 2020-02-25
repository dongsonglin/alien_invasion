'''
烤地瓜——地瓜类——创建对象/实例
地瓜类——属性——方法
属性——时间——生熟——调料
方法——考地瓜（和生熟挂钩）
方法——添加调料
'''

class Sweet_potato():
    def __init__(self):
        self.time = 0
        self.condition = '生'
        self.condiment = []
    def inf(self):
        print(f'红薯烤了{self.time}分钟')
        print(f'土豆是{self.condition}的')
        print(f'红薯放了{self.condiment}这些调料')
    def cook(self,time):
        self.time = time
        if 0 <= time <=3:
            self.condition = '生'
        elif 3 < time <= 5:
            self.condition = '半生不熟'
        elif 5 < time <= 8:
            self.condition = '熟'
        elif time > 8:
            self.condition = '糊了'
        else: print('不能这么烤，笨蛋')
    def add_condiment(self,condiment):
        self.condiment.extend(condiment)









sweet_potato1 = Sweet_potato()
sweet_potato1.inf()
sweet_potato1.cook(8)
sweet_potato1.inf()
tl = ['sdf']
sweet_potato1.add_condiment(tl)
sweet_potato1.inf()
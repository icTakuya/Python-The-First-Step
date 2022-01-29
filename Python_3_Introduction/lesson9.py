class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class MazdaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', 
                enable_auto_run=False,):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, in_enable):
         self._enable_auto_run = in_enable

    def run(self):
       print('super fast')   
    def auto_run(self):
        print('auto_run')

tesla_car = TeslaCar('Model S')
# __のものを後から定義してしまうと実行できてしまう
tesla_car.__enable_auto_run = 'xxxxxx'
print(tesla_car.__enable_auto_run)



class T(object):
    pass

# 空のクラスを作成してインスタンス化したあとでも、定義が可能
t = T()
t.name = 'Yujin'
t.age = 25
print(t.name, t.age)
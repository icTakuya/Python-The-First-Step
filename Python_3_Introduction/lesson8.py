# クラスの継承
class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

# （）内にクラス名入れると継承
class MazdaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', 
                enable_auto_run=False,
                passwd='123'):
        super().__init__(model)
        # _を入れると書き換えたり外から見えないようにするという意味がある（実際にはできる）ゲッターとセッターを記述する
        # __の場合はクラス外からアクセスできない
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property # ゲッター
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, in_enable):
        if self.passwd == '456': #この条件にあっているときのみ変更可能にする
            self._enable_auto_run = in_enable
        else:
            raise ValueError

    def run(self):
       print('super fast')   
    def auto_run(self):
        print('auto_run')

tesla_car = TeslaCar('Model S', passwd='111')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
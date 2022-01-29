# 新たなクラス
class Person(object):
    def __init__(self, age=1):
        self.age = age
# ドライブメソッド
    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
# 1.rideメソッドを追加その中で引数でdriveメソッドを実行        
    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)

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
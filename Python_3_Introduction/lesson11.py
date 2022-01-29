# 抽象クラス Pythonではあまり使用しない
import abc

class Person(metaclass=abc.ABCMeta): # これは抽象クラスという記述
    def __init__(self, age=1):
        self.age = age
   
    #抽象メソッドの記述
    @abc.abstractmethod # このメソッドを実装してくださいという意味
    def drive(self):
       pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    # def drive(self):
    #     print('ok')

baby = Baby()
# baby.drive()
adult = Adult()
# adult.drive()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')        
    def ride(self, person):
        person.drive()

car = Car()


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
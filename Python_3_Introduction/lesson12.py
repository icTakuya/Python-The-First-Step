# 多重継承
class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

# 継承する際に左に記載したほうが優先される
# 開発途中で同じメソッドが発生しないほうが良いができてしまった場合はこの様な事が起きる
class PersonCarRobot(Person, Car): 
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run() #Personのrunメソッドが優先される
person_car_robot.fly()
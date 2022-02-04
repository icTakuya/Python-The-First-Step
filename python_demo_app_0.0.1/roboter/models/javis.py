from roboter.views import console

DEFAULT_ROBOT_NAME = 'JAVIS'

class Robot(object):
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        self.name = name
        self.user_name = user_name

    def hello(self):   
        template = console.get_template('hello.txt')
        user_name = input(template.substitute({
            'robot_name': self.name,
            }))
        
        self.user_name = user_name

class MovieRobot(Robot):
    def ask_movies(self):
        template = console.get_template('ask_movie.txt')
        movies = input(template.substitute({
            'user_name': self.user_name,
            }))

    def thank_you(self):
        template = console.get_template('thank_you.txt')
        print(template.substitute({
            'robot_name': self.name, 
            'user_name': self.user_name,
            }))

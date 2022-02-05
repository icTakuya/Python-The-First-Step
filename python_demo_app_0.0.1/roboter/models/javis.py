from roboter.views import console
from roboter.models import ranking

DEFAULT_ROBOT_NAME = 'JAVIS'

class Robot(object):
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='',spek_color='blue'):
        self.name = name
        self.user_name = user_name
        self.speak_color =spek_color

    def hello(self):   
        template = console.get_template('hello.txt', self.speak_color)
        user_name = input(template.substitute({
            'robot_name': self.name,
        }))
        self.user_name = user_name

class MovieRobot(Robot):
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        super().__init__(name, user_name)
        self.ranking_model = ranking.RankingModel()

    def ask_movies(self):
        while True:
            template = console.get_template(
                'ask_movie.txt', self.speak_color)
            movie = input(template.substitute({
                'user_name': self.user_name,
            }))
            if movie:
                self.ranking_model.add_movie(movie)
                break

    def thank_you(self):
        template = console.get_template('thank_you.txt', self.speak_color)
        print(template.substitute({
            'robot_name': self.name, 
            'user_name': self.user_name,
         }))
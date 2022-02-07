"""Definition of a robot named Jarvis."""
from roboter.views import console
from roboter.models import ranking


DEFAULT_ROBOT_NAME = 'JAVIS'


class Robot(object):
    """Base model for Robot."""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='',spek_color='magenta'):
        self.name = name
        self.user_name = user_name
        self.speak_color =spek_color

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning.""" 
        template = console.get_template('hello.txt', self.speak_color)
        user_name = input(template.substitute({
            'robot_name': self.name}))
        self.user_name = user_name


class MovieRobot(Robot):
    """Handling data for movie."""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name=''):
        super().__init__(name, user_name)
        self.ranking_model = ranking.RankingModel()

    def recommend_movie(self):
        """Introduce recommended movies to users."""
        new_recomend_movie = self.ranking_model.get_most_popular()
        if not new_recomend_movie:
            return None

        will_recomend_movie = [new_recomend_movie]
        while True:
            template = console.get_template(
                'recomend_movie.txt', self.speak_color)
            say_yes = input(template.substitute({
                'movie': new_recomend_movie,
            }))

            if say_yes.lower() == 'y' or say_yes.lower() == 'yes':
                break

            if say_yes.lower() == 'n' or say_yes.lower() == 'no':
                new_recomend_movie = self.ranking_model.get_most_popular(
                    not_list=will_recomend_movie)
                if not new_recomend_movie:
                    break
                will_recomend_movie.append(new_recomend_movie)

    def ask_movies(self):
        """Get recommended movie names from users."""
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
        """Say thank you to users."""
        template = console.get_template('thank_you.txt', self.speak_color)
        print(template.substitute({
            'robot_name': self.name, 
            'user_name': self.user_name,
         }))
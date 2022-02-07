"""A controller for the robot to talk"""
from roboter.models import javis


def questions_about_movies():
    """Function to talk to the robot"""
    question_robot = javis.MovieRobot()
    question_robot.hello()
    question_robot.recommend_movie()
    question_robot.ask_movies()
    question_robot.thank_you()

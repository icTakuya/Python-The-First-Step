from roboter.models import javis

def questions_about_movies():
    question_robot = javis.MovieRobot()
    question_robot.hello()
    question_robot.ask_movies()
    question_robot.thank_you()

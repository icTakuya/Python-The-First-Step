"""Console to get the template to return to the user."""
import os
import string

import termcolor


def get_template_dir_path():
    """Return the path of the template's directory.

    Returns:
        str: The template dir path.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir_path = os.path.join(base_dir, 'templates')
    return template_dir_path

def find_template(temp_file):
    """Find for template file in the given location.

    Returns:
        str: The template file path
    """
    template_dir_path = get_template_dir_path()
    temp_file_path = os.path.join(template_dir_path, temp_file)
    return temp_file_path

def get_template(template_file_path, color=None):
    """Return the path of the template.

    Color: Color formatting for output in terminal
            See in more details: https://pypi.python.org/pypi/termcolor

    Returns:
        string.Template: Return templates with characters in templates.
    """
    template = find_template(template_file_path)
    with open(template) as template_file:
        contents = template_file.read()
        contents = '{decoration}\n{contents}\n{decoration}\n'.format(
            contents=contents, decoration='=' * 60)
        contents = termcolor.colored(contents, color)
        return string.Template(contents)
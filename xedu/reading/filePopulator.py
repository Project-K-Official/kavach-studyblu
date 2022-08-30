from inspect import getsourcefile
from os.path import dirname
import pathlib
import requests
html = "https://www.freecodecamp.org/news/learning-python-from-zero-to-hero-120ea540b567/"
course = requests.get(html)
with open(pathlib.PurePath(dirname(getsourcefile(lambda: 0)), "course.html"), "w", encoding="utf-8") as f:
    f.write(course.text)

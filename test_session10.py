import polygon
from polygon_sequence import *
import pytest
import inspect
import os
import re

README_CONTENT_CHECK_FOR = [
    'interiorAngle',
    'edgeLength',
    'apothem',
    'area',
    'perimeter',
    'max efficiency polygon'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
    significant indenting."""
    lines = inspect.getsource(polygon)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_sides():
    obj = Polygon(3,4)
    assert obj.count_vertices == 3, " Vertices count incorrect"


def test_side_lessthan3():
    with pytest.raises(ValueError):
        Polygon(2, 10)


def test_equal():
    a = Polygon(5, 20)
    b = Polygon(5, 20)
    c = [2, 3, 4]

    assert a.__eq__(b) is True
    assert a.__eq__(c) is NotImplemented


def test_greaterthan():
    a = Polygon(5, 20)
    b = Polygon(8, 20)
    c = [2, 3, 4]

    assert a.__gt__(b) is False
    assert a.__gt__(c) is NotImplemented


def test_repr():
    a = Polygons(5, 20)
    b = Polygon(5,20)
    assert a.__repr__() == 'Polygons(m=5, R=20)'
    assert b.__repr__() == 'Polygon(n=5, R=20)'


def test_max_efficiency_polygon():
    polygons = Polygons(25, 15)
    assert polygons.max_efficiency_polygon.__repr__() == 'Polygon(n=25, R=15)'


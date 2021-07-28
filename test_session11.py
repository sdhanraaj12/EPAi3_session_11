import pytest
import math
import os
import inspect
import re
import polygon, customPolygon
from polygon import regular_polygon
from customPolygon import custom_polygon_iterable

README_CONTENT_CHECK_FOR = [
    'regular_polygon',
    'custom_polygon_iterable',
    '__init__',
    '__repr__',
    '__eq__',
    '__gt__',
    '__len__',
    '__getitem__',
    '__iter__',
    '__next__',
    'Class custom_polygon_iterator',
    'set_polygon_property',
    'num_of_sides',
    'circum_radius',
    'interior_angle',
    'edge_length',
    'apothem',
    'area',
    'perimeter',
    '_poly_ratio',
    'max_efficiency_polygon',
    'largest_num_of_sides',
    'circum_rad',
    'area_peri_ratios'
]

def test_session11_readme_exists():
    """
    Method checks if there is a README.md file. 
    failure_message: "README.md file missing!"  
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session11_readme_500_words():
    """
    Method checks if there are atleast 500 words in the README.md file
    failures_message: Make your README.md file interesting! Add atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session11_readme_proper_description():
    """
    Method checks if all the functions are described in the README.md file
    failures_message: You have not described all the functions/classes well in your README.md file
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_session11_readme_file_for_more_than_10_hashes():
    """
    Method checks if README.md file has atleast 10 '#' (indentations)
    failures_message: You have not described all the functions/classes well in your README.md file 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_polygon_indentations():
    """
    Method checks for proper indentations \
    Returns pass if used four spaces for each level of syntactically significant indenting.
    failures_message_1: Your script contains misplaced indentations
    failures_message_2: Your code indentation does not follow PEP8 guidelines
    """
    lines = inspect.getsource(polygon)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_customPolygon_indentations():
    """
    Method checks for proper indentations
    Returns pass if used four spaces for each level of syntactically significant indenting.
    failures_message_1: Your script contains misplaced indentations
    failures_message_2: Your code indentation does not follow PEP8 guidelines
    """
    lines = inspect.getsource(customPolygon)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_polygon_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in session11.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(polygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_customPolygon_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in session11.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(customPolygon, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
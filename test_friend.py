#test_age.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

import pytest
from datetime import date
from friend import *


### unit tests ###
def test_calculate_current_age():
    """ 
    GIVEN a user enters the year they were born
    WHEN that year is passed to this function
    THEN the user's age is accurately calculated
    """
    print("\r") # carriage return
    print(" -- calculate_current_age unit test")
    assert calculate_current_age(2000) == 23  # will change as the years progress
    

def test_calculate_future_age():
    """ 
    GIVEN a friend's current age
    WHEN that age is passed to this function
    THEN the user's age in 10 years is accurately calculated
    """
    current_age = 26
    expected_age = current_age + 10
    print("\r") # carriage return
    print(" -- calculate_future_age unit test")
    assert calculate_future_age(current_age) == expected_age



def test_add_friend():
    """ 
    GIVEN a friends's details
    WHEN those details are used to create a Python dictionary
    THEN that friend's dictionary is added to Python list of all friends
    """
    friend = {"name": "John Doe", "age": 30, "future": 40, "past": 20}
    add_friend(friend["name"].split()[0], friend["name"].split()[1], friend["age"], friend["future"], friend["past"])
    assert friend_list[-1] == friend

import pytest

from solver.main import *

def test_min_3_tasks():
    assert check_number_of_tasks([1,1]) == "Failed"

def test_integer_average_points(): 
    assert check_integer_average_points([1,1,1]) == "OK"
    assert check_integer_average_points([1,2,1]) == "Failed"
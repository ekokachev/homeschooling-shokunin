import pytest

from solver.main import *

def test_min_3_tasks():
    assert check_number_of_tasks([1,1]) == "Failed"

def test_integer_average_points(): 
    assert check_integer_average_points([1,1,1]) == "OK"
    assert check_integer_average_points([1,2,1]) == "Failed"

#def test_at_least_one_set_of_tasks_exists():
#    assert check_average_is_reachable([1,2,3,4,5,7,8]) == "OK"

def test_sort():
    assert sort_list_of_tasks([1,10,1]) == [1,1,10]

def test_convert_list_to_dict():
    assert convert_list_to_dict([3,10,20]) == {3: [{0}], 10: [{1}], 20: [{2}]}
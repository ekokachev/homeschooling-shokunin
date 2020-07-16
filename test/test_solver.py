import pytest

from solver.main import *

COMPLICATED_SET = [2,2,2,3,3,3,4,4,4,5,5,5,10,11,12]

def test_min_3_tasks():
    assert check_number_of_tasks([1,1]) == "Failed"

def test_integer_average_points(): 
    assert check_integer_average_points([1,1,1]) == "OK"
    assert check_integer_average_points([1,2,1]) == "Failed"

def test_average_is_reachable():
    p1 = convert_list_to_dict([9,9,12])
    p2 = convert_list_to_dict([9,10,11])
    p3 = convert_list_to_dict([1,2,3,4,5,7,8])
    assert check_average_is_reachable(p1, [9,9,12]) == "Failed"
    assert check_average_is_reachable(p2, [9,10,11]) == "OK"
    assert check_average_is_reachable(p3, [1,2,3,4,5,7,8]) == "OK"

def test_sort():
    assert sort_list_of_tasks([1,10,1]) == [1,1,10]

def test_convert_list_to_dict():
    assert convert_list_to_dict([3,10,20]) == {3: [{0}], 10: [{1}], 20: [{2}]}

def test_create_initial_paths():
    assert convert_list_of_tasks_to_paths([3,10,20]) == [{3: {0}}, {10: {1}}, {20: {2}}]

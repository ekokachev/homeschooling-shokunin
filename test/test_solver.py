import pytest

from solver.main import *

COMPLICATED_SET = [2,2,2,3,3,3,4,4,4,5,5,5,10,11,12]

def test_min_3_tasks():
    with pytest.raises(ValueError) as excinfo:
        assert Task_Assigner([1,1])
    assert "at least 3 tasks" in str(excinfo.value)               

def test_calculate_average_points(): 
    assert Task_Assigner([1,1,1]).average == 1
    
    with pytest.raises(ValueError) as excinfo:
        assert Task_Assigner( [1, 2, 1] )


def test_average_is_reachable():
    test_A = Task_Assigner([9,9,12])
    test_B = Task_Assigner([9,10,11])
    test_C = Task_Assigner([1,2,3,4,5,7,8])
    assert test_A.check_average_is_reachable() == "Failed"
    assert test_B.check_average_is_reachable() == "OK"
    assert test_C.check_average_is_reachable() == "OK"

def test_sort():
    test_A = Task_Assigner([1,10,1])
    assert test_A.list_of_tasks == [1,1,10]

def test_create_initial_paths():
    test_A = Task_Assigner([3,10,20])
    assert test_A.queue == [{3: {0}}, {10: {1}}, {20: {2}}]

import pytest

from solver.Task_Assigner import *

def test_min_3_tasks():
    with pytest.raises(ValueError) as excinfo:
        assert Task_Assigner([1,1])
    assert "at least 3 tasks" in str(excinfo.value)               

def test_calculate_average_points(): 
    assert Task_Assigner([1,1,1]).average == 1
    
    with pytest.raises(ValueError) as excinfo:
        assert Task_Assigner( [1, 2, 1] )


def test_is_average_reachable():
    test_A = Task_Assigner([9,9,12])
    test_B = Task_Assigner([9,10,11])
    test_C = Task_Assigner([1,2,3,4,5,7,8])

    test_A.generate_tasks_subsets()
    assert not test_A.is_average_reachable() 
    test_B.generate_tasks_subsets()
    assert test_B.is_average_reachable() 
    test_C.generate_tasks_subsets()
    assert test_C.is_average_reachable() 

def test_sort():
    test_A = Task_Assigner([1,10,1])
    assert test_A.list_of_tasks == [1,1,10]

def test_convert_list_of_tasks_to_queue():
    test_A = Task_Assigner([3,10,20])
    assert len(test_A.mapping) == len(test_A.list_of_tasks)
    assert len(test_A.queue) == len(test_A.list_of_tasks)

def check_assignments(assignments, average): 
    if sum(assignments[0]) == sum(assignments[1]) == sum(assignments[2]) == average:
        return True
    else:
        return False

def test_assign_tasks():
    test_1 = Task_Assigner([9,9,12])
    assert not test_1.assign_tasks()

    test_2 = Task_Assigner([9,10,11])
    assert not test_2.assign_tasks()
    
    test_3 = Task_Assigner([2,2,2,1,1,1])
    assert test_3.assign_tasks()
    assert check_assignments(test_3.assignments, test_3.average)

    test_4 = Task_Assigner([2,2,2,3,3,3,4,4,4,5,5,5,10,11,12])
    assert test_4.assign_tasks()
    assert check_assignments(test_4.assignments, test_4.average)

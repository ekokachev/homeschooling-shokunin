import pytest

from solver.main import check_number_of_tasks

def test_min_3_tasks():
    assert check_number_of_tasks([1,1]) == "Failed"

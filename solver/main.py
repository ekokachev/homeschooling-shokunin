
def check_number_of_tasks(list_of_tasks):
    if len(list_of_tasks) < 3:
        return "Failed"
    else:
        return "OK"


print(check_number_of_tasks([1,2,3]))
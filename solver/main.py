
def check_number_of_tasks(list_of_tasks):
    if len(list_of_tasks) < 3:
        return "Failed"
    else:
        return "OK"

def check_integer_average_points(list_of_tasks):
    if (sum(list_of_tasks) % len(list_of_tasks)) == 0:
        return "OK"
    else:
        return "Failed"

print(check_number_of_tasks([1,2,3]))
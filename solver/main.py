"""
Data Structure
dict = { 10: [{}, {}, {}, {}],
         20: [{}]
}

"""


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

def sort_list_of_tasks(list_of_tasks):
    list_of_tasks.sort()
    return list_of_tasks

def convert_list_to_dict(list_of_tasks):
    #Convert the list of tasks into appropriate data structure for the next step
    D = {}
    for i in range(len(list_of_tasks)):
        print(i, list_of_tasks[i])
        D[list_of_tasks[i]] = [set([i])]
    return D
    
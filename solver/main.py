"""
Data Structure
dict = { 10: [{}, {}, {}, {}],
         20: [{}]
}

paths = [{Sum of Points: set(list of tasks that give that value)}]


"""
import bisect

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
        #print(i, list_of_tasks[i])
        D[list_of_tasks[i]] = [set([i])]
    return D

def convert_list_of_tasks_to_paths(list_of_tasks):
    D = []
    for i in range(len(list_of_tasks)):
        D.append({list_of_tasks[i]: {i}})
    return D   


def check_average_is_reachable(D, list_of_tasks): 
    unique_elements = set(list_of_tasks)
    queue = list_of_tasks
    AVERAGE = sum(list_of_tasks) // 3 #floor (integer) division
    print(AVERAGE)
    while True: 
        next_in_line = queue.pop(0)
        if next_in_line >= AVERAGE:
            break

        for i in queue:
            new_element = next_in_line + i
            if new_element > AVERAGE:
                break
            if new_element not in unique_elements:
                bisect.insort(queue, new_element)
                unique_elements.add(new_element)         

    if AVERAGE in unique_elements: 
        return "OK"
    else:
        return "Failed"
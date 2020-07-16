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


def check_average_is_reachable(paths, list_of_tasks): 
    #unique_elements = set(list_of_tasks)
    queue = paths
    AVERAGE = sum(list_of_tasks) // 3 #floor (integer) division

    index_in_queue = -1
    while True: 
        index_in_queue += 1
        next_in_line = queue[index_in_queue]
        
        left_sum = next(iter(next_in_line)) # give the first key from a dict
        left_path = next_in_line[left_sum]

        if left_sum >= AVERAGE:
            break

        for i in queue[index_in_queue+1:]:
            right_sum = next(iter(i))
            right_path = i[right_sum]
            new_sum = left_sum + right_sum
            if new_sum > AVERAGE:
                break
            if not bool(left_path & right_path): 
                queue.append({new_sum: left_path.union(right_path)})


    if AVERAGE in queue[index_in_queue]:
        return "OK"
    else:
        return "Failed"
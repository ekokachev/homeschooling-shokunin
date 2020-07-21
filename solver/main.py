"""
Data Structure
dict = { 10: [{}, {}, {}, {}],
         20: [{}]
}

paths = [{Sum of Points: {subset of tasks that give that amount of points}}]
List of dicts was chosen as it allows to store this mapping. 
And data type set was chosen as dict value as tasks in the set are unique and sets make it easy to see if 2 of them have any common tasks. 
"""
#from bisect import bisect_left
import uuid

class Task_Assigner: 
    def __init__(self, list_of_tasks):
        super().__init__()
        self.list_of_tasks = list_of_tasks
        self.check_number_of_tasks()
        self.list_of_tasks.sort()
        self.queue_sorted_keys = self.list_of_tasks
        self.queue, self.mapping = self.convert_list_of_tasks_to_queue()

        self.average = self.calculate_average()

        self.index_in_queue = -1

    def calculate_average(self):
        if (sum(self.list_of_tasks) % 3) == 0:
            return sum(self.list_of_tasks) // 3
        else:
            raise ValueError("Average is not integer")

    def check_number_of_tasks(self):
        if len(self.list_of_tasks) < 3:
            raise ValueError("There should be at least 3 tasks")


    def convert_list_of_tasks_to_queue(self):
        queue = []
        mapping = {}
        for i in range(len(self.list_of_tasks)):
            unique_task_id = uuid.uuid4().fields[-1]
            queue.append({self.list_of_tasks[i]: {unique_task_id}})
            mapping[unique_task_id] = [i+1, self.list_of_tasks[i]]
        return queue, mapping


    def generate_tasks_subsets(self):
        for task_index in range(0, len(self.list_of_tasks)): 
            #self.index_in_queue += 1
            next_in_line = self.queue[task_index]
            
            left_sum = next(iter(next_in_line)) # give the first key from a dict
            left_path = next_in_line[left_sum]

#            if left_sum >= self.average:
#                break
            
            #frozen_queue = self.queue.copy()
            queue_length = len(self.queue)
            for i in self.queue[task_index + 1:queue_length]:
                right_sum = next(iter(i))
                right_path = i[right_sum]
                new_sum = left_sum + right_sum

                if (not bool(left_path & right_path)) and (new_sum <= self.average): 
#                    insert_index = bisect_left(self.queue_sorted_keys, new_sum)
#                    self.queue_sorted_keys.insert(insert_index, new_sum)
                    #self.queue.append({new_sum: left_path.union(right_path)})
                    self.queue.append({new_sum: left_path.union(right_path)})
                
    def check_average_is_reachable(self): 
        for item in self.queue:
            if self.average in item:
                return "OK"
        return "Failed"

    def convert_ids_to_weight(self, list_of_sets):
        r = []
        print(list_of_sets, '\n\n')
        for s in list_of_sets:
            new_s = [self.mapping[val][1] for val in s]
            r.append(new_s)
        print(self.mapping, '\n\n')
        print(r)
        return r

    def assign_tasks(self):
        self.generate_tasks_subsets()

        candidates = []
        for i in range(0, len(self.queue)):
            item = self.queue[i]
            if self.average in item:
                candidates.append(item[self.average])

        if len(candidates) < 3:
            return "Failed"
        else:
            for i in range(0, len(candidates)):
                for j in range(i+1, len(candidates)): 
                    for k in range(j+1, len(candidates)):
                        A_tasks = candidates[i]
                        B_tasks = candidates[j]
                        C_tasks = candidates[k]
                        if not ( bool(A_tasks & B_tasks) or bool(A_tasks & C_tasks) or bool(B_tasks & C_tasks)):
                            self.assignments = self.convert_ids_to_weight([A_tasks, B_tasks, C_tasks])
                            return "OK"
            return "Failed"

"""
Data Structure
dict = { 10: [{}, {}, {}, {}],
         20: [{}]
}

paths = [{Sum of Points: {subset of tasks that give that amount of points}}]
List of dicts was chosen as it allows to store this mapping. 
And data type set was chosen as dict value as tasks in the set are unique and sets make it easy to see if 2 of them have any common tasks. 
"""

class Task_Assigner: 
    def __init__(self, list_of_tasks):
        super().__init__()
        self.list_of_tasks = list_of_tasks
        self.check_number_of_tasks()
        self.list_of_tasks.sort()

        self.queue = self.convert_list_of_tasks_to_queue()

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
        for i in range(len(self.list_of_tasks)):
            queue.append({self.list_of_tasks[i]: {i}})
        return queue


    def generate_tasks_subsets(self):
        while True: 
            self.index_in_queue += 1
            next_in_line = self.queue[self.index_in_queue]
            
            left_sum = next(iter(next_in_line)) # give the first key from a dict
            left_path = next_in_line[left_sum]

            if left_sum >= self.average:
                break

            for i in self.queue[self.index_in_queue+1:]:
                right_sum = next(iter(i))
                right_path = i[right_sum]
                new_sum = left_sum + right_sum
                if new_sum > self.average:
                    break
                if not bool(left_path & right_path): 
                    self.queue.append({new_sum: left_path.union(right_path)})
                
    def check_average_is_reachable(self): 
        self.generate_tasks_subsets()
        if self.average in self.queue[self.index_in_queue]:
            return "OK"
        else:
            return "Failed"
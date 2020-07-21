import uuid

class Task_Assigner: 
    def __init__(self, list_of_tasks):
        super().__init__()
        self.list_of_tasks = list_of_tasks
        self.check_number_of_tasks()
        self.list_of_tasks.sort()
        self.queue, self.mapping = self.convert_list_of_tasks_to_queue()
        self.assignments = []
        self.average = self.calculate_average()

    def calculate_average(self):
        if (sum(self.list_of_tasks) % 3) == 0:
            return sum(self.list_of_tasks) // 3
        else:
            raise ValueError("Tasks cannot be equally distributed between the kids")

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
            next_in_line = self.queue[task_index]
            
            left_sum = next(iter(next_in_line)) # give the first key from a dict
            left_path = next_in_line[left_sum]

            queue_length = len(self.queue)
            for i in self.queue[task_index + 1:queue_length]:
                right_sum = next(iter(i))
                right_path = i[right_sum]
                new_sum = left_sum + right_sum

                if (not bool(left_path & right_path)) and (new_sum <= self.average): 
                    self.queue.append({new_sum: left_path.union(right_path)})
                
    def is_average_reachable(self): 
        for item in self.queue:
            if self.average in item:
                return True
        return False

    def convert_ids_to_weight(self, list_of_sets):
        r = []
        for s in list_of_sets:
            new_s = [self.mapping[val][1] for val in s]
            r.append(new_s)
        return r

    def assign_tasks(self):
        # TODO: refactor to treat "status codes" the same way
        self.generate_tasks_subsets()

        candidates = []
        for i in range(0, len(self.queue)):
            item = self.queue[i]
            if self.average in item:
                candidates.append(item[self.average])

        for i in range(0, len(candidates)):
            for j in range(i+1, len(candidates)): 
                for k in range(j+1, len(candidates)):
                    A_tasks = candidates[i]
                    B_tasks = candidates[j]
                    C_tasks = candidates[k]
                    if not ( bool(A_tasks & B_tasks) or bool(A_tasks & C_tasks) or bool(B_tasks & C_tasks)):
                        self.assignments = self.convert_ids_to_weight([A_tasks, B_tasks, C_tasks])
                        return True
        return False
    
    def get_printable_assignments(self):
        if self.assignments:
            assignments_str = f"Tasks are assigned as following: \n Livia: {self.assignments[0]} \n Julia: {self.assignments[1]} \n Agrippina: {self.assignments[2]}"
            return assignments_str
        else:
            return "Tasks couldn't be assigned"
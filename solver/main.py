import argparse
from solver.Task_Assigner import *

text = 'Enter a list of tasks in 1 line separated by space.'

parser = argparse.ArgumentParser(description=text)
parser.add_argument('tasks', metavar="N", type=int, nargs='+',
                    help='list of tasks')
args = parser.parse_args()

if args.tasks: 
    s = Task_Assigner(args.tasks)
    s.assign_tasks()
    print(s.get_printable_assignments())
    
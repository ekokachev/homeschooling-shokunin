# Shokunin Challenge
Assign tasks to 3 kids, so that: 
- each kid does the same number of points
- each task is assigned to a kid
- one task cannot be assigned to more than 1 kid

## Prerequisites
Clone this repo and navigate to the folder.

Create and activate a Python 3 Virtual Environment. 
```bash
$ virtualenv -p python3.7 virtual_environment
$ source virtual_environment/bin/activate
```
Install pytest
```bash
$ pip install -r requirements.txt 
```

## Running 
The script accepts the list of tasks as input. 

```bash
$ python solver/main.py [List of Tasks]
```
For example:
```bash
$ python solver/main.py 2 2 2 3 3 3 4 4 4 5 5 5 10 11 12
```

Sample output: 
```
Tasks are assigned as following:
 Livia: [2, 2, 3, 3, 12, 3]
 Julia: [11, 4, 2, 4, 4]
 Agrippina: [10, 5, 5, 5]
```

## Testing
```bash
$ pytest -v
```

## Evidence of TDD
In commit history. 
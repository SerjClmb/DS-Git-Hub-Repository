from collections import defaultdict
from collections import deque


def task_manager(tasks):
    task_dict = defaultdict(deque)

    for element in tasks:
        
        if element[2] is False:
            task_dict[element[1]].append(element[0])
        else:
            task_dict[element[1]].appendleft(element[0])
            
    return task_dict
        

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

print(task_manager(tasks))

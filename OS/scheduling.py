def fcfs_schedule(tasks):
    tasks.sort(key=lambda x: x[1])  # Sort by arrival time (priority)
    return [task[0] for task in tasks]

def sjf_schedule(tasks):
    tasks.sort(key=lambda x: x[2])  # Sort by burst time (CPU burst)
    return [task[0] for task in tasks]

def priority_schedule(tasks):
    tasks.sort(key=lambda x: x[1])  # Sort by priority
    return [task[0] for task in tasks]

def round_robin_schedule(tasks, time_quantum):
    schedule = []
    queue = tasks.copy()
    while queue:
        task = queue.pop(0)
        schedule.append(task[0])
        task[2] -= time_quantum
        if task[2] > 0:
            queue.append(task)
    return schedule

def priority_preemption_schedule(tasks):
    tasks.sort(key=lambda x: (x[1], x[2]))  # Sort by priority and burst time
    return [task[0] for task in tasks]

def srtf_schedule(tasks):
    time = 0
    schedule = []
    while tasks:
        eligible_tasks = [task for task in tasks if task[1] <= time]
        if eligible_tasks:
            shortest_task = min(eligible_tasks, key=lambda x: x[2])
            schedule.append(shortest_task[0])
            time += shortest_task[2]
            tasks.remove(shortest_task)
        else:
            time += 1
    return schedule

tasks = [["Task1", 3, 5], ["Task2", 1, 8], ["Task3", 2, 3]]
print("FCFS Schedule:", fcfs_schedule(tasks))
print("SJF Schedule:", sjf_schedule(tasks))
print("Priority Schedule:", priority_schedule(tasks))
print("Round Robin Schedule:", round_robin_schedule(tasks, 2))
print("Priority with Preemption Schedule:", priority_preemption_schedule(tasks))
print("SRTF Schedule:", srtf_schedule(tasks))

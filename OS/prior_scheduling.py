def priority_schedule_from_file(file_path):
    tasks = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split()
            process = parts[0]
            arrival_time = int(parts[1])
            burst_time = int(parts[2])
            priority = int(parts[3])
            tasks.append([process, arrival_time, burst_time, priority])

    tasks.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival time and priority (lowest priority first)

    return tasks

def calculate_metrics_priority(schedule):
    n = len(schedule)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    response_times = [0] * n

    remaining_time = [task[2] for task in schedule]

    time = 0
    executed_processes = []

    while executed_processes != schedule:
        eligible_tasks = [task for task in schedule if task[1] <= time and task not in executed_processes]
        if eligible_tasks:
            highest_priority_task = max(eligible_tasks, key=lambda x: -x[3])
            process_index = schedule.index(highest_priority_task)

            if remaining_time[process_index] == schedule[process_index][2]:
                response_times[process_index] = time

            remaining_time[process_index] -= 1
            time += 1

            if remaining_time[process_index] == 0:
                executed_processes.append(schedule[process_index])
                turnaround_times[process_index] = time - schedule[process_index][1]
                waiting_times[process_index] = turnaround_times[process_index] - schedule[process_index][2]

        else:
            time += 1

    average_waiting_time = sum(waiting_times) / n
    average_turnaround_time = sum(turnaround_times) / n
    average_response_time = sum(response_times) / n

    return waiting_times, turnaround_times, response_times, average_waiting_time, average_turnaround_time, average_response_time

# Example usage for Priority Scheduling:
file_path_priority = "prior_scheduling.txt"  # Replace with the actual path to your Priority input file
schedule_priority = priority_schedule_from_file(file_path_priority)
print("Priority Schedule from file:", [task[0] for task in schedule_priority])

waiting_times_priority, turnaround_times_priority, response_times_priority, avg_waiting_time_priority, avg_turnaround_time_priority, avg_response_time_priority = calculate_metrics_priority(schedule_priority)
print("\nMetrics for Priority Scheduling:")
for i in range(len(schedule_priority)):
    print(f"Process {schedule_priority[i][0]} - Waiting Time: {waiting_times_priority[i]}, Turnaround Time: {turnaround_times_priority[i]}, Response Time: {response_times_priority[i]}")

print(f"\nAverage Waiting Time: {avg_waiting_time_priority:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time_priority:.2f}")
print(f"Average Response Time: {avg_response_time_priority:.2f}")

def priority_round_robin_schedule_from_file(file_path, time_quantum):
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
            
    tasks.sort(key=lambda x: (x[1], -x[3]))  # Sort by arrival time and priority (higher priority first)

    return tasks, time_quantum

def calculate_metrics_priority_round_robin(schedule, time_quantum):
    n = len(schedule)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    response_times = [0] * n

    remaining_time = [task[2] for task in schedule]

    time = 0
    executed_processes = []

    while executed_processes != schedule:
        for i in range(n):
            if schedule[i] not in executed_processes:
                process_index = i

                if remaining_time[process_index] == schedule[process_index][2]:
                    response_times[process_index] = time

                if remaining_time[process_index] > time_quantum:
                    remaining_time[process_index] -= time_quantum
                    time += time_quantum
                else:
                    time += remaining_time[process_index]
                    remaining_time[process_index] = 0

                    executed_processes.append(schedule[process_index])
                    turnaround_times[process_index] = time - schedule[process_index][1]
                    waiting_times[process_index] = turnaround_times[process_index] - schedule[process_index][2]

    average_waiting_time = sum(waiting_times) / n
    average_turnaround_time = sum(turnaround_times) / n
    average_response_time = sum(response_times) / n

    return waiting_times, turnaround_times, response_times, average_waiting_time, average_turnaround_time, average_response_time

# Example usage for Priority Scheduling with Round Robin:
file_path_priority_rr = "prior_round_robin.txt"  # Replace with the actual path to your Priority with Round Robin input file
time_quantum_priority_rr = 2  # Replace with the desired time quantum
schedule_priority_rr, time_quantum_priority_rr = priority_round_robin_schedule_from_file(file_path_priority_rr, time_quantum_priority_rr)
print("Priority with Round Robin Schedule from file:", [task[0] for task in schedule_priority_rr])

waiting_times_priority_rr, turnaround_times_priority_rr, response_times_priority_rr, avg_waiting_time_priority_rr, avg_turnaround_time_priority_rr, avg_response_time_priority_rr = calculate_metrics_priority_round_robin(schedule_priority_rr, time_quantum_priority_rr)
print("\nMetrics for Priority Scheduling with Round Robin:")
for i in range(len(schedule_priority_rr)):
    print(f"Process {schedule_priority_rr[i][0]} - Waiting Time: {waiting_times_priority_rr[i]}, Turnaround Time: {turnaround_times_priority_rr[i]}, Response Time: {response_times_priority_rr[i]}")

print(f"\nAverage Waiting Time: {avg_waiting_time_priority_rr:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time_priority_rr:.2f}")
print(f"Average Response Time: {avg_response_time_priority_rr:.2f}")

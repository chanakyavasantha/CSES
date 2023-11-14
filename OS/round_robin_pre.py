def round_robin_schedule_from_file(file_path, time_quantum):
    tasks = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split()
            process = parts[0]
            arrival_time = int(parts[1])
            burst_time = int(parts[2])
            tasks.append([process, arrival_time, burst_time])

    tasks.sort(key=lambda x: x[1])  # Sort by arrival time

    return tasks, time_quantum

def calculate_metrics_round_robin(schedule, time_quantum):
    n = len(schedule)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    response_times = [0] * n

    remaining_time = [task[2] for task in schedule]

    time = 0
    executed_processes = []

    while any(remaining_time):
        for i in range(n):
            if remaining_time[i] > 0:
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

# Example usage for Round Robin:
file_path_rr = "round_robin_pre.txt"  # Replace with the actual path to your Round Robin input file
time_quantum_rr = 4  # Replace with the desired time quantum
schedule_rr, time_quantum_rr = round_robin_schedule_from_file(file_path_rr, time_quantum_rr)
print("Round Robin Schedule from file:", [task[0] for task in schedule_rr])

waiting_times_rr, turnaround_times_rr, response_times_rr, avg_waiting_time_rr, avg_turnaround_time_rr, avg_response_time_rr = calculate_metrics_round_robin(schedule_rr, time_quantum_rr)
print("\nMetrics for Round Robin:")
for i in range(len(schedule_rr)):
    print(f"Process {schedule_rr[i][0]} - Waiting Time: {waiting_times_rr[i]}, Turnaround Time: {turnaround_times_rr[i]}, Response Time: {response_times_rr[i]}")

print(f"\nAverage Waiting Time: {avg_waiting_time_rr:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time_rr:.2f}")
print(f"Average Response Time: {avg_response_time_rr:.2f}")

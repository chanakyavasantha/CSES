def fcfs_schedule_from_file(file_path):
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

    return tasks

def calculate_metrics(schedule):
    n = len(schedule)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    response_times = [0] * n

    waiting_times[0] = 0
    turnaround_times[0] = schedule[0][2]
    response_times[0] = waiting_times[0]

    for i in range(1, n):
        waiting_times[i] = turnaround_times[i - 1]
        turnaround_times[i] = waiting_times[i] + schedule[i][2]
        response_times[i] = waiting_times[i]

    average_waiting_time = sum(waiting_times) / n
    average_turnaround_time = sum(turnaround_times) / n
    average_response_time = sum(response_times) / n

    return waiting_times, turnaround_times, response_times, average_waiting_time, average_turnaround_time, average_response_time

# Example usage:
file_path = "fcfs.txt"  # Replace with the actual path to your input file
schedule = fcfs_schedule_from_file(file_path)
print("FCFS Schedule from file:", [task[0] for task in schedule])

waiting_times, turnaround_times, response_times, avg_waiting_time, avg_turnaround_time, avg_response_time = calculate_metrics(schedule)
print("\nMetrics:")
for i in range(len(schedule)):
    print(f"Process {schedule[i][0]} - Waiting Time: {waiting_times[i]}, Turnaround Time: {turnaround_times[i]}, Response Time: {response_times[i]}")

print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
print(f"Average Response Time: {avg_response_time:.2f}")

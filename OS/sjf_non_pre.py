def sjf_schedule_from_file(file_path):
    tasks = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split()
            process = parts[0]
            arrival_time = int(parts[1])
            burst_time = int(parts[2])
            tasks.append([process, arrival_time, burst_time])

    tasks.sort(key=lambda x: x[2])  # Sort by burst time (shortest job first)

    return tasks

def calculate_metrics_sjf(schedule):
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

# Example usage for SJF:
file_path_sjf = "sjf.txt"  # Replace with the actual path to your SJF input file
schedule_sjf = sjf_schedule_from_file(file_path_sjf)
print("SJF Schedule from file:", [task[0] for task in schedule_sjf])

waiting_times_sjf, turnaround_times_sjf, response_times_sjf, avg_waiting_time_sjf, avg_turnaround_time_sjf, avg_response_time_sjf = calculate_metrics_sjf(schedule_sjf)
print("\nMetrics for SJF:")
for i in range(len(schedule_sjf)):
    print(f"Process {schedule_sjf[i][0]} - Waiting Time: {waiting_times_sjf[i]}, Turnaround Time: {turnaround_times_sjf[i]}, Response Time: {response_times_sjf[i]}")

print(f"\nAverage Waiting Time: {avg_waiting_time_sjf:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time_sjf:.2f}")
print(f"Average Response Time: {avg_response_time_sjf:.2f}")

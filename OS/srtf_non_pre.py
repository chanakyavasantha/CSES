def srtf_schedule_from_file(file_path):
    tasks = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split()
            process = parts[0]
            arrival_time = int(parts[1])
            burst_time = int(parts[2])
            tasks.append({"process": process, "arrival_time": arrival_time, "burst_time": burst_time})

    tasks.sort(key=lambda x: (x["arrival_time"], x["burst_time"]))  # Sort by arrival time and burst time

    return tasks

def calculate_metrics_srtf(schedule):
    n = len(schedule)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    response_times = [0] * n

    time = 0
    executed_processes = []

    for i in range(n):
        process = schedule[i]
        response_times[i] = time

        time += process["burst_time"]
        executed_processes.append(process)

        turnaround_times[i] = time - process["arrival_time"]
        waiting_times[i] = turnaround_times[i] - process["burst_time"]

    average_waiting_time = sum(waiting_times) / n
    average_turnaround_time = sum(turnaround_times) / n
    average_response_time = sum(response_times) / n

    return waiting_times, turnaround_times, response_times, average_waiting_time, average_turnaround_time, average_response_time

# Example usage for SRTF (Non-Preemptive):
file_path_srtf = "srtf_non_pre.txt"  # Replace with the actual path to your SRTF input file
schedule_srtf = srtf_schedule_from_file(file_path_srtf)
print("SRTF Schedule (Non-Preemptive) from file:", [task["process"] for task in schedule_srtf])

waiting_times_srtf, turnaround_times_srtf, response_times_srtf, avg_waiting_time_srtf, avg_turnaround_time_srtf, avg_response_time_srtf = calculate_metrics_srtf(schedule_srtf)
print("\nMetrics for SRTF (Non-Preemptive):")
for i in range(len(schedule_srtf)):
    print(f"Process {schedule_srtf[i]['process']} - Waiting Time: {waiting_times_srtf[i]}, Turnaround Time: {turnaround_times_srtf[i]}, Response Time: {response_times_srtf[i]}")

print(f"\nAverage Waiting Time: {avg_waiting_time_srtf:.2f}")
print(f"Average Turnaround Time: {avg_turnaround_time_srtf:.2f}")
print(f"Average Response Time: {avg_response_time_srtf:.2f}")

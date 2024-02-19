class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort processes based on arrival time

    current_time = 0

    for process in processes:
        # If the process arrives after the current time, wait for it to arrive
        if process.arrival_time > current_time:
            current_time = process.arrival_time

        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

        current_time = process.completion_time

def display_results(processes):
    print("\nProcess:")

    total_turnaround_time = 0
    total_waiting_time = 0
    total_completion_time = 0  # Variable to store the sum of completion times

    gantt_chart = []  # List to store Gantt chart entries

    for process in processes:
        gantt_chart.append((process.process_id, process.completion_time))

        print(f"P{process.process_id}, AT: {process.arrival_time}, BT: {process.burst_time}, CT: {process.completion_time}, TAT: {process.turnaround_time}, WT: {process.waiting_time}")

        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time
        total_completion_time += process.completion_time  # Accumulate completion times

    # Calculate and display average turnaround time, average waiting time, and average completion time
    num_processes = len(processes)
    average_turnaround_time = total_turnaround_time / num_processes
    average_waiting_time = total_waiting_time / num_processes
    average_completion_time = total_completion_time / num_processes  # Calculate average completion time

    print(f"\nAverage TAT: {average_turnaround_time}")
    print(f"Average WT: {average_waiting_time}")
    print(f"Average CT: {average_completion_time}")  # Display the average completion time

    # Display Gantt chart
    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"| P{entry[0]} ", end="")
    print("|")

    for entry in gantt_chart:
        print(f"{entry[1]:2d} ", end="")
    print("\n")

if _name_ == "_main_":
    # Get the number of processes from the user
    num_processes = int(input("Enter the number of processes: "))

    # Create a list to store processes
    processes_list = []

    # Get arrival time and burst time for each process
    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter AT for P{i}: "))
        burst_time = int(input(f"Enter BT for P{i}: "))
        processes_list.append(Process(i, arrival_time, burst_time))

    # Run FCFS scheduling algorithm
    fcfs_scheduling(processes_list)

    # Display the results including the Gantt chart
    display_results(processes_list)

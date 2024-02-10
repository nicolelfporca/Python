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

    for process in processes:
        print(f"P{process.process_id}, AT: {process.arrival_time}, BT: {process.burst_time}, CT: {process.completion_time}, TAT: {process.turnaround_time}, WT: {process.waiting_time}")

if __name__ == "__main__":
    # Get the number of processes from the user
    num_processes = int(input("Enter the number of processes: "))

    # Create a list to store processes
    processes_list = []

    # Get arrival time and burst time for each process
    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter arrival time for Process {i}: "))
        burst_time = int(input(f"Enter burst time for Process {i}: "))
        processes_list.append(Process(i, arrival_time, burst_time))

    # Run FCFS scheduling algorithm
    fcfs_scheduling(processes_list)

    # Display the results
    display_results(processes_list)

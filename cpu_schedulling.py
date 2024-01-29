def menu():
    print("CPU Scheduling Algorithms")
    print("1. Round Robin with Quantum 3")
    print("2. Preemptive SJF")
    print("3. Non-Preemptive SJF")
    print("4. Preemptive Priority")
    print("5. Non-Preemptive Priority")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

processes = []

def input_processes():
    process_num = int(input("Enter the number of processes: "))
    for i in range(int(process_num)):
        process = []
        bt = int(input("Enter the burst time of P{}: ".format(i)))
        process.append(i)
        at = int(input("Enter the arrival time of P{}: ".format(i)))
        process.append(at)
        p = int(input("Enter the priority of P{}: ".format(i)))
        process.append(bt)
        print(process)
        processes.append(process)

    print(processes)

def round_robin():
    input_processes()
    quantum = 3
    processes.sort(key=lambda x: x[1])
    print(processes)
    time = 0
    while len(processes) > 0:
        if processes[0][2] > quantum:
            time += quantum
            processes[0][2] -= quantum
            processes.append(processes[0])
            processes.pop(0)
        else:
            time += processes[0][2]
            processes[0][2] = 0
            print("P{}: {}".format(processes[0][0], time))
            processes.pop(0)

def preemptive_sjf():
    # Assuming input_processes() populates the processes list
    input_processes()
    time = 0
    while processes:
        # Sort processes based on burst time (shortest burst time first)
        processes.sort(key=lambda x: x[0])
        # Pop the process with the shortest burst time
        current_process = processes.pop(0)
        # Print the process ID and the current time
        print("P{}: {}".format(current_process[0], time))
        # Update the time by adding the burst time of the current process
        time += current_process[2]

def non_preemptive_sjf():
    # Assuming input_processes() populates the processes list
    input_processes()
    # Sort processes based on burst time (shortest burst time first)
    processes.sort(key=lambda x: x[0])
    time = 0
    for process in processes:
        # Print the process ID and the current time
        print("P{}: {}".format(process[0], time))
        # Update the time by adding the burst time of the current process
        time += process[2]

def preemptive_priority():
    # Assuming input_processes() populates the processes list
    input_processes()
    time = 0
    while processes:
        # Sort processes based on priority (lowest priority first)
        processes.sort(key=lambda x: x[2])
        # Pop the process with the highest priority
        current_process = processes.pop(0)
        # Print the process ID and the current time
        print("P{}: {}".format(current_process[0], time))
        # Update the time by adding the burst time of the current process
        time += current_process[2]

def non_preemptive_priority():
    # Assuming input_processes() populates the processes list
    input_processes()
    # Sort processes based on priority (lowest priority first)
    processes.sort(key=lambda x: x[2])
    time = 0
    for process in processes:
        # Print the process ID and the current time
        print("P{}: {}".format(process[0], time))
        # Update the time by adding the burst time of the current process
        time += process[2]


def main():
    while True:
        choice = menu()
        if choice == 1:
            round_robin()
        elif choice == 2:
            preemptive_sjf()
        elif choice == 3:
            non_preemptive_sjf()
        elif choice == 4:
            preemptive_priority()
        elif choice == 5:
            non_preemptive_priority()
        elif choice == 6:
            exit()
        else:
            print("Invalid choice")

main()


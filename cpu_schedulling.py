# Initilisation ---------------------------------------------------------------------------------------------

processes = []  # Process format: [process_num, burst_time, arrival_time, priority]
pr_gantt, start_times, end_times = [], [], []  # Gantt chart data
pr, bt, at, ft, tat, wt = [], [], [], [], [], []  # Table data

def input_process(process_num, burst_time, arrival_time, priority):
    processes.append([process_num, burst_time, arrival_time, priority])
    print(processes)

def clone_processes():
    print(processes)  # Add this line to print the content of processes
    return [list(p) for p in processes]

# Gantt Chart and Table Visualisation Data ------------------------------------------------------------------
    
def ganttchartdata(process_id, start, end):
    pr_gantt.append(process_id)
    start_times.append(start)
    end_times.append(end)

def tabledata(process_num, burst_time, arrival_time, finish_time):
    pr.append(process_num)
    bt.append(burst_time)
    at.append(arrival_time)
    ft.append(finish_time)
    tat.append(finish_time - arrival_time)
    wt.append(finish_time - arrival_time - burst_time)

# CPU Scheduling Algorithms ---------------------------------------------------------------------------------

# Round Robin
def round_robin():
    quantum = 3
    time, finish_times = 0, {}
    ready_queue, local_processes, unfinished = [], clone_processes(), None
    local_processes.sort(key=lambda x: x[2])  # Sort by arrival time

    while local_processes or ready_queue:
        # Move processes from local_processes to ready_queue if their arrival time is <= current time
        while local_processes and local_processes[0][2] <= time:
            ready_queue.append(local_processes.pop(0))

        for p in ready_queue:
            if p[0] == unfinished:
                ready_queue.remove(p)
                ready_queue.append(p)
                unfinished = None
                break

        # If there are processes in the ready queue, execute them
        if ready_queue:
            process = ready_queue.pop(0)
            # Execute the process for either the quantum or its remaining burst time, whichever is smaller
            exec_time = min(quantum, process[1])
            # Update the Gantt chart or any other visualization
            ganttchartdata(process[0], time, time + exec_time)
            # Update the remaining burst time for the process
            process[1] -= exec_time
            # Update the current time
            time += exec_time
            # If the process still has remaining burst time, put it back in the ready queue
            if process[1] > 0:
                ready_queue.append(process)
                unfinished = process[0]
            # If the process has finished, record its finish time
            else:
                finish_times[process[0]] = time
        # If there are no processes in the ready queue, move to the next time unit
        else:
            time += 1

    for process in processes:
        tabledata(process[0], process[1], process[2], finish_times.get(process[0], time))

# Preemptive Shortest Job First (SJF)
def preemptive_sjf():
    time, finish_times = 0, {}
    ready_queue, local_processes = [], clone_processes()
    local_processes.sort(key=lambda x: x[2])  # Sort by arrival time

    while local_processes or ready_queue:
        while local_processes and local_processes[0][2] <= time:
            ready_queue.append(local_processes.pop(0))
            ready_queue.sort(key=lambda x: x[1])  # Sort by burst time
        if ready_queue:
            process = ready_queue[0]
            ganttchartdata(process[0], time, time + 1)
            process[1] -= 1
            time += 1
            if process[1] == 0:
                ready_queue.pop(0)
                finish_times[process[0]] = time
        else:
            time += 1

    for process in processes:
        tabledata(process[0], process[1], process[2], finish_times.get(process[0], time))

# Non-Preemptive Shortest Job First (SJF)
def non_preemptive_sjf():
    time, finish_times = 0, {}
    local_processes = sorted(clone_processes(), key=lambda x: (x[2], x[1]))  # Sort by arrival time, then burst time

    while local_processes:
        process = local_processes.pop(0)
        if time < process[2]:
            time = process[2]
        ganttchartdata(process[0], time, time + process[1])
        time += process[1]
        finish_times[process[0]] = time

    for process in processes:
        tabledata(process[0], process[1], process[2], finish_times.get(process[0], time))

# Non-Preemptive Priority Scheduling
def non_preemptive_priority():
    time, finish_times = 0, {}
    local_processes = sorted(clone_processes(), key=lambda x: (x[2], x[3], x[1]))  # Sort by arrival time, priority, burst time

    while local_processes:
        ready_queue = [process for process in local_processes if process[2] <= time]
        
        if ready_queue:
            process_to_execute = min(ready_queue, key=lambda x: (x[3], x[2]))  # Choose FCFS for same priority
            local_processes.remove(process_to_execute)

            if time < process_to_execute[2]:
                time = process_to_execute[2]

            ganttchartdata(process_to_execute[0], time, time + process_to_execute[1])
            time += process_to_execute[1]
            finish_times[process_to_execute[0]] = time
        else:
            # If no ready processes, just increment time
            time += 1

    for process in processes:
        tabledata(process[0], process[1], process[2], finish_times.get(process[0], time))

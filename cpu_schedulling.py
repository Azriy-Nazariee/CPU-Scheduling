# for the gantt chart generation
processes = []
pr=[]
arrival_time = []
burst_time = []
finish_time = []
done = False

def updates(process, time):
    pr.append(process[0])
    print(pr)
    arrival_time.append(process[3])
    print(arrival_time)
    burst_time.append(process[2])
    print(burst_time)
    finish_time.append(time)
    print(finish_time)

def input_process(process_num, burst_time, arrival_time, priority):
    process = []
    process.append(process_num)
    bt = int(burst_time)
    process.append(bt)
    at = int(arrival_time)
    process.append(at)
    p = int(priority)
    process.append(p)
    print(process)
    processes.append(process)
    print(processes)

def round_robin():
    quantum = 3
    processes.sort(key=lambda x: x[2])  # Sort by arrival time
    time = 0
    ready_queue = [process for process in processes]  # Create a ready queue

    while ready_queue:
        process = ready_queue.pop(0)
        if process[1] > quantum:
            time += quantum
            process[1] -= quantum
            ready_queue.append(process)
            updates(process, time)
        else:
            time += process[1]
            print(f"{process[0]}: {time}")
            updates(process, time)

def preemptive_sjf():
    time = 0
    while processes:
        processes.sort(key=lambda x: (x[2], x[3]))  # Sort by arrival time then by burst time
        current_process = processes.pop(0)
        print(f"P{current_process[0]}: {time}")
        time += current_process[2]
        updates(current_process, time)

def non_preemptive_sjf():
    processes.sort(key=lambda x: (x[2], x[3]))  # Sort by arrival time then by burst time
    time = 0
    for process in processes:
        print(f"P{process[0]}: {time}")
        time += process[2]
        updates(process, time)

def preemptive_priority():
    time = 0
    while processes:
        processes.sort(key=lambda x: (x[3], x[2]))  # Sort by priority then by arrival time
        current_process = processes.pop(0)
        print(f"P{current_process[0]}: {time}")
        time += current_process[2]
        updates(current_process, time)

def non_preemptive_priority():
    processes.sort(key=lambda x: (x[3], x[2]))  # Sort by priority then by arrival time
    time = 0
    for process in processes:
        print(f"P{process[0]}: {time}")
        time += process[2]
        updates(process, time)
import matplotlib.pyplot as plt
import numpy as np
from cpu_schedulling import processes, arrival_time, burst_time, finish_time

def create_table():
    # Calculate turnaround time and waiting time for each process
    turnaround_time = [f - a for f, a in zip(finish_time, arrival_time)]
    waiting_time = [t - b for t, b in zip(turnaround_time, burst_time)]

    # Calculate total and average turnaround time and waiting time
    total_turnaround_time = sum(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(turnaround_time)
    total_waiting_time = sum(waiting_time)
    average_waiting_time = total_waiting_time / len(waiting_time)

    # Create a data list from the process details
    data = list(zip(processes, arrival_time, burst_time, finish_time, turnaround_time, waiting_time))
    data.append(['Total', '', '', total_turnaround_time, total_waiting_time, ''])
    data.append(['Average', '', '', average_turnaround_time, average_waiting_time, ''])

    # Create a figure and a plot
    fig, ax = plt.subplots()

    # Hide the axes
    ax.axis('tight')
    ax.axis('off')

    # Create a table and add it to the plot
    table = ax.table(cellText=data, colLabels=['Process', 'Arrival Time', 'Burst Time', 'Finish Time', 'Turnaround Time', 'Waiting Time'], loc='center')

    plt.show()
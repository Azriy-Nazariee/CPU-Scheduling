import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
# Assuming cpu_schedulling.py is correctly implemented
from cpu_schedulling import input_process, preemptive_sjf, non_preemptive_sjf, preemptive_priority, non_preemptive_priority, round_robin, pr, processes, arrival_time, burst_time, finish_time

# Initialization of necessary variables
current_process = 0
process_count = 0
done = False

def window_properties(window):
    # Set the window size
    window_width = 250
    window_height = 300

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position to center the window
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Set the window size and position
    window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

def check_done_and_create_charts(algo):
    if algo == 'RR':
        round_robin()
    elif algo == 'P_SJF':
        preemptive_sjf()
    elif algo == 'NP_SJF':
        non_preemptive_sjf()
    elif algo == 'P_PRIO':
        preemptive_priority()
    elif algo == 'NP_PRIO':
        non_preemptive_priority()
    ganttchart()
    table()

def open_process_count_window(algo):
    global num_entry, inputnum

    window.withdraw()  # Assuming 'window' is your main application window

    inputnum = tk.Toplevel(window)
    window_properties(inputnum)
    num = tk.Label(inputnum, text="Enter the number of processes: ")
    num.pack()

    num_entry = ttk.Combobox(inputnum, values=list(range(3, 11)))
    num_entry.pack()

    submit_num = tk.Button(inputnum, text="Submit", command=lambda: open_details_window(inputnum, algo))
    submit_num.pack()

def open_details_window(previous_window, algo):
    global current_process, process_count, burst_entry, arrival_entry, priority_entry, inputprocess

    process_count = int(num_entry.get())
    current_process = 0  # Reset current_process for new input

    previous_window.destroy()

    inputprocess = tk.Toplevel()
    window_properties(inputprocess)
    inputprocess.title("Input Processes")

    enter_process_details()  # Call function to enter details for the first process

    submit = tk.Button(inputprocess, text="Start Simulation", command=lambda: finalize_input(algo))
    submit.pack()

def enter_process_details():
    global burst_entry, arrival_entry, priority_entry, inputprocess, current_process, process_label

    if current_process == 0:  # Only setup the widgets if it's the first process
        process_label = tk.Label(inputprocess, text=f"Process {current_process}")
        process_label.pack()

        tk.Label(inputprocess, text="Burst Time:").pack()
        burst_entry = tk.Entry(inputprocess)
        burst_entry.pack()

        tk.Label(inputprocess, text="Arrival Time:").pack()
        arrival_entry = tk.Entry(inputprocess)
        arrival_entry.pack()

        tk.Label(inputprocess, text="Priority:").pack()
        priority_entry = tk.Entry(inputprocess)
        priority_entry.pack()

        submit_process = tk.Button(inputprocess, text="Submit Process", command=enter_details)
        submit_process.pack()
    else:
        # Update the label for the next process
        update_process_label()

def update_process_label():
    global current_process, process_label
    process_label.config(text=f"Process {current_process}")  # Update label for next process
    burst_entry.delete(0, 'end')  # Clear the previous entry
    arrival_entry.delete(0, 'end')  # Clear the previous entry
    priority_entry.delete(0, 'end')  # Clear the previous entry

def enter_details():
    global current_process

    # Logic to input process and manage process details
    process_num = "P" + str(current_process)  # Process numbering starts at 1
    b_time = int(burst_entry.get())
    a_time = int(arrival_entry.get())
    p_value = int(priority_entry.get())

    input_process(process_num, b_time, a_time, p_value)  # Assuming this function exists to handle process data

    current_process += 1
    if current_process < process_count:
        update_process_label()  # Reuse the interface for the next process
    else:
        messagebox.showinfo("Information", "All processes have been entered. Proceeding to scheduling and charts. Please click 'Start Simulation' to start the simulation.")


def finalize_input(algo):
    inputprocess.destroy()  # Close input window after all processes are entered
    check_done_and_create_charts(algo)  # Now proceed to scheduling and chart creation

# Example setup function calls
def rr_setup():
    open_process_count_window('RR')

def p_sjf_setup():
    open_process_count_window('P_SJF')

def np_sjf_setup():
    open_process_count_window('NP_SJF')

def p_priority_setup():
    open_process_count_window('P_PRIO')

def np_priority_setup():
    open_process_count_window('NP_PRIO')

def ganttchart():
    # Prepare figure
    plt.figure(figsize=(10, 6))

    # Constant y-coordinate for all bars, representing a single line
    y_coordinate = 0.8  # Adjust this to move the entire line of bars up or down


    # Create a bar for each time a process is running
    for i, process in enumerate(processes):
        duration = finish_time[i] - arrival_time[i]
        plt.barh(y_coordinate, duration, left=arrival_time[i], height=0.4, color='skyblue', edgecolor='black')
        
        # Text for process name in the middle of the bar
        middle_point = arrival_time[i] + duration / 2
        plt.text(middle_point, y_coordinate, process[0], ha='center', va='center')
        
        # Text for end time at the end of each bar, placed below the bar
        plt.text(finish_time[i], y_coordinate - 0.205, str(finish_time[i]), ha='center', va='top', color='red')  # Adjust the y-coordinate offset as needed

    # Setting labels and title
    plt.xlabel('Time Units')
    plt.title('CPU Scheduling Gantt Chart')

    # Remove y-axis labels and ticks as they are not relevant in this context
    plt.yticks([])
    plt.ylabel('')

    # Optionally, add a line for clarity
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()  # Adjust the layout to make room for text

    # Show the plot
    plt.show()

def table():

    # Calculate turnaround time and waiting time for each process
    turnaround_time = [f - a for f, a in zip(finish_time, arrival_time)]
    waiting_time = [t - b for t, b in zip(turnaround_time, burst_time)]

    print(arrival_time)
    print(burst_time)
    print(finish_time)
    print(turnaround_time)
    print(waiting_time)

    # Calculate total and average turnaround time and waiting time
    total_turnaround_time = sum(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(turnaround_time)
    total_waiting_time = sum(waiting_time)
    average_waiting_time = total_waiting_time / len(waiting_time)

    # Create a data list from the process details
    data = list(zip(pr, arrival_time, burst_time, finish_time, turnaround_time, waiting_time))
    data.append(['Total', '', '', '', total_turnaround_time, total_waiting_time])
    data.append(['Average', '', '', '', average_turnaround_time, average_waiting_time])

    # Create a figure and a plot
    fig, ax = plt.subplots()

    # Hide the axes
    ax.axis('tight')
    ax.axis('off')

    # Create a table and add it to the plot
    table = ax.table(cellText=data, colLabels=['Process', 'Arrival Time', 'Burst Time', 'Finish Time', 'Turnaround Time', 'Waiting Time'], loc='center')

    table.auto_set_font_size(False)
    table.set_fontsize(10)  # Adjust font size as needed
    table.scale(1, 1)  # Scale table size for better visibility

    plt.show()

# Main Menu 

# Create the tkinter window
window = tk.Tk()

window_properties(window)

# Set the window title
window.title("CPU Scheduling Algorithms")

label = tk.Label(window, text="Welcome To CPU Scheduling Algorithms")
label.pack(anchor='center', expand=True)

buttonframe = tk.Frame(window)

button_width = 40
button_height = 2

rr = tk.Button(buttonframe, text="Round Robin with Quantum 3", width=button_width, height=button_height, command=rr_setup)
rr.pack()

p_sjf = tk.Button(buttonframe, text="Preemptive SJF", width=button_width, height=button_height, command=p_sjf_setup)
p_sjf.pack()

np_sjf = tk.Button(buttonframe, text="Non-Preemptive SJF", width=button_width, height=button_height, command=np_sjf_setup)
np_sjf.pack()

p_priority = tk.Button(buttonframe, text="Preemptive Priority", width=button_width, height=button_height, command=p_priority_setup)
p_priority.pack()

np_priority = tk.Button(buttonframe, text="Non-Preemptive Priority", width=button_width, height=button_height, command=np_priority_setup)
np_priority.pack()

buttonframe.pack()

window.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from cpu_schedulling import input_process, preemptive_sjf, non_preemptive_sjf, preemptive_priority, non_preemptive_priority, round_robin, processes, arrival_time, burst_time, finish_time

current_process = 0
process_count = 0
type = ""
done = False

def check_done_and_create_charts():
    global done
    print(done)
    if done:
        create_gantt_chart()
        create_table()

# Function to open the window for entering the number of processes
def open_process_count_window():
    global num_entry, inputnum  # Declare inputnum as a global variable

    window.withdraw()

    inputnum = tk.Toplevel(window)
    inputnum.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    num = tk.Label(inputnum, text="Enter the number of processes: ")
    num.pack()
    
    # Create a combobox with values from 3 to 10
    num_entry = ttk.Combobox(inputnum, values=list(range(3, 11)))
    num_entry.pack()

    submit_num = tk.Button(inputnum, text="Submit", command=lambda: open_details_window(inputnum))
    submit_num.pack()
    return inputnum

def open_details_window(previous_window):
    global current_process, process_count, burst, arrival, priority, burst_entry, arrival_entry, priority_entry, inputprocess

    process_count = int(num_entry.get())  # Get the number of processes

    previous_window.destroy()  # Close the previous window

    # Input Processes' Details Window
    inputprocess = tk.Toplevel()
    input_frame = tk.Frame(inputprocess)
    inputprocess.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    inputprocess.title("Input Processes")

    # Dynamic labels and entries for process details
    burst = tk.Label(input_frame, text=f"Enter the burst time of P{current_process}: ")
    burst.pack()
    burst_entry = tk.Entry(input_frame)
    burst_entry.pack()

    arrival = tk.Label(input_frame, text=f"Enter the arrival time of P{current_process}: ")
    arrival.pack()
    arrival_entry = tk.Entry(input_frame)
    arrival_entry.pack()

    priority = tk.Label(input_frame, text=f"Enter the priority of P{current_process}: ")
    priority.pack()
    priority_entry = tk.Entry(input_frame)
    priority_entry.pack()

    input_frame.pack()

    submit = tk.Button(input_frame, text="Submit", command=enter_details)
    submit.pack()

# Input Processes' Details Window

def enter_details():
    global current_process, done

    # Ensure that the current process number does not exceed the total number of processes
    if current_process < process_count:
        try:
            # Get the values from the Entry widgets and convert them to integers
            process_num = "P"+str(current_process)
            burst_time = int(burst_entry.get())
            arrival_time = int(arrival_entry.get())
            priority_value = int(priority_entry.get())

            print(current_process)
            print(process_count)

            if current_process < process_count:

                # Call your function to process these values (assuming input_process function exists)
                input_process(process_num, burst_time, arrival_time, priority_value)

                # Clear the Entry widgets for the next input
                burst_entry.delete(0, 'end')
                arrival_entry.delete(0, 'end')
                priority_entry.delete(0, 'end')

                # Increment the current process number and update labels for the next process
                current_process += 1
                if current_process != process_count:
                    burst.config(text=f"Enter the burst time of P{current_process}: ")
                    arrival.config(text=f"Enter the arrival time of P{current_process}: ")
                    priority.config(text=f"Enter the priority of P{current_process}: ")
                else:
                    done = True
                    print("All process details entered")  # Placeholder for further action
                    messagebox.showinfo("Information", "All processes have already been entered")
                    inputprocess.destroy()  # Optionally close the input process window

                    # Call the function that generates the table and graph
                    check_done_and_create_charts()

        except ValueError:
            # Handle cases where the input is not a valid integer
            print("Please enter valid integer values for burst time, arrival time, and priority")
    else:
        # This part of the code should not be reachable due to the checks, but it's good practice to handle it
        print("All processes have already been entered")

def rr_setup():
    open_process_count_window()
    round_robin()
    check_done_and_create_charts()

def p_sjf_setup():
    open_process_count_window()
    preemptive_sjf()
    check_done_and_create_charts()

def np_sjf_setup():
    open_process_count_window()
    non_preemptive_sjf()
    check_done_and_create_charts()

def p_priority_setup():
    open_process_count_window()
    preemptive_priority()
    check_done_and_create_charts()

def np_priority_setup():
    open_process_count_window()
    non_preemptive_priority()
    check_done_and_create_charts()

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

def create_gantt_chart():
    # Prepare figure
    plt.figure(figsize=(10, 6))

    # Constant y-coordinate for all bars, representing a single line
    y_coordinate = [1] * len(processes)  # Same y-value for all processes

    # Create a bar for each time a process is running
    for i, process in enumerate(processes):
        plt.barh(y_coordinate, finish_time[i] - arrival_time[i], left=arrival_time[i], height=0.4, color='skyblue', edgecolor='black')

        # Optionally, add text labels
        middle_point = arrival_time[i] + (finish_time[i] - arrival_time[i]) / 2
        plt.text(middle_point, y_coordinate[i], process, ha='center', va='center')

    # Setting labels and title
    plt.xlabel('Time Units')
    plt.title('CPU Scheduling Gantt Chart')

    # Remove y-axis labels and ticks as they are not relevant in this context
    plt.yticks([])
    plt.ylabel('')

    # Show the plot
    plt.show()

# Main Menu 

# Create the tkinter window
window = tk.Tk()

# Set the window title
window.title("CPU Scheduling Algorithms")

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
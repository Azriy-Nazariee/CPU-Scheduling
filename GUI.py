import tkinter as tk
from cpu_schedulling import round_robin, preemptive_sjf, non_preemptive_sjf, preemptive_priority, non_preemptive_priority, input_process

current_process = 0

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

# Main Menu

rr = tk.Button(buttonframe, text="Round Robin with Quantum 3", width=button_width, height=button_height)
rr.pack()

p_sjf = tk.Button(buttonframe, text="Preemptive SJF", width=button_width, height=button_height)
p_sjf.pack()

np_sjf = tk.Button(buttonframe, text="Non-Preemptive SJF", width=button_width, height=button_height)
np_sjf.pack()

p_priority = tk.Button(buttonframe, text="Preemptive Priority", width=button_width, height=button_height)
p_priority.pack()

np_priority = tk.Button(buttonframe, text="Non-Preemptive Priority", width=button_width, height=button_height)
np_priority.pack()

exit_button = tk.Button(buttonframe, text="Exit", width=button_width, height=button_height)
exit_button.pack()

buttonframe.pack(anchor='center', expand=True)

# Input Processes Window

inputnum= tk.Toplevel()
inputnum.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
num = tk.Label(inputnum, text="Enter the number of processes: ")
num_entry = tk.Entry(inputnum)
num.pack()

inputprocess= tk.Toplevel()
input_frame= tk.Frame(inputprocess)
inputprocess.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
inputprocess.title("Input Processes")

num_entry.pack()
burst = tk.Label(input_frame, text="Enter the burst time of P{}: ")
burst.pack()
burst_entry = tk.Entry(input_frame)
burst_entry.pack()
arrival = tk.Label(input_frame, text="Enter the arrival time of P{}: ")
arrival.pack()
arrival_entry = tk.Entry(input_frame)
arrival_entry.pack()
priority = tk.Label(input_frame, text="Enter the priority of P{}: ")
priority.pack()
priority_entry = tk.Entry(input_frame)
priority_entry.pack()

input_frame.pack()

def enter_details():
    global current_process

    # Get the values from the Entry widgets
    burst_time = int(burst_entry.get())
    arrival_time = int(arrival_entry.get())
    priority = int(priority_entry.get())

    # Call your function to process these values
    input_process(burst_time, arrival_time, priority)

    # Clear the Entry widgets
    burst_entry.delete(0, 'end')
    arrival_entry.delete(0, 'end')
    priority_entry.delete(0, 'end')

    # Increment the current process number
    current_process += 1

    # Update the labels for the next process
    burst.config(text=f"Enter the burst time of P{current_process}: ")
    arrival.config(text=f"Enter the arrival time of P{current_process}: ")
    priority.config(text=f"Enter the priority of P{current_process}: ")

submit = tk.Button(input_frame, text="Submit", command=enter_details)
submit.pack()

# Run the tkinter main loop
window.mainloop()
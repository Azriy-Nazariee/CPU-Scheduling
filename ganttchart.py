import matplotlib.pyplot as plt

# Sample data: Process IDs and their start and end times
processes = ['P0', 'P1', 'P2', 'P3', 'P4', 'P5']
start_times = [3, 3, 1, 1, 5, 6]
end_times = [0, 1, 6, 12, 19, 27]  # Assuming continuous execution for simplicity

# Prepare figure
plt.figure(figsize=(10, 6))

# Constant y-coordinate for all bars, representing a single line
y_coordinate = 0.8  # Adjust this to move the entire line of bars up or down

# Create a bar for each time a process is running
for i, process in enumerate(processes):
    duration = end_times[i] - start_times[i]
    plt.barh(y_coordinate, duration, left=start_times[i], height=0.4, color='skyblue', edgecolor='black')
    
    # Text for process name in the middle of the bar
    middle_point = start_times[i] + duration / 2
    plt.text(middle_point, y_coordinate, process, ha='center', va='center')
    
    # Text for end time at the end of each bar, placed below the bar
    plt.text(end_times[i], y_coordinate - 0.205, str(end_times[i]), ha='center', va='top', color='red')  # Adjust the y-coordinate offset as needed

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

import matplotlib.pyplot as plt

# Sample data: Process IDs and their start and end times
processes = ['P1', 'P2', 'P1', 'P3']
start_times = [0, 2, 4, 7]
end_times = [2, 4, 7, 9]

def create_gantt_chart():
    # Prepare figure
    plt.figure(figsize=(10, 6))

    # Constant y-coordinate for all bars, representing a single line
    y_coordinate = [1] * len(processes)  # Same y-value for all processes

    # Create a bar for each time a process is running
    for i, process in enumerate(processes):
        plt.barh(y_coordinate, end_times[i] - start_times[i], left=start_times[i], height=0.4, color='skyblue', edgecolor='black')

        # Optionally, add text labels
        middle_point = start_times[i] + (end_times[i] - start_times[i]) / 2
        plt.text(middle_point, y_coordinate[i], process, ha='center', va='center')

    # Setting labels and title
    plt.xlabel('Time Units')
    plt.title('CPU Scheduling Gantt Chart')

    # Remove y-axis labels and ticks as they are not relevant in this context
    plt.yticks([])
    plt.ylabel('')

    # Show the plot
    plt.show()

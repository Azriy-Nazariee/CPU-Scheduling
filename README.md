# CPU Scheduling Simulator

A comprehensive CPU Scheduling Simulator built with Python, leveraging Tkinter for the GUI and Matplotlib for generating Gantt charts and detailed tables. This simulator provides an interactive way to understand how different CPU scheduling algorithms work, including Round Robin, Preemptive Shortest Job First (SJF), Non-Preemptive SJF, and Non-Preemptive Priority scheduling.

## Features

- **Interactive GUI**: Utilizes Tkinter for an easy-to-navigate graphical user interface, allowing users to input process details such as burst time, arrival time, and priority.
- **Multiple Scheduling Algorithms**: Supports Round Robin, Preemptive SJF, Non-Preemptive SJF, and Non-Preemptive Priority scheduling algorithms.
- **Visualization**: Generates Gantt charts and detailed tables for each scheduling algorithm using Matplotlib, providing visual insights into the scheduling process and its outcome.
- **Dynamic Input**: Users can specify the number of processes and input specific details for each, including burst time, arrival time, and priority.
- **Customizable**: Easy to adapt and extend with more scheduling algorithms or enhanced features.

## Installation

Ensure you have Python installed on your system. This project requires Python 3.x.

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/cpu-scheduling-simulator.git
```
2. Navigate into the project directory:
   
```
cd cpu-scheduling-simulator
```

3. Install the required dependencies:
   
```
pip install matplotlib tk
```

## Usage

To run the simulator, execute the following command in the terminal:

```
python main.py
```

Upon launch, the GUI will guide you through the following steps:

1. **Select a Scheduling Algorithm**: Choose one of the available CPU scheduling algorithms from the main menu.
2. **Input Process Details**: Enter the number of processes and specify their burst time, arrival time, and priority.
3. **Simulation and Visualization**: After inputting the process details, the simulator will compute the scheduling based on the selected algorithm and display the Gantt chart and a detailed table showing the finish time, turnaround time, and waiting time for each process.

## Contributing

Contributions to enhance the CPU Scheduling Simulator are welcome. This can include adding new scheduling algorithms, improving the UI, or fixing bugs. Please feel free to fork the repository and submit a pull request with your improvements.

---

For more details on how to use the simulator or to report issues, please refer to the project's GitHub repository.

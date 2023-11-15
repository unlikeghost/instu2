import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuring the serial port (adjust the port and baud rate as needed)
arduino_port = "COM3"  # Change the COM port as needed
arduino_baud = 9600

ser = serial.Serial(arduino_port, arduino_baud)

x_data = []
y_data = []

# Create a function to update the plot in real-time
def update_plot(i):
    try:
        line_data = ser.readline().decode().strip()
        value = float(line_data)
        
        x_data.append(len(x_data))  # Use a simple counter as the x-axis data
        y_data.append(value)
        
        # Limit the number of data points to display
        max_display_points = 500
        if len(x_data) > max_display_points:
            x_data.pop(0)
            y_data.pop(0)
        
        ax.clear()
        ax.plot(x_data, y_data)
        ax.set_xlabel("Data Point")
        ax.set_ylabel("Value")
        ax.set_title("Real-Time Data Plot")

    except Exception as e:
        print("Error:", e)

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()

# Create an animation that calls the update_plot function every 100 milliseconds
ani = FuncAnimation(fig, update_plot, interval=10)

# Show the plot
plt.show()

# Close the serial port when the plot window is closed
def on_closing():
    ser.close()

plt.gca().figure.canvas.mpl_connect('close_event', on_closing)

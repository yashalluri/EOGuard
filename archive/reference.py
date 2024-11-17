import plotly.graph_objects as go
from IPython.display import display, clear_output
import random
import time

# Initialize figure
fig = go.Figure()

# Add initial traces
fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', name='Line 1'))
fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', name='Line 2'))

# Set layout
fig.update_layout(
    title="Live Scrolling Graph Example",
    xaxis=dict(title="Time", range=[0, 100]),
    yaxis=dict(title="Value", range=[0, 600]),
    template="plotly_dark"
)

# Data storage
x_data = []
y_data1 = []
y_data2 = []
colors1 = []  # Colors for Line 1
colors2 = []  # Colors for Line 2
current_x = 0

# Update graph function
def update_graph():
    global current_x, x_data, y_data1, y_data2, colors1, colors2

    # Generate new data points (replace with real streaming data sources)
    new_y1 = random.randint(0, 300)  # Example data for Line 1
    new_y2 = random.randint(300, 600)  # Example data for Line 2
    current_x += 1
    x_data.append(current_x)
    y_data1.append(new_y1)
    y_data2.append(new_y2)

    # Conditional highlighting: Red if new_y1 > 250 or new_y2 > 550, else Blue
    colors1.append('red' if new_y1 > 250 else 'blue')
    colors2.append('red' if new_y2 > 550 else 'green')

    # Adjust x-axis range for scrolling
    x_range = [current_x - 100 if current_x > 100 else 0, current_x]

    # Update figure data
    fig.data[0].x = x_data
    fig.data[0].y = y_data1
    fig.data[0].marker = dict(color=colors1)  # Line 1 conditional colors

    fig.data[1].x = x_data
    fig.data[1].y = y_data2
    fig.data[1].marker = dict(color=colors2)  # Line 2 conditional colors

    fig.update_layout(xaxis=dict(range=x_range))

# Live update loop
while True:  # Run indefinitely
    update_graph()
    clear_output(wait=True)  # Clear previous output in Jupyter Notebook
    display(fig)  # Redisplay the updated figure
    time.sleep(0.5)  # Adjust refresh rate
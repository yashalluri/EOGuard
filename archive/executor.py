import logging
from graphy_bois import GraphyClass
from IPython.display import display
import time

# Suppress logs from cmdstanpy
logging.getLogger("cmdstanpy").setLevel(logging.WARNING)

def graph_generator(file_path):
    generator = GraphyClass(file_path)
    generator.create_graph()

    display(generator.fig)  # Display the initial FigureWidget

    while True:
        generator.update_graph()
        time.sleep(0)  # Adjust refresh rate


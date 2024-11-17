import os
import pandas as pd

# Initialize an empty dictionary to store DataFrames
data_frames = {}

# Path to the data folder
data_folder = "./data"

# Iterate over files in the folder
for file_name in os.listdir(data_folder):
    file_path = os.path.join(data_folder, file_name)
    
    # Ensure it's a CSV file
    if file_name.endswith('.csv') and os.path.isfile(file_path):
        # Extract file name without extension
        key = os.path.splitext(file_name)[0]
        
        # Load the CSV into a DataFrame and store it in the dictionary
        data_frames[key] = pd.read_csv(file_path)

# Dictionary with DataFrames stored under keys as file names
print(data_frames)
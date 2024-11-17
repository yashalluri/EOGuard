import pandas as pd
import numpy as np
from pathlib import Path
from prophet import Prophet
import plotly.io as pio
pio.renderers.default = 'notebook'

import plotly.express as px
import pandas as pd
import numpy as np
import plotly.io as pio

# Ensure Plotly renders in Jupyter Notebook
pio.renderers.default = 'notebook'
import warnings
warnings.filterwarnings("ignore")
import warnings
warnings.filterwarnings("ignore")


import logging

# Suppress logging for cmdstanpy
logging.getLogger("cmdstanpy").setLevel(logging.WARNING)

def stream_data(ticker, pipes):
    results_df = {}
    for key, value in pipes.items():
            
        if ticker>len(value):
            temp_df = value.copy()
        else:
            temp_df = value.iloc[:ticker+1].copy()
        
        #Anamoly Detection
        temp_df['ds'] = value["Time"]
        temp_df['y'] = value["Inj Gas Meter Volume Instantaneous"]
        
        if ticker < 3:
            results_df[key] = {
                "actual": temp_df['y'].iloc[ticker%len(value)], 
                "predicted": temp_df['y'].iloc[ticker%len(value)],
                "anamoly": False
            }
            return results_df

        # Fit a Prophet model
        model = Prophet()
        model.fit(temp_df[['ds', 'y']])

        # Make predictions
        future = model.make_future_dataframe(periods=0)  # Predict only on existing data
        forecast = model.predict(future)

        # Merge predictions back into the original DataFrame
        temp_df['yhat'] = forecast['yhat']
        temp_df['deviation'] = abs(temp_df['y'] - temp_df['yhat'])
        threshold = temp_df['deviation'].quantile(0.995)  # Set a threshold at the 95th percentile
        temp_df['anomaly'] = (temp_df['deviation'] > threshold) & ((temp_df['y'] - temp_df['yhat']) < 0)

        results_df[key] = {
            "actual": temp_df['y'].iloc[ticker%len(value)], 
            "predicted": temp_df['yhat'].iloc[ticker%len(value)],
            "anamoly": temp_df['anomaly'].iloc[ticker%len(value)]
        }

    return results_df    
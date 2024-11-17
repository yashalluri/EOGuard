import pandas as pd
import numpy as np
from pathlib import Path
from prophet import Prophet
import warnings
import logging
import plotly.graph_objects as go
from IPython.display import display, clear_output
import random
import time
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



# Suppress logging for cmdstanpy
logging.getLogger("cmdstanpy").setLevel(logging.WARNING)
warnings.filterwarnings("ignore")

#data_path = Path("/Users/harsha_gurram/repos/HackUTD-RippleEffect/data")
#pipe_df = pd.read_csv(data_path/Path("Bold_744H-10_31-11_07.csv"))
"""
class GraphyClass():
    def __init__(self,path):
        self.pipe_df = pd.read_csv(path)
        self.ticker = 0
        self.fig = go.Figure()
        self.x_data = []
        self.y_data1 = []
        self.y_data2 = []
        self.colors1 = []  # Colors for Line 1
        self.colors2 = []  # Colors for Line 2
        self.current_x = 0  # Current x-axis value
    
    def stream_data(self, ticker):
        if ticker>len(self.pipe_df):
            temp_df = self.pipe_df.copy()
        else:
            temp_df = self.pipe_df.iloc[:ticker+1].copy()

        #Anamoly Detection
        temp_df['ds'] = temp_df["Time"]
        temp_df['ds'] = pd.to_datetime(temp_df['Time'])
        temp_df['y'] = temp_df["Inj Gas Meter Volume Instantaneous"]

        if ticker < 3:
            results = {
                "actual": temp_df['y'].iloc[ticker%len(self.pipe_df)], 
                "predicted": temp_df['y'].iloc[ticker%len(self.pipe_df)],
                "anamoly": False
            }

            return results

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

        results = {
            "actual": temp_df['y'].iloc[ticker%len(self.pipe_df)], 
            "predicted": temp_df['yhat'].iloc[ticker%len(self.pipe_df)],
            "anamoly": temp_df['anomaly'].iloc[ticker%len(self.pipe_df)]
        }

        return results
    
    def create_graph(self):

        self.fig = go.Figure()

        self.fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', name='Flow Rate'))
        self.fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', name='Predicted Flow Rate'))

        # Set layout
        self.fig.update_layout(
            xaxis=dict(title="Time", range=[0,100]),
            yaxis=dict(title="Value", range=[0, self.pipe_df["Inj Gas Meter Volume Instantaneous"].max()]),
            template="plotly_dark"
        )

    # Update graph function
    def update_graph(self):

        # Generate new data points (replace with real streaming data sources)
        y_values = self.stream_data(self.current_x)
        new_y1 = y_values["actual"]  # Example data for Line 1
        new_y2 = y_values["predicted"]  # Example data for Line 2
        self.current_x += 1
        self.x_data.append(self.current_x)
        self.y_data1.append(new_y1)
        self.y_data2.append(new_y2)

        # Conditional highlighting: Red if new_y1 > 250 or new_y2 > 550, else Blue
        self.colors1.append('red' if y_values["anamoly"] else 'blue')
        #self.colors2.append('red' if new_y2 > 550 else 'green')

        # Adjust x-axis range for scrolling
        x_range = [self.current_x - 100 if self.current_x > 100 else 0, self.current_x]

        # Update figure data
        self.fig.data[0].x = self.x_data
        self.fig.data[0].y = self.y_data1
        self.fig.data[0].marker = dict(color=self.colors1)  # Line 1 conditional colors

        self.fig.data[1].x = self.x_data
        self.fig.data[1].y = self.y_data2
        #fig.data[1].marker = dict(color=colors2)  # Line 2 conditional colors

        self.fig.update_layout(xaxis=dict(range=x_range))

"""

from plotly.graph_objects import FigureWidget, Scatter

class GraphyClass():
    def __init__(self, path):
        self.pipe_df = pd.read_csv(path)
        self.ticker = 0
        self.fig = FigureWidget()
        self.x_data = []
        self.y_data1 = []
        self.y_data2 = []
        self.colors1 = []  # Colors for Line 1
        self.current_x = 0  # Current x-axis value
    
    def stream_data(self, ticker):
        if ticker > len(self.pipe_df):
            temp_df = self.pipe_df.copy()
        else:
            temp_df = self.pipe_df.iloc[:ticker + 1].copy()

        # Anomaly Detection
        temp_df['ds'] = pd.to_datetime(temp_df["Time"])
        temp_df['y'] = temp_df["Inj Gas Meter Volume Instantaneous"]

        if ticker < 3:
            results = {
                "actual": temp_df['y'].iloc[ticker % len(self.pipe_df)],
                "predicted": temp_df['y'].iloc[ticker % len(self.pipe_df)],
                "anomaly": False
            }
            return results

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

        results = {
            "actual": temp_df['y'].iloc[ticker % len(self.pipe_df)],
            "predicted": temp_df['yhat'].iloc[ticker % len(self.pipe_df)],
            "anomaly": temp_df['anomaly'].iloc[ticker % len(self.pipe_df)]
        }
        return results
    
    def create_graph(self):
        self.fig.add_trace(Scatter(
            x=[], 
            y=[], 
            mode='lines+markers', 
            name='Flow Rate', 
            line=dict(color='blue', width=2),
            marker=dict(color='blue', size=2)
        ))
        self.fig.add_trace(Scatter(x=[], y=[], mode='lines', name='Predicted Flow Rate', line=dict(color='green', width=2)))

        # Set layout
        self.fig.update_layout(
            xaxis=dict(title="Time", range=[0, 100]),
            yaxis=dict(title="Value", range=[0, self.pipe_df["Inj Gas Meter Volume Instantaneous"].max()]),
            template="plotly_dark"
        )

    def update_graph(self):
        # Generate new data points
        y_values = self.stream_data(self.current_x)
        new_y1 = y_values["actual"]
        new_y2 = y_values["predicted"]
        self.current_x += 1
        self.x_data.append(self.current_x)
        self.y_data1.append(new_y1)
        self.y_data2.append(new_y2)

        # Conditional highlighting
        self.colors1.append('red' if y_values["anomaly"] else 'blue')
        """
        if y_values["anomaly"]:
            message = Mail(
                from_email=Email("EOGaurd <pedigonatalie@gmail.com>"),
                to_emails='harsha8913@gmail.com',
                subject='Anomaly Detected!',
                html_content='<strong>URGENT: Hydrate has formed. Maintenance required.</strong>'
            )
            try:
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)

        """
        # Adjust x-axis range for scrolling
        x_range = [self.current_x - 100 if self.current_x > 100 else 0, self.current_x]

        # Update traces directly
        with self.fig.batch_update():
            self.fig.data[0].x = self.x_data
            self.fig.data[0].y = self.y_data1
            self.fig.data[0].marker.color = self.colors1  # Update marker colors

            self.fig.data[1].x = self.x_data
            self.fig.data[1].y = self.y_data2

            self.fig.update_layout(xaxis=dict(range=x_range))
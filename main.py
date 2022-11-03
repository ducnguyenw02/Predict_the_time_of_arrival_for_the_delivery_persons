import create_data
import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.offline as py
import seaborn as sns

import matplotlib.ticker as mtick

def main():

    # Tạo file dữ liệu mới và đọc file dữ liệu csv được khởi tạo 
    # path = "D:/Github/Predict_the_time_of_arrival_for_the_delivery_persons/dataset/data"
    # os.chdir(path)
    # df = pd.read_csv(create_data.main(path))

    # Đọc file dữ liệu có sẵn 
    df = pd.read_csv("D:/Github/Predict_the_time_of_arrival_for_the_delivery_persons/dataset/data_new/dataset_new.csv")
    del df['ID']
    del df['Delivery_person_ID']
    del df['Unnamed: 0']
    for feature in df.columns:
        if feature in ('ID', 'Delivery_person_ID', 'Delivery_person_Age','Delivery_person_Ratings','Restaurant_latitude','Restaurant_longitude'
    ,'Delivery_location_latitude','Delivery_location_longitude','Order_Date','Time_Orderd','Time_Order_picked','Time_taken_(min)'):
            continue
        x = df[feature].value_counts()

        trace = go.Pie(labels = x.index, values = x, textinfo= 'value')

        #layout = go.Layout(title = feature)

        fig = go.Figure(data= [trace])

        py.iplot(fig, image_width = 25, image_height = 25)

if __name__ == '__main__':
    main()
import create_data
import os
import pandas as pd 
import numpy as np

def main():

    # Tạo file dữ liệu mới và đọc file dữ liệu csv được khởi tạo 
    # path = "D:/Github/Predict_the_time_of_arrival_for_the_delivery_persons/dataset/data"
    # os.chdir(path)
    # df = pd.read_csv(create_data.main(path))

    # Đọc file dữ liệu có sẵn 
    df = pd.read_csv("D:/Github/Predict_the_time_of_arrival_for_the_delivery_persons/dataset/data_new/dataset_new.csv")
    print(df)

if __name__ == '__main__':
    main()
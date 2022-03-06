import numpy as np
import pandas as pd
import datetime as dt
import sys
import os


def main():

    print("Using pandas library for data manipulation and cleansing:")
    print()

    # first we open the file we want to clean
    df_input_file = pd.read_csv(
        r'/Users/jordyhers/Downloads/Ex_Files_Learning_Python_Upd/Exercise Files/Ch6/sales_data_test.csv', dtype=float)
    print(df_input_file)

    # Lets now find the number of rows and columns
    print('Number of rows and columns')
    print(df_input_file.shape)
    print()

    # # what about the information related to the data
    # print('Information related to data')
    # print(df_input_file.info)
    # print()

    # print("summary descriptive stats for numerical columns:")
    # print(df_input_file.describe())
    # print()

    df_result = df_input_file["is_action"].value_counts()
    print("To know the repetition of values in the column is_action:")
    print(df_result)
    print()

    # df_input_file = pd.DataFrame(data=df_input_file, index=["Mario Kart", "Tomb Raider", "Fifa 2022",
    #                                                         "Nba 2k", "Fortnite", "Goddess", "Tetris", "Horizon", "Katamari", "Watch Dog", "Element 3"])
    # print(df_input_file)

    # Clear duplicated files
    df_result = df_input_file.duplicated()
    print("duplicated rows:")
    print(df_result)
    print()


if __name__ == "__main__":
    main()

import numpy as np
import pandas as pd


def main():
    print("pandas version: {}".format(pd.__version__))
    # randn(): return a sample (or samples) from the standard normal distribution
    s_data = pd.Series(np.random.randn(5))
    print(s_data)
    # create a dataframe from a dictionary
    dictionary = {"col 1": [1., 2., 3., 4., 5.], "col 2": [
        6, 7, 8, 9, 10], "col 3": ["uno", "dos", "tres", "cuatro", "cinco"]}
    df_data = pd.DataFrame(data=dictionary, index=[
                           'row 1', 'row 2', 'row 3', 'row 4', 'row 5'])
    print(df_data)


if __name__ == '__main__':
    main()

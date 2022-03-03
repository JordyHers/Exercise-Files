
import pandas as pd


def main():

    print("Difference when prefexing imports")
    print()

    # If you get an error
    df_input_file = pd.read_csv('sales_data_test.csv', dtype=float)
    print(df_input_file)

    # Try this to fix your import path
    df_input_file = pd.read_csv(
        r'/Users/jordyhers/PythonTipes/sales_data_test.csv', dtype=float)
    print(df_input_file)


if __name__ == "__main__":
    main()

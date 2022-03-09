import matplotlib.pyplot as plt
import seaborn as sns


def main():
    iris_data = sns.load_dataset("iris")
    print(iris_data)
    if __name__ == '__main__':
        main()

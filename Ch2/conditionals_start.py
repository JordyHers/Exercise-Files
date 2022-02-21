#
# Example file for working with conditional statements
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if (x > y):
        print("x is greater than y")
    elif (x < y):
        print("x is less than y")
    # conditional statements let you use "a if C else b"
    elif (y % x == 0):
        print("x is a multiple of y")

    print(y % x == 0)


if __name__ == "__main__":
    main()

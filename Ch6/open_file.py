

def main():

    # my_cv = open("mycvtext.txt", "w")
    # my_cv.write("Here is the beginning of life.\n")
    # my_cv.close()

    # my_cv = open("mycvtext.txt", "a")
    # my_cv.write("Add this new line to the end of the file test.txt\n")
    # my_cv.close()

    my_cv = open("mycvtext.txt", "r")
    for eachline in my_cv:
        print(eachline)


if __name__ == "__main__":
    main()

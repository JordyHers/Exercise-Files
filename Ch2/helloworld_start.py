#
# Example file for HelloWorld
#
def main():
    #    string length using len() method
    string_0 = "Python is becoming the worlds most popular programminglanguage today"
    print(len(string_0))

    # substrings (or splices) using [start, start + length]
    # get 'Python' word from the start
    string_3 = string_0[6:14]
    print(string_3)


if __name__ == '__main__':
    main()

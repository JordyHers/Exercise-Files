
import math_library


def main():
    # result = math_library.area_of_circle(2)
    # print("The area of the circle is: {}".format(result))
    set_value = set(["Jerry", "Collins", "James",
                     "Marvin", "Thomas", "Leni", "Glenn"])
    set_value2 = set(["Carlton", "Collins", "Michael", "Steven"])
    print("................................\n")
    print("...Set initial values ...\n\n")

    print(set_value)
    print("\n")
    print(set_value2)
    print("\n")
    join_value = set_value.union(set_value2)
    intersection_value = set_value.intersection(set_value2)
    difference_value = set_value.difference(set_value2)
    print("...Set union value...\n\n")
    print(join_value)
    print("\n")
    print("...Set intersection value...\n\n")
    print(intersection_value)
    print("\n\n")
    print("...Set difference value...\n\n")
    print(difference_value)
    print("\n\n")

    subset = {'Collins', 'James', 'Thomas'}
    answer = subset.issubset(set_value)
    print(answer)


if __name__ == '__main__':
    main()

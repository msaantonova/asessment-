"""
Upper and Lower
"""


def count_upper_lower():
    my_string = str(input("Simon says: "))

    length = len(my_string)

    for i in my_string:
        if my_string.isupper():
            print(f"No. of Upper case characters: {len(my_string)}")

        elif my_string.islower():
            print(f"No. of Lower case characters: {len(my_string)}")

count_upper_lower()



# if my_string.isupper() == True:
# "m".isupper() -> False
# "m".islower() -> True
# "M".isupper() -> True
# "M".isupper() -> False


"""
Check 33
"""


def has_33():
    my_list = []

    while True:
        my_string = int(input(f"has_33({[]})"))

        i = 0
        j = 0

        for i in range(0, -1):
            if i == 3 and j == 3:
                if range(i, j) == bool:
                    print(True)
                else:
                    print(False)

has_33()




# has_33([1, 3, 3]) -> True
# has_33([1, 3, 1, 3]) -> False
# has_33 ([3, 1, 3]) -> False

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")


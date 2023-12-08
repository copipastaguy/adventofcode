def getCalibratedValues01(file: str) -> list[int]:
    sum = 0
    # read input file
    with open(file) as input:
        for line in input:
            listOfValues = []
            # filter through each line to look for int
            for character in line:
                try:
                    if type(int(character)) == int:
                        # append all int into array
                        listOfValues.append(character)
                except:
                    pass
        if len(listOfValues) > 1:
            # form a single 2 digit number
            number = str(listOfValues[0]) + str(listOfValues[-1])
            sum += int(number)
        else:
            number = str(listOfValues[0]) + str(listOfValues[0])
            sum += int(number)
    return sum


# def getCalibratedValues02(file: str) -> list[int]:
#     sum = 0

#     # single digit words
#     words = {"one": 1, "two": 2, "three": 3, "four": 4,
#              "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

#     with open(file) as input:
#         for line in input:
#             listOfValues = []
#             dict = {}

#             for word, num in words.items():
#                 if word in line:
#                     listOfValues.insert(line.index(word), num)

#             for character in line:
#                 try:
#                     if type(int(character)) == int:
#                         # get index of int
#                         dict[character] = line.index(character)
#                 except:
#                     pass

#             print(listOfValues)
#     return sum


def main():
    part01 = getCalibratedValues01("input01.txt")
    print(part01)

    # part02 = getCalibratedValues02("input02.txt")


if __name__ == "__main__":
    main()

def commaCode(list):
    # loop through all of the list save the last entry
    for i in range(len(list) - 1):
        # For each item make it a string with comma added
        list[i] = str(list[i] + ",")
#        print(list[i])

#   Add "and" in final spot, pushing the current entry forward
    list.insert((len(list) - 1), 'and')

#    print(list)

#    create a string by joining the list using space as a seperator
    newString = " ".join(list)

#    print(newString)

    return newString


if __name__ == "__main__":

    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(commaCode(spam))

    NBA = ['Amina', 'Fievel', 'Gerard', 'NZ', 'Sara', 'Victor']

    print(commaCode(NBA))

# If number is even should print number // 2 and return this value
# If number is odd should print and return 3 * number + 1

def collatz(number):
    if number % 2 == 0:
        even_number = number // 2
        print(even_number)
        return even_number

    else:
        odd_number = 3 * number + 1
        print(odd_number)
        return odd_number


# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.

# To do, ok.

# collatz(int(input("Give me a number! > ")))

def run():
    try:
        number = int(input("\nGive me a number! > "))
        print("\nI started with", number)

        value = collatz(number)

        while value != 1:
            value = collatz(value)

    except:
        print("\nThat's not a number!")
        run()

run()

# =============================================================================
# Day 13 - Debugging Exercises
# =============================================================================

# Exercise 1: Debug the Odd or Even Code
# Bug: Used = (assignment) instead of == (equality check)

# ORIGINAL (buggy):
# if number % 2 = 0:

# FIXED:
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# =============================================================================

# Exercise 2: Debug the Leap Year Code
# Bug: input() returns a string - modulo operator needs an integer

# ORIGINAL (buggy):
# year = input("Which year do you want to check?")

# FIXED:
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


# =============================================================================

# Exercise 3: Debug the FizzBuzz Code
# Bug 1: print([number]) printed a list instead of the number
# Bug 2: "or" instead of "and" - FizzBuzz printed when either condition was true
# Bug 3: Multiple "if" statements instead of "elif" - multiple branches could run

# ORIGINAL (buggy):
# if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
# if number % 3 == 0:
#     print("Fizz")
# if number % 5 == 0:
#     print("Buzz")
# else:
#     print([number])

# FIXED:
for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
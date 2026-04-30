def factorial(num):
    """This is a recursive function to find the factorial of an integer."""
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)

num=int(input("Enter a number to find the factorial of it: "))
print(factorial.__doc__)
print(f"The factorial of {num} is: ",factorial(num))
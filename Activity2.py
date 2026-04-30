def cube(num):
    return num**3
def divide(num):
    if num % 3==0:
        return cube(num)
    else:
        print(f"{num} is not divisble by 3.")
num=int(input("Enter a whole number: "))
print(divide(num))
def shut():
    return "I am shutting down."
s=input("Do you want to shut down a function Y/N: ").upper()
if s == "Y":
    print(f"The function says: {shut()}")
else:
    print("I will not shut down, bye.")
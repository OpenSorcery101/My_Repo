def get_int():
    print("__name__")
    while True:
        try:
            x = int(input("Enter a number: "))
            return x
        except ValueError:
            print("Please Enter a number.")
            continue
if __name__ == "__main__":
    num1 = get_int()
    print(num1)
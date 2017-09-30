def main():
    compare()

def compare():
    if x == y:
        print("They're equal")
    else:
        print("They're not equal")
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a number.")

x = get_float("Give me a number\n")
y = get_float("Give me another number\n")\

if __name__ == "__main__":
    main()

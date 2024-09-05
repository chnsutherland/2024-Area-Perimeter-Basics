def num_check(question):
    error = "Invalid value\n"
    while True:

        try:
            response = float(input(question))
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
    width = num_check("Width: ")
    height = num_check("Height: ")

    area = width * height
    perimeter = 2 * (width + height)

    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    keep_going = input("Press enter to continue, or any other key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")

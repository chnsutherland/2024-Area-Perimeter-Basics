def num_check(question):

    error = "Invalid value\n"
    while True:

        try:
            response =float(input(question))
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)
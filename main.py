# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import ratingAssingment2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    userinput = float(input("Enter rating between 0 to 5: "))
    r = ratingAssingment2.Rating(userinput)
    while not r.validateRating(userinput):
        userinput = float(input("Enter rating between 0 to 5: "))
        r = ratingAssingment2.Rating(userinput)
    print(r.getRating())

import random


def check(value, type):

    numResponse = ["I wasn't asking for a number, dummy...",
                   "...It's just a yes or no...",
                   "Type \"y\" to continue or \"n\" to exit the program."]

    strResponse = ["I can't calculate with letters you know...",
                   "Just type any number you want, be it negative or positive.",
                   "Please stop messing with me..."]

    noResponse = ["Um... Hello...?",
                  "Is anyone there...?",
                  "I need a response please..."]

    if len(value) == 0:
        print(noResponse[random.randint(0, 2)])

    elif type == "str":
        if value.isdigit() is False:
            return True

        else:
            print(numResponse[random.randint(0, 2)])

    elif type == "int":
        if value.lstrip('-').isdigit():
            return True

        else:
            print(strResponse[random.randint(0, 2)])


class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def display(self):
        print("\nThe Fahrenheit is", self.fahrenheit())


while True:

    while True:
        print("\nHello! Please input a value for Celsius so I can convert it to Fahrenheit.")

        num = input("Celsius: ")

        if check(num, "int") is True:
            break

    temp1 = Temperature(int(num))
    temp1.display()

    while True:
        ans = input("\nWanna convert some more? [y/n]: ").lower()

        if check(ans, "str") is True:
            break

    if ans == "y":
        continue

    elif ans == "n":
        print("See you next time!")
        break

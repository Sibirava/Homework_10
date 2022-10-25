import math
def find_all_dividers(number):
    dividers = []

    for i in range(2, number):
        if number % i == 0:
            dividers.append(i)
    return dividers


def find_simple_dividers(number):

    dividers = find_all_dividers(number)
    simple_dividers = []
    count = 0

    for k in dividers:
        for j in range(2, int(math.sqrt(k)) + 1):
            if k % j == 0:
                count += 1
        if count == 0:
            simple_dividers.append(k)
    return simple_dividers


def main():
    number = int(input("Input your number:"))

    simple_dividers = find_simple_dividers(number)

    msg = f"Simple dividers of a number {number} are {simple_dividers} "

    print(msg)

main()

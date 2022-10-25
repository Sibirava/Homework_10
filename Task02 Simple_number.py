import math
def simple_number(number):

    count = 0

    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            count += 1
    return count

def main():

    number = int(input("Input number: "))
    count = simple_number(number)

    if count == 0:
        msg = f"Simple number"
    else:
        msg = f"Complex number"

    print(msg)

main()
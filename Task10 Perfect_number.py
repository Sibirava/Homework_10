def check_perfect_number(number):
    sum_divider = 0

    for i in range(1, number):
        if number % i == 0:
            sum_divider += i
    return sum_divider

def main ():
    number = int(input("Input number: "))
    sum_divider = check_perfect_number(number)

    if number == sum_divider:
        msg = f"The number {number} is PERFECT"
    else:
        msg = f"The number {number} is not perfect"

    print(msg)
main()
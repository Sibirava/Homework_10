def fibonacci(element):
    first = 0
    second = 1
    third = 0

    if element < 2:
        return element

    ls = []

    while first + second <= element:
        third = first + second
        first = second
        second = third
        ls.append(third)
    return ls


def main():
    element = int(input("Input element in Fibonacci row: "))

    ls = fibonacci(element)

    print(ls)


main()

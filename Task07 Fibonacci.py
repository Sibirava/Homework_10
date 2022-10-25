#RECURSION
def fibonacci(index):
    first = 0
    second = 1

    if index < 2:
        return index   # тк индекс и первые значения равны


    for i in range(2, index + 1):
        third = first + second
        first = second
        second = third
    return third


def main():
    index = int(input("Input index in Fibonacci row: "))
    element = fibonacci(index)

    msg = f"Fibonacci[{index}] is {element}"

    print(msg)

main()



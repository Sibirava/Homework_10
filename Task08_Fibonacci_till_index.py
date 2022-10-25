def fibonacci_till_bound(index):
    first = 0
    second = 1

    if index < 2:
        return index

    ls = []
    for i in range(2, index + 1):
        third = first + second
        first = second
        second = third
        ls.append(third)
    return ls

def main ():
    index = int(input("Input index: "))

    ls = fibonacci_till_bound(index)

    print(ls)

main()

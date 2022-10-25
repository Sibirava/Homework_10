def find_simple_number_in_range(index):
    ls = []

    for i in range(2, index + 1):
        if i % 2 == 0:
            break
        else:
            ls.append(i)
    return ls

def main():
    number = int(input("Input number: "))
    ls = find_simple_number_in_range(number)
    print(ls)

main()

def find_simple_number_till_bound(number):
    ls = []

    for i in range(2, number):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ls.append(i)
    return ls

def main():
    number = int(input("Input number: "))
    ls = find_simple_number_till_bound(number)
    print(ls)

main()

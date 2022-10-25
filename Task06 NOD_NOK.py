# НОД и НОК of the number

def find_nod(a, b):

    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller + 1):
        if (a % i == 0) and (b % i == 0):
            nod = i
    return nod

def find_nok(a, b):

    if a > b:
        bigger = b
    else:
        bigger = a
    while True:
        if (bigger % a == 0) and (bigger % b == 0):
            nok = bigger
            break
        else:
            bigger += 1
    return nok

def main():
    a = int(input("a = "))
    b = int(input("b = "))

    if a > 0 and b > 0:
        nod = find_nod(a, b)
        nok = find_nok(a, b)
        print("NOD = ", nod, "NOK = ", nok)
    else:
        print("Wrong number")

main()
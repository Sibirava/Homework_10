import random

def heads_tails(number):

    num_simulations = 1
    count_heads = 0
    count_tails = 0
    while num_simulations <= number:
        num_simulations += 1
        result = random.randint(0, 2)
        if result == 0:
            count_heads += 1
        else:
            count_tails += 1
    return(count_heads, count_tails)

def main():
    number = int(input("Input number of simulations: "))

    heads, tails = heads_tails(number)
    msg = f"For {number} of tries there are {heads} heads and {tails} tails "
    print(msg)

main()

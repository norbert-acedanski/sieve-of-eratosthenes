import sys

def primes_less_than(limit_number: int) -> list:
    if limit_number <= 2:
        print("Input number greater than 2!")
        sys.exit()
    numbers_list = [None]*limit_number
    numbers_list[0] = False
    numbers_list[1] = False
    for number in range(2, limit_number):
        if numbers_list[number] == None:
            numbers_list[number] = True
            for multiple in range(number + number, limit_number, number):
                numbers_list[multiple] = False
    return [number for number in range(limit_number) if numbers_list[number]]

if __name__ == "__main__":
    print(primes_less_than(100))
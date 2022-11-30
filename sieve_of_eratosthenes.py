import math


def primes_less_than(limit_number: int) -> list:
    if limit_number <= 2:
        raise ValueError("Input number greater than 2!")
    numbers_list = [None]*limit_number
    numbers_list[0] = False
    numbers_list[1] = False
    for number in range(2, math.isqrt(limit_number)):
        if numbers_list[number] is None:
            numbers_list[number] = True
            for multiple in range(number**2, limit_number, number):
                numbers_list[multiple] = False
    for number in range(math.isqrt(limit_number) + 1, limit_number):
        if numbers_list[number] is None:
            numbers_list[number] = True
    return [number for number in range(limit_number) if numbers_list[number]]


if __name__ == "__main__":
    print(primes_less_than(100))

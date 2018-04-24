# work_with_simple_numbers
import math
import random
# Finding simple multipliers
# time =>  O(sqrt(number))

def find_simple_multipliers(number):
    results = []
    i = 2
    while number % 2 == 0:
        results.append(2)
        number /= 2
        print "number =>", number
        break
    i = 3
    max_result = math.sqrt(number)
    while i <= max_result:
        while number % i == 0:
            if number not in results:
                results.append(i)
            number = number / i
            max_result = math.sqrt(number)
        i += 2
    if number > 1:
        results.append(number)
    return results

# Eratosthenes sieve, find prime numbers
def find_primes_numbers(max_number):
    result = []
    list_numbers = [True] * max_number
    list_numbers[0] = list_numbers[1] = False
    for (index, value) in enumerate(list_numbers):
        if value:
            for j in range(index*index, max_number, index):
                list_numbers[j] = False
    for index in range(2, max_number):
        if list_numbers[index]:
            result.append(index)
    return result

# Fermat's test, check if number is prime
def is_prime(number, max_test):
    for i in range(1, max_test+1):
        random_number = random.randint(2, number)
        if ((random_number**(number-1)) % number) != 1:
            return False
    return True

if __name__ == "__main__":
    number = 29
    print "simple multipliers from number {} is:".format(number), \
        find_simple_multipliers(number)
    print "primes numbers from 2 to {} is:".format(number), \
        find_primes_numbers(number)
    print "Is the number {} the prime number? Answer:".format(number), is_prime(number,2)
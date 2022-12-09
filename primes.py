"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError("has to be greater than 0!")

    else:
        number = 2
        counter = 0

    while counter < number_of_primes:
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False

        if prime:
            list.append(number)
            counter+=1

        number = number + 1
    return list

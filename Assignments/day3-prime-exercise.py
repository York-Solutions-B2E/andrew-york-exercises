# Generate a list of prime numbers (numbers that are only divisible by 1 and themselves) from 1 to 10000

primeList = []

def testPrime(num):
    isPrime = True
    for z in range(2, num):
        if num % z == 0:
            isPrime = False
            break
    if isPrime:
        primeList.append(num)

# Starting at 2 since primes are by definition greater than 1
for i in range(2, 10001):
    testPrime(i)

print(primeList)
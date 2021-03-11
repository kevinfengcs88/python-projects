minimum = int(input("Enter an integer for the lower limit of the range you would like to test for prime numbers: "))
maximum = int(input("Enter an integer for the upper limit of the range you would like to test for prime numbers: "))
primeList = []

def isPrime(num):
    for i in range(2, int(num/2 + 1)):
        if (num % i) == 0:
            return False
    else:
        return True

def obtainPrimeNumbers(min, max):
    for i in range(min, max + 1):
        if isPrime(i):
            primeList.append(i)

if minimum < 0 or maximum < 0 or minimum > maximum:
    print("Enter valid limits for the range you would like to test for prime numbers: ")
else:
    obtainPrimeNumbers(minimum, maximum)
    print(primeList)

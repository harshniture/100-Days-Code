#Ask the user to enter a number. Then find all the primes up to that number.

def isPrime(num):
    for i in range(2,num):
        if (num % i) == 0:
          return False
    return True
 
def allPrimes(num):
  primes = []
  for n in range(2,num+1):
    if isPrime(n) is True:
        primes.append(n)
  return primes
 
num = int(input("Upper Limit: "))
primes = allPrimes(num)
print(primes)
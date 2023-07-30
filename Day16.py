#Ask the user to enter a number. Then find all the primes factors for the number.

def prime_factors(n):
   factors = []
   divisor = 2
   while n > 2:
    if(n % divisor == 0):
        factors.append(divisor)
        n = n / divisor
    else:
        divisor = divisor + 1
   return factors
 
num = int (input('Number: '))
factors = prime_factors(num)
print(factors)
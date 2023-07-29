#For a given number, check whether the number is a prime number or not.

def is_prime(num):
   for i in range(2,num):
       if (num % i) == 0:
           return False
   return True


num = int(input("Num: "))

check_prime = is_prime(num)

if check_prime:
   print('Prime Number')
else:
   print('Not a Prime Number')
#Find the smallest prime factor for the given number.

def get_smallest_factor(num):
   factor = 2
   while num % factor != 0:
       factor += 1
   return factor
 
num = int(input('Num: '))
 
smallest_factor = get_smallest_factor(num)
 
print('Smallest prime factor: ', smallest_factor)
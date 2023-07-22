#Convert a decimal number to binary number using a recursive function.

def dec_to_binary(n):
   if n > 1:
       dec_to_binary(n//2)
   print(n % 2,end = '')
   
dec_to_binary(1000)
#Reverse a number.

def reverseNum(num):
   reverse = 0
   while(num>0):
       last_digit = num%10
       reverse = reverse*10 + last_digit
       num = num//10
   return reverse
 
n=int(input("Number: "))
reverse = reverseNum(n)
print("Reverse number:",reverse)
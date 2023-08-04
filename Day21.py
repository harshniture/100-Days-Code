#Reverse a string using a recursive function.

def reverseRecur(str):
   if len(str) == 0:
       return str
   else:
       return reverseRecur(str[1:]) + str[0]
 
str = input("String: ")
rev_str = reverseRecur(str)
print ('Reverse string: ', rev_str)
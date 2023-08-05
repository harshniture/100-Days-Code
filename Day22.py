#Reverse a string.
#If the input is: Hello World.
#The output should be: .dlroW olleH

def reverseString(str):
   reverse = ""
   for char in str:
       reverse = char + reverse
   return reverse
 
str = input("String: ")
result = reverseString(str)
print(result)
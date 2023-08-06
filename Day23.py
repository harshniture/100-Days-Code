#Reverse a string using a stack.

def reverseStack(str):
  stack = []
  for char in str:
      stack.append(char)
  rev = ''
  while len(stack) > 0:
       last = stack.pop()
       rev = rev + last       
  return rev
usr_str = input('String:')
reverse = reverseStack(usr_str)
print('Reversed is: ', reverse)
#Reverse the word in a sentence.
#For example, if the input string is “Hello young Programmer”, the output will be “Programmer young Hello”

def reverseWords(sentence):
   words = sentence.split()
   words.reverse()
   return " ".join(words)
 
usr_input = input("Sentence: ")
reverse = reverseWords(usr_input)
print('Reversed words: ', reverse)
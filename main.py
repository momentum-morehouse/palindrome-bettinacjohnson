##HOW DO YOU USE THE RE.SUB??????????
import re

# def get_tests():
#  print("Hello!")
#  get_test_username()
#  get_test_num()
#  get_phrase()
#  get_tests()

#  def get_test_username():  
#   name = input('Please enter your name  ')
#   print(name)
#   if name == name[::-1]:
#     print(name, 'is a palindrome.')
#   else:
#     print(name,'is not a palindrome.')

# def get_phrase():
#   word = input('Enter a word of phrase  ')
#   #The next line wipes the punctuation from the string. This will strip the string
#   cleaned_phrase = re.sub(r'[^A-Za-z]', '', word.lower())

#   print(cleaned_phrase)
#   print(word)
#   #This tests the stripped string by reversing the user input
#   if cleaned_phrase == cleaned_phrase[::-1]:
#     print(word, 'is a palindrome.')
#   else:
#     print(word,'is not a palindrome.')
# #This function will call the test for each 



#Getting info from user
#Question1
def get_test_username():  
  name = input('Please enter your name: ')
  print('Hello ' + name + '!')
  # if name == name[::-1]:
  #   print(name, 'is a palindrome.')
  # else:
  #   print(name,'is not a palindrome.')


#Question2
def get_test_num():
  num = input('Enter your age:  ')
  print(num)
  # if num == num[::-1]:
  #   print(num, 'is a palindrome.')
  # else:
  #   print(num,'is not a palindrome.')

#Question3
def get_phrase():
  word = input('Enter a word or phrase: ')
  #The next line wipes the punctuation from the string. This will strip the string
  cleaned_phrase = re.sub(r'[^A-Za-z]', '', word.lower())

  # print(cleaned_phrase)
  # print(word)
  #This tests the stripped string by reversing the user input
  if cleaned_phrase == cleaned_phrase[::-1]:
    print(word, 'IS a palindrome.')
  else:
    print(word,'is NOT a palindrome.')
#This function will call the test for each 
def get_tests():
  print ('Hello!')
  get_test_username()
  get_test_num()
  get_phrase()

get_tests()

#MY INITIAL CODE
# string=input(("Enter a string:"))
# if(string==string[::-1]):
#       print("The string is a palindrome")
# else:
#       print("Not a palindrome")


# def get_phrase():
#   word = input('Enter a word or phrase ')
#   cleaned_phrase = re.sub((r'[A-Za-z]', "", word.lower())
#   print(cleaned_phrase)
#   print(word)
#   if cleaned_phrase == cleaned_phrase[::-1]:
#   print(word, 'is a palindrome.')
#   else:
#   print(word, 'is not a palindrome.')
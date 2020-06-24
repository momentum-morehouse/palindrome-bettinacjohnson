# # function which return reverse of a string 
# print("Let's play a palindrome game!")
# def is_palindrome(phrase): 
#   reverse = ''.join(reversed(phrase))
#     # return phrase == phrase[::-1] 

# phrase = input("Enter a number or word: ")
# ans = is_palindrome(phrase) 
  
# if (phrase == reverse): 
#   return True
# print("Yes, this is a palindrome!") 
# else: 
#   return False
# print("No, this is not a plaindrome!") 


string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")



# def ispalindrome(s): 
#     return s == s[::-1] 
  
# # Driver code 
# s = ('')
# ans = ispalindrome(s) 
  
# if ans: 
#     print("Yes") 
# else: 
#     print("No") 

# def is_palindrome(s): 
#     # Using predefined function to  
#     # reverse to string print(s) 
#     rev = ''.join(reversed(s)) 

#     # Checking if both string are  
#     # equal or not 
#     if (s == rev): 
#         return True
#     return False
  
# # main function 
# s = "malayalam"
# ans = is_palindrome(s) 
  
# if (ans): 
#     print("Yes") 
# else: 
#     print("No")
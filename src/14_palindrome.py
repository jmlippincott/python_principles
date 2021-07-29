# A string is a palindrome when it is the same when read backwards.
#
# For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".
#
# Write a function named palindrome that takes a single string as its parameter. Your function should return True if the string is a palindrome, and False otherwise.

def palindrome(word):
    word = word.lower()
    drow = list(word)
    word = list(word)
    drow.reverse()
    return word == drow

def palindrome(word):
    return word.lower() == word.lower()[::-1]
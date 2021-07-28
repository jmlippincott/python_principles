# Two strings are anagrams if you can make one from the other by rearranging the letters.
#
# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.
#
# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return set([(i,word1.count(i)) for i in word1]) == set([(i,word2.count(i)) for i in word2])
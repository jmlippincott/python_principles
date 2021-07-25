# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
#
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(word):
    word = list(word)
    capitals = [count for count,ele in enumerate(word) if ele.isupper()]
    return capitals
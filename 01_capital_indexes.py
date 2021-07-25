def capital_indexes(word):
    word = list(word)
    capitals = [word.index(i) for i in word if i.isupper()]
    return capitals

capital_indexes("hELlO")
def capital_indexes(word):
    word = list(word)
    capitals = [count for count,ele in enumerate(word) if ele.isupper()]
    return capitals

capital_indexes("hELlO")
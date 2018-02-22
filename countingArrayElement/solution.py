def count(array):
    r = {}
    for c in array:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r
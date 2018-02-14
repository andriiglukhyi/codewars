def is_isogram(string):
    new = string.lower()
    print(new)
    for item in new:
        if new.count(item)>1:
            return False
    return True
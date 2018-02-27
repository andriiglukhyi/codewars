def reverse_words(str):
    new_str = ""
    for items in str.split(" "):
        new_str+= items[::-1]+ " "
    return new_str[:-1]
    
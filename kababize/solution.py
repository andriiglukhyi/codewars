def kebabize(string):
    a = ""
    for item in string:
        
        if item == item.upper() and item.isdigit() == False:
            a+= "-"+ item.lower()
        elif item.isdigit() == False and type(item) == str:
            a+= item
    return a.strip("-")
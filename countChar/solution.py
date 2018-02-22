def count(string):
    # The function code should be here
    a = {}
    if string == '':
        return {}    
    else:
        for item in string:
            if item not in a:
                a.update({item: string.count(item)})
        return a
    
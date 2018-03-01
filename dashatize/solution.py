def dashatize(num):
    a = ''
    if num == None:
        return 'None'
    else:
        num = abs(num)
        for item in list(str(num)):
            if int(item)%2 == 1:
                a+= '-'+item+'-'
            else:
                a+=item
        b = a.replace('--', '-') 
    return b.strip('-')
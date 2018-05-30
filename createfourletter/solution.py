def bird_code(arr):
    new = []
    for item in arr:
        if '-'in item:
            item = item.replace('-', ' ')
        temp = item.split(' ')
        if len (temp) == 1:
            new.append(temp[0][:4].upper())
        if len(temp) == 2:
            new.append(temp[0][:2].upper() + temp[1][:2].upper())
        if len(temp) == 3:
            new.append(temp[0][0].upper() + temp[1][0].upper() + temp[2][:2].upper())
        if len(temp) == 4:
            new.append(temp[0][0].upper() + temp[1][0].upper() + temp[2][0].upper() + temp[3][0].upper())
    return new
def sumDigits(number):
    total = 0
    for item in str(number).replace('-', ''):
        total+= int(item)
    return total
       
       
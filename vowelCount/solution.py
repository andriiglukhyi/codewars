def getCount(str):
    num_vowels = 0
    num_vowels += str.count('a') + str.count('e') + str.count('i')+ str.count('o')+str.count('u')
    
    return num_vowels
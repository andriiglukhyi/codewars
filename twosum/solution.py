from itertools import permutations

def two_sum(numbers, target):
    perm = permutations(numbers,2)
    for item in list(perm):
        if sum(item) == target:
            a = numbers.index(item[0])
            numbers[a] = None
            print(numbers)
            b= numbers.index(item[1])
            return [a, b]
        

def presses(phrase):
    print(phrase)
    total = 0
    char = ['1', 'abc2', 'def3', 'ghi4', 'jkl5', 'mno6','pqrs7', 'tuv8', 'wxyz9', ' 0', '#', '*']
    for let in phrase.lower():
        for but in char:
            if let in but:
                total+=but.index(let)+1
    return total
        
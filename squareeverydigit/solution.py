def square_digits(num):
    arr = ""
    for item in str(num):
        arr += str(int(item)**2)
    return int(arr)
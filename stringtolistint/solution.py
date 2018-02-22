def string_to_int_list(s):
    s = s.replace(',', ' ').strip()
    arr = []
    for item in s.split(' '):
        arr.append(int(item))
    print arr
    return arr
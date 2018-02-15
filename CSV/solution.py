def toCsvText(array) :
    res = ""
    for item in array:
        res+=str(item)[1:-1].replace(" ", "")+"\n"
    return res.strip()
    
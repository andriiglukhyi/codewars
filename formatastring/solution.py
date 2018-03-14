def namelist(names):
    print(names)
    a = []
    if len(names) == 0:
        return ''
    elif len(names) == 1: 
        return names[0]["name"]
    elif len(names) == 2:
        return names[0]["name"] + " & "+ names[1]["name"]
    else:
        for item in range(len(names)-1):
            a.append((names[item]["name"]))
        return ", ".join(a) + " & "+ names[-1]["name"]
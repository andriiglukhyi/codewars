def human_years_cat_years_dog_years(human_years):
    h = human_years
    k = 0
    d = 0
    if h == 1:
        k+=15
        d +=15   
    elif h == 2:
        k+= 24
        d += 24
    elif h == 3:
        k += 28
        d += 29
    elif h >=4:
        k = 28 + (h-3)*4
        d = 29 + (h-3)*5
    return [h,k,d]
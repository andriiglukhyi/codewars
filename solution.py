def regressionLine(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line 
        (Y on X).
    """
    sumX2 = 0
    sumY2 = 0
    sumxy = 0
    sumX = sum(x)
    sumy = sum(y)


    for item in x:
        sumX2 += item**2
        sumxy += x[item]+y[item]        
    for item in y:
        sumY2 += item**2
    
    return (float(((sumX2*sumy - sumX*sumxy)/(len(x)*sumX2- sumX**2)), 4), float((len(x)*sumxy - sumX*sumy )/(len(x)*sumX2 - sumX**2), 4))
         
regressionLine([25,30,35,40,45,50], [78,70,65,58,48,42])
def find_the_ball(start, swaps):
    ball = start
    if len(swaps) >= 2:
        for item in swaps:
            if item[0] == ball:
                ball = item[1]
            elif item[1]==ball:
                ball = item[0]
        return ball
    return start
            
            
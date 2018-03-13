def balance(left, right):
    if (left.count('!')*2+left.count('?')*3) > (right.count('!')*2+right.count('?')*3):
        return "Left"
    elif left.count('!')*2+left.count('?')*3 < right.count('!')*2+right.count('?')*3:
        return "Right"
    return "Balance"
  
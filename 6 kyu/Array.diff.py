def array_diff(a, b):
    
    for digit in b:
        while digit in a:
            a.remove(digit)

    return a
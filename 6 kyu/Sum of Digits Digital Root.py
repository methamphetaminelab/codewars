def digital_root(n):

    def rasklad(n):
        number = 0
        for digit in str(n):
            number += int(digit)

        return number

    while len(str(n)) > 1:
        n = rasklad(n)
    
    return n
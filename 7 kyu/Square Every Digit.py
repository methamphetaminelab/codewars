def square_digits(num):
    if num <= 0: return 0

    result = ''
    for number in str(num):
        result += str(int(number)**2)

    return int(result)
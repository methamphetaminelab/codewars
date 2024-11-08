'''
Создайте функцию, которая принимает положительное целое число и возвращает следующее большее число, которое можно получить путем перестановки его цифр. Например:

  12 ==> 21
 513 ==> 531
2017 ==> 2071

Если цифры не могут быть переставлены в большее число, верните -1 (или ноль в Swift, None в Rust):

  9 ==> -1
111 ==> -1
531 ==> -1
'''

def next_bigger(n):
    digits = list(str(n))
    i = len(digits) - 2

    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1

    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]

    digits = digits[:i + 1] + sorted(digits[i + 1:])
    
    return int("".join(digits))
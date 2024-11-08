'''
Вам дана строка s. Каждая буква в s встречается один раз.

Рассмотрим все строки, образованные перестановкой букв в s. Упорядочив эти строки в словарном порядке, верните средний термин. 
(Если последовательность имеет четную длину n, определите ее средний член как (n/2)-й член.)

Пример

Для s = «abc» результатом должно быть «bac».

Перестановки по порядку: «abc», «acb», «bac», «bca», «cab», «cba». Итак, средний термин — «bac».
Ввод/вывод

[вход] строка с

уникальные буквы (2 <= длина <= 26)

[вывод] строка

средняя перестановка.'''

from math import factorial

def middle_permutation(s):
    s = ''.join(sorted(s))
    result = []
    n = len(s)
    k = factorial(n) // 2 - 1
    
    while n > 0:
        n -= 1
        fact = factorial(n)
        index, k = divmod(k, fact)
        result.append(s[index])
        s = s[:index] + s[index+1:]
    
    return ''.join(result)
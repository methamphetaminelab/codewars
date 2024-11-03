def is_interesting(number, awesome_phrases):
    def followed_by_zeros(num):
        return str(num)[1:] == '0' * (len(str(num)) - 1)
    
    def all_same_digits(num):
        return len(set(str(num))) == 1
    
    def incrementing(num):
        s = str(num)
        return s in '1234567890'
    
    def decrementing(num):
        s = str(num)
        return s in '9876543210'
    
    def palindrome(num):
        s = str(num)
        return s == s[::-1]
    
    def in_awesome_phrases(num):
        return num in awesome_phrases
    
    def is_really_interesting(num):
        if num < 100:
            return False
        return (followed_by_zeros(num) or all_same_digits(num) or
                incrementing(num) or decrementing(num) or
                palindrome(num) or in_awesome_phrases(num))
    
    # Check the current number and the next two numbers
    if is_really_interesting(number):
        return 2
    elif is_really_interesting(number + 1) or is_really_interesting(number + 2):
        return 1
    return 0

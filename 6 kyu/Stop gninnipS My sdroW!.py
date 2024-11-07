def spin_words(sentence):
    words = sentence.split()
    
    result = []
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    
    resultWords = ''
    for index, word in enumerate(result):
        if index != len(result) - 1:
            resultWords += f'{word} '
        else:
            resultWords += word
            
    return resultWords
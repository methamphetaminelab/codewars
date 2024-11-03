def generate_hashtag(s):
    if s == '': return False
    result = "#"
    for word in s.split():
        result += word[0].upper()
        result += word[1:].lower()
    if len(result) > 140: return False
    return result
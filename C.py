def string_splosion(s):
    result = ""
    for i in range(1, len(s)+1):
        result += s[:i]
    return result

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
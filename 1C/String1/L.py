def theEnd(s, front):
    if front:
        return s[0]
    else:
        return s[-1]

s = input()
front = input().lower() == "true"
print(theEnd(s, front))
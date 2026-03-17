def comboString(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

a = input()
b = input()
print(comboString(a, b))

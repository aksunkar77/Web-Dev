def xor(x, y):

    return (x and not y) or (not x and y)

x, y = map(int, input().split())

x_bool = bool(x)
y_bool = bool(y)

print(int(xor(x_bool, y_bool)))
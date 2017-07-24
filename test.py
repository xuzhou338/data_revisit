def list_subtract(a, b):
    c = list(set(a) - set(b))
    return c

choice_full = list(range(1, 10))
b = [1, 3, 5, 6, 7, 4]
c = list_subtract(choice_full, b)
print(c)
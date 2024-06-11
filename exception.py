a = [1, 2, 3, 4, 5]

try:

    x = a[5]
    a = b / 2
except (IndexError,NameError):
    a.append(5)  # Append 5 to the end of the list
    x = a[5]
    print(x)
    a = b/2
else:
    print(x)



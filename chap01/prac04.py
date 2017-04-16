# coding: utf-8

def med3(a, b, c):

    if(a >= b):
        if(b >= c):
            return b
        elif(a >= c):
            return c
        else:
            return a
    elif(a > c):
        return a
    elif(b > c):
        return c
    else:
        return b


# Main function
print("Compare three values in one list and answer the center value.")

print('med3({0}, {1}, {2}) = {3}'.format(3, 2, 1, med3(3, 2, 1)))
print('med3({0}, {1}, {2}) = {3}'.format(3, 2, 2, med3(3, 2, 2)))
print('med3({0}, {1}, {2}) = {3}'.format(3, 1, 2, med3(3, 1, 2)))
print('med3({0}, {1}, {2}) = {3}'.format(3, 2, 3, med3(3, 2, 3)))
print('med3({0}, {1}, {2}) = {3}'.format(2, 1, 3, med3(2, 1, 3)))
print('med3({0}, {1}, {2}) = {3}'.format(3, 3, 2, med3(3, 3, 2)))
print('med3({0}, {1}, {2}) = {3}'.format(3, 3, 3, med3(3, 3, 3)))
print('med3({0}, {1}, {2}) = {3}'.format(2, 2, 3, med3(2, 2, 3)))
print('med3({0}, {1}, {2}) = {3}'.format(2, 3, 1, med3(2, 3, 1)))
print('med3({0}, {1}, {2}) = {3}'.format(2, 3, 2, med3(2, 3, 2)))
print('med3({0}, {1}, {2}) = {3}'.format(1, 3, 2, med3(1, 3, 2)))
print('med3({0}, {1}, {2}) = {3}'.format(2, 3, 3, med3(2, 3, 3)))
print('med3({0}, {1}, {2}) = {3}'.format(1, 2, 3, med3(1, 2, 3)))

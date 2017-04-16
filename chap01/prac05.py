# coding: utf-8

# 中央値を求める関数は、以下のようにも実現できる。ただし、List1C-1(参考書参照)に示すmed3と比較すると
# 実行効率が悪い。その理由を説明せよ。

def med3(a, b, c):

    if((b >= a & a >= b) | (a >= b & c >= a)):
        return a
    elif((a > b & b > c) | (b > a & c > b)):
        return b
    else:
        return c


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

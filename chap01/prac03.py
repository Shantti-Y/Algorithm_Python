# coding: utf-8

def min4(a, b, c, d):
    minnum = a

    if(b < minnum):
        minnum = b
    if(c < minnum):
        minnum = c
    if(d < minnum):
        minnum = d

    return minnum


# Main function
print("Compare four values in one list and answer the lowest value.")
print("Input four values.")

ar  = []
for i in range(4):
    print("No.", i + 1)
    a = int(input())
    ar.append(a)

print("The lowest number in the list is", min4(ar[0], ar[1], ar[2], ar[3]), ".")

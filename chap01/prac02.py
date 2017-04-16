# coding: utf-8

def min3(a, b, c):
    minnum = a

    if(b < minnum):
        minnum = b
    if(c < minnum):
        minnum = c

    return minnum


# Main function
print("Compare three values in one list and answer the lowest value.")
print("Input three values.")

ar  = []
for i in range(3):
    print("No.", i + 1)
    a = int(input())
    ar.append(a)

print("The lowest number in the list is", min3(ar[0], ar[1], ar[2]), ".")

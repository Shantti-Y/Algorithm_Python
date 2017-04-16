# coding: utf-8

def max4(a, b, c, d):
    maxnum = a

    if(b > maxnum):
        maxnum = b
    if(c > maxnum):
        maxnum = c
    if(d > maxnum):
        maxnum = d

    return maxnum




# Main function
print("Compare four values in one list and answer the highest value.")
print("Input four values.")

ar  = []
for i in range(4):
    print("No.", i + 1)
    a = int(input())
    ar.append(a)

print("The highest number in the list is", max4(ar[0], ar[1], ar[2], ar[3]), ".")

# Searching a number from a lang class array program with 'bsearch' function in a descending order
def int_cmp(a, b):
    if(a < b):
        return -1
    elif(a > b):
        return 1
    else:
        return 0

def bsearch(key, base, size):
    pl = 0
    pr = size - 1
    res = 1

    while(res != 0):
        pc = int((pl + pr) / 2)
        x = base[pc]
        res = int_cmp(x, key)

        if(res == 0):
            return pc
        elif(res == 1):
            pl = pc + 1
        elif(res == -1):
            pr = pc - 1

# Main Function
print("I'm gonna search a key you input in a binary search method.")
print("Number of elements :")
nx = int(input())
ar = []

print("Input a number in a descending order for specified times.")
for i in range(nx):
    while(True):
        print("x[{0}]".format(i))
        x = int(input())
        if(i == 0 or x <= ar[i - 1]):
            ar.append(x)
            break

print("the key")
ky = int(input())

idx = bsearch(ky, ar, nx)

if(idx == -1):
    print("Failed Searching '{0}'".format(ky))
else:
    print("{0} is in x[{1}]".format(ky, idx))

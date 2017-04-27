# Searching a number from a lang class array program with 'bsearch' function in a descending order
def int_cmp(a, b):
    if(a < b):
        return -1
    elif(a > b):
        return 1
    else:
        return 0

def seqbsearch(key, base, size):

    base.append(key)
    ans = size
    for i in range(size):
        res = int_cmp(base[i], key)
        if(res == 0):
            ans = i
            break

    if(ans < size):
        return ans
    else:
        return -1

# Main Function
print("I'm gonna search a key you input in a binary search method.")
print("Number of elements :")
nx = int(input())
ar = []

print("Input a number for specified times.")
for i in range(nx):
    print("x[{0}]".format(i))
    x = int(input())
    ar.append(x)

print("the key")
ky = int(input())

idx = seqbsearch(ky, ar, nx)

if(idx == -1):
    print("Failed Searching '{0}'".format(ky))
else:
    print("{0} is in x[{1}]".format(ky, idx))

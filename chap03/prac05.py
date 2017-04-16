# Advanced Binary Search
def bin_search2(a, n, key):
    pl = 0
    pr = n - 1

    while(pl <= pr):
        pc = int((pl + pr) / 2)
        if(a[pc] == key):
            head = pc
            while(a[head] == key):
                pc = head
                head -= 1
            return pc
        elif(a[pc] < key):
            pl = pc + 1
        else:
            pr = pc - 1
    return -1


# Main Function
print("I'm gonna search a key you input in a binary method")
print("Number of elements :")
nx = int(input())
ar = []

for i in range(nx):
    while(True):
        print("x[{0}] :".format(i))
        x = int(input())
        if(i == 0 or x >= ar[i - 1]):
            ar.append(x)
            break

print("The key :")
ky = int(input())

idx = bin_search2(ar, nx, ky)

if(idx == -1):
    print("Failed Searching '{0}'".format(ky))
else:
    print("{0} is in x[{1}]".format(ky, idx))

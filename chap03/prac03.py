# Return the number of elements that are matched with your input

def search_idx(a, n, key, idx):
    fo = 0
    for i in range(n):
        if(a[i] == key):
            idx.append(i)
            fo += 1
    return fo

# Main Function
print("I'm gonna search a key you input in a linear method")
print("Number of elements :")
nx = int(input())
ar = []
ix = []

for i in range(nx):
    print("x[{0}] :".format(i))
    x = int(input())
    ar.append(x)

print("The key :")
ky = int(input())

ar_num = search_idx(ar, nx, ky, ix)

if(ar_num > 0):
    print(ix)
print("{0} of {1} founded.".format(ky, ar_num))

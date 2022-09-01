n = int(input())
k = 0
s = 3
while n > s:
    k += 1
    s = 2 * s + k + 3

def moo(s, k, n):
    ns = (s - (k + 3)) // 2
    if n <= ns:
        return moo(ns, k - 1, n)
    elif ns < n <= ns + k + 3:
        if n == ns + 1:
            return 'm'
        else:
            return 'o'
    else:
        return moo(ns, k - 1, n - ns - (k + 3))
print(moo(s, k, n))


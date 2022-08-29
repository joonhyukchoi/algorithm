def solution(n, k):
    def checkPrime(num):
        if num == 0 or num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    numstr = ''
    m = n
    while True:
        numstr += str(m % k)
        m = m // k
        if m == 0:
            break
    numlist = numstr[::-1].split('0')
    for i in range(len(numlist)):
        if numlist[i] != '':
            numlist[i] = int(numlist[i])
        else:
            numlist[i] = 0
    count = 0
    for num in numlist:
        if checkPrime(num):
            count += 1
    return count
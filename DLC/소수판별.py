#함수 사용
'''
import math # sqrt

def sieve(n):
    arr = [True] * (n+1)
    arr[0] = False; arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i]:
            j = 2
            while i*j <= n: 
                arr[i*j] = False
                j += 1
    return arr
'''

#반복문 사용
'''
arr = [True for _ in range(100001)]
arr[0] = False
arr[1] = False
for i in range(2,100001):
    if arr[i] == False:
        continue
    for j in range(i * 2, 100001, i):
        arr[j] = False
for i in range(100001):
    if arr[i]: print(i,end=" ")
'''
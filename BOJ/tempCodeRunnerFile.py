from math import sqrt

def check(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

n = int(input())
arr = [int(input()) for _ in range(n)]
for i in arr:
    cnt = i
    while True:
        if check(cnt) == True:
            print(cnt)
            break
        cnt += 1
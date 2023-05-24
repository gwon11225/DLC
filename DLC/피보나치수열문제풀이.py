#첫 번쨰 문제  - 피보나치 수
'''n = int(input())
fibo = [1,1]
for i in range(2,n+1):
    fibo.append(fibo[i-2] + fibo[i-1])
print(fibo[-2])'''

#두 번째 문제 - 피보나치 수 2 (첫 번쨰 문제와 코드 동일)
'''n = int(input())
fibo = [1,1]
for i in range(2,n+1):
    fibo.append(fibo[i-2] + fibo[i-1])
print(fibo[-2])'''

#세 번째 문제 - 피보나치 수 4
'''n = int(input())
if n == 0:
    print(0)
    exit()
fibo = [1,1]
for i in range(2,n+1):
    fibo.append(fibo[i-2] + fibo[i-1])
print(fibo[-2])'''

#네 번째 문제 - 피보나치 비스무리한 수열
'''n = int(input())
fibo = [0,1,1]
for i in range(3,n+1):
    fibo.append(fibo[i-3] + fibo[i-1])
print(fibo[n])'''

#다섯 번째 문제 - 피보나치 수 7
'''fibo_first = 1
fibo_second = 1
fibo = 0
n = int(input())
if n == 1:
    print(1)
    exit()
if n == 2:
    print(1)
    exit()
for i in range(n - 2):
    fibo = fibo_first%1000000007 + fibo_second%1000000007
    fibo_first = fibo_second%1000000007
    fibo_second = fibo%1000000007
print(fibo%1000000007)'''

#다음 부터는 못풀었음
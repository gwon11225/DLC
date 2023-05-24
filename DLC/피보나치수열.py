#for문으로 피보나치 구현하기
'''n = int(input()) # n 번째 피보나치 항을 찾는 프로그램에서 n을 담당
fibo = [1,1] # 피보나치 수열이 저장될 리스트
for i in range(2,n+1): #0번째 항과 첫번쨰 항은 저장이 되어있기 때문에 2번쨰 부터 시작한다
    fibo.append(fibo[i - 2] + fibo[i - 1])
print(fibo[-1])'''
#재귀함수로 피보나치 구현하기
'''def fibo(num: int) -> int:
    if num == 0: # 0 번쨰 피보나치 수를 반환해야 하는 상황
        return 0
    if num == 1: # 1 번째 피보나치 수를 반환해야 하는 상황
        return 1
    return fibo(num - 1) + fibo(num - 2)
n = int(input()) # n번째 피보나치에서 n
print(fibo(n))'''
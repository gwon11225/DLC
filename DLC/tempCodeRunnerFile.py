n = int(input())
a,b = input().split('*')
for i in range(n):
    word = input()
    if len(a) > len(word) or len(b) > len(word):
        print("NE")
        continue
    cnt = 0
    for j in range(len(a)):
        if a[j] == word[j]:
            cnt += 1
    if cnt != len(a):
        print("NE")
        continue
    cnt = 0
    for j in range(len(b)):
        if b[j] == word[len(word) - len(b) + j]:
            cnt += 1
    if cnt != len(b):
        print("NE")
        continue
    print("DA")
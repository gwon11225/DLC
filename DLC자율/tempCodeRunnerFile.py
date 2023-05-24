n = int(input())
arr_1 = list(map(int,input().split()))
m = int(input())
arr_2 = list(map(int,input().split()))
s_1,s_2 = arr_1[0],arr_2[0]
for i in range(1,len(arr_1)):
    s_1 *= arr_1[i]
print(s_1)
for i in range(1,len(arr_2)):
    s_2 *= arr_2[i]
print(s_2)
while s_2:
    s_1,s_2 = s_2,s_1%s_2
s_1 = str(s_1)
if len(s_1) >= 9:
    print(s_1[-9:])
else:
    print(s_1)
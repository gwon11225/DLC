'''
집합을 구현하는 문제(11723)

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 
'''
#직접 구현
'''
import sys

n = int(input())
s = 0b0
for i in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            s = 0b111111111111111111110
        else:
            s = 0b0
    else:
        cmd, x = cmd
        x = int(x)
        if cmd == 'add':
            s |= (1 << x)
        if cmd == 'remove':
            s &= ~(1<<x)
        if cmd == 'check':
            print(1 if s & (1 << x) else 0)
        if cmd == 'toggle':
            s ^= (1 << x)
'''

#셋 자료형 사용 

from sys import stdin
s = set()
for _ in range(int(input())):
    cmd = stdin.readline().rstrip().split()
    if len(cmd) == 1:
        if cmd == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
    else:
        cmd,x = cmd
        x = int(x)
        if cmd == 'add':
            s.add(x)
        if cmd == 'remove':
            s.discard(x)
        if cmd == 'check':
            print(int(x in s))
        if cmd == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
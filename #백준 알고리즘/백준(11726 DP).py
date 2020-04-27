import sys
sys.setrecursionlimit(10000)
#sys.stdin = open('test.txt','rt')

N = int(input())
D = [0]*1001
D[1] = 1
D[2] = 2
for i in range(3,N+1) :
    D[i] = D[i-1] + D[i-2]

print(D[N]%10007)

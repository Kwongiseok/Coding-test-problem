import sys
#sys.stdin = open('test.txt','rt')
input = sys.stdin.readline

N,M,K = map(int,input().split())

for _ in range(K) :
    if N > 2*M :
        N -= 1
    else :
        M -= 1

if N >= 2*M :
    print(M)
else :
    print(N//2)

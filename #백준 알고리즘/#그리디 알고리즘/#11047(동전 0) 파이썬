import sys
#sys.stdin = open('test.txt','rt')
input = sys.stdin.readline

N , K = map(int,input().split())
coin = []
cnt = 0

for _ in range(N) :
    t = int(input())
    coin.append(t)

for i in range(N-1,-1,-1) :
    if coin[i] <= K :
        tmp = K // coin[i]
        cnt += tmp
        K = K - tmp*coin[i]
        if K == 0 :
            print(cnt)
            break
    else :
        continue

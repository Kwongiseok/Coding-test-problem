import sys
#sys.stdin = open('test.txt','rt')
input = sys.stdin.readline

T = int(input())
list_tmp = []
for i in range(T) :
    N = int(input())
    cnt = 0
    list_tmp =[]
    for _ in range(N) :
        list_tmp.append(tuple(map(int,input().split())))
    list_tmp.sort()
    Top_rank = list_tmp[0][1]
    for j in range(N) :
        if list_tmp[j][1] > Top_rank :
            cnt+=1
        else :
            Top_rank = list_tmp[j][1]
            
    print(N-cnt)

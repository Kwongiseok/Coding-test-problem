import sys
#sys.stdin = open('test.txt','rt')
input = sys.stdin.readline
accumulate = 0
N = int(input())
arr = list(map(int,input().split()))
answer = []
arr.sort()
for i in arr :
    accumulate += i
    answer.append(accumulate)
print(sum(answer))

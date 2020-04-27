import sys
sys.setrecursionlimit(10000)
#sys.stdin = open('test.txt','rt')

N = int(input())
list_rgb = []
for i in range(N) :
    R,G,B = map(int,sys.stdin.readline().split())
    list_rgb.append([R,G,B])

for i in range(1,N) :
    list_rgb[i][0] = min(list_rgb[i-1][1],list_rgb[i-1][2]) + list_rgb[i][0]
    list_rgb[i][1] = min(list_rgb[i-1][0],list_rgb[i-1][2]) + list_rgb[i][1]
    list_rgb[i][2] = min(list_rgb[i-1][0],list_rgb[i-1][1]) + list_rgb[i][2]

p = min(list_rgb[N-1][0],list_rgb[N-1][1],list_rgb[N-1][2])
print(p)

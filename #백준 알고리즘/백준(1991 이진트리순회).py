import sys
sys.setrecursionlimit(10000)
#sys.stdin = open('test.txt','rt')

def preorder(tmp) :
    if tmp!='.' :
        print(tmp,end='')
        preorder(node[tmp][0])
        preorder(node[tmp][1])
    else :
        return
def inorder(tmp) :
    if tmp!='.' :
        inorder(node[tmp][0])
        print(tmp,end='')
        inorder(node[tmp][1])
    else :
        return
def postorder(tmp) :
    if tmp!='.' :
        postorder(node[tmp][0])
        postorder(node[tmp][1])
        print(tmp,end='')
    else :
        return
N = int(input())
node = {}
for i in range(N) :
    key,node1,node2 = sys.stdin.readline().rstrip().split()
    node[key] = (node1,node2)
preorder('A')
print()
inorder('A')
print()
postorder('A')

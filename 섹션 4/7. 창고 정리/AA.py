import sys

#sys.stdin=open("input.txt","rt")
L=int(input())
boxes=list(map(int,input().split()))

M=int(input())
cnt=0

while cnt<M:
    boxes.sort()
    boxes[0]+=1
    boxes[-1]-=1
    cnt+=1

print(max(boxes)-min(boxes))

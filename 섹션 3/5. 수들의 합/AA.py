import sys
#sys.stdin=open("input.txt","rt")
N,M=map(int,input().split())
nums=list(map(int,input().split()))
cnt=0

left=0
right=1
total=nums[left]
while True:
    if total==M:
        cnt+=1
        total-=nums[left]
        left+=1
    elif total<M:
        if right<N:
            total+=nums[right]
            right+=1
        else:
            break
    else:
        total-=nums[left]
        left+=1



print(cnt)
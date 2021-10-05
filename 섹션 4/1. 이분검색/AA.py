import sys
#sys.stdin=open("input.txt","rt")
N,M=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
lt=0
rt=N-1
while True:
    mid=(lt+rt)//2
    if nums[mid]==M:
        print(mid+1)
        break
    elif nums[mid]>M:
        rt=mid-1
    else:
        lt=mid+1



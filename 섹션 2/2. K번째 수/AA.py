import sys
#sys.stdin=open("input.txt","rt")
T=int(input())
for i in range(1,T+1):
    n,s,e,k=map(int,input().split())
    nums=list(map(int,input().split()))
    nums=nums[s-1:e]
    nums.sort()
    print('#%d %d' %(i,nums[k-1]))


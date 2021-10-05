import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
nums=list(map(int,input().split()))
def digit_sum(x):
    x=str(x)
    sum=0
    for i in x:
        i=int(i)
        sum+=i
    return sum

max_result=0
max_sum=nums[0]
for i in nums:

    result=digit_sum(i)
    if max_result<result:
        max_result=result
        max_sum=i

print(max_sum)
import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
nums=[]
result=0
max_result=0
for i in range(N):
    row=list(map(int,input().split()))
    result=sum(row)
    max_result=max(result,max_result)
    nums.append(row)
#대각선
result1=0
result2=0
for i in range(N):
    result1+=nums[i][i]
    result2+=nums[i][N-1-i]
    max_result2=max(result2,result1)
result3=0
max_result3=0
for i in range(0,len(nums)):
    result3=0
    for j in range(0,len(nums)):
        result3+=nums[j][i]
        max_result3=max(result3,max_result3)
ans=max(max_result,max_result2,max_result3)
print(ans)
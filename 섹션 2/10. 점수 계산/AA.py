import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
wrong_flag=0
score=list(map(int,input().split()))
result=0
total=0
for i in score:
    if i==0:
        wrong_flag=1
    if i==1:
        if wrong_flag==1:
            result=1
            wrong_flag=0
        else:
            result+=1
        total+=result

print(total)






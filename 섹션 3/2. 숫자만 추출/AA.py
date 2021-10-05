import sys
#sys.stdin=open("input.txt","rt")
str=input()
result=[]
for i in str:
    if i.isdigit():
        result.append(i)
while result:
    if result[0]=='0':
        result.pop(0)
    else:
        break
answer=''
#print(result)
for i in range(0,len(result)):
    answer=answer+result[i]
    print(result[i],end='')
print()
cnt=0

for i in range(1,int(answer)+1):
    if int(answer)%i==0:
        cnt+=1
print(cnt)



import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
nums=list(map(int,input().split()))

def reverse(x):
    answer=''
    while x>0:
        ans=x%10
        answer+=str(ans)
        x=x//10

    return int(answer)

def isPrime(x):
    ch=[0]*(x+1)
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False

    return True

for i in nums:
    reverse_num=reverse(i)
    reverse_num=str(reverse_num)
    #print(reverse_num)
    if reverse_num[0]=='0':
        while reverse_num[0]!='0':
            reverse_num=reverse_num[1:]
            #print(reverse_num)
    if isPrime(int(reverse_num)):
        print(int(reverse_num),end=' ')




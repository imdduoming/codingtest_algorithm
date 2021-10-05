import sys
#sys.stdin=open("input.txt","rt")
N=int(input())
ch=[0]*(N+1)
#def find_prime(x): #에라토스테네스의 채
cnt=0
for i in range(2,N+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i,N+1,i):
            ch[j]=1
print(cnt)
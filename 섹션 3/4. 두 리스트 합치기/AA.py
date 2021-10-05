import sys
#sys.stdin=open("input.txt","rt")
N=input()
arr1=list(map(int,input().split()))
N=input()
arr2=list(map(int,input().split()))
arr3=arr1+arr2
arr3.sort()
arr3=[str(i) for i in arr3]
print(' '.join(arr3))

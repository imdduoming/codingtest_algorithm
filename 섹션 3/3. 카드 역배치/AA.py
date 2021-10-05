import sys
#sys.stdin=open("input.txt","rt")
card=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(10):
    start,end=map(int,input().split())

    if start==1 :
        card=card[end-1:0:-1]+[card[0]]+card[end:]
    else:
        card = card[0:start - 1] + card[end - 1:start - 2:-1] + card[end:]


    #print('i:',i,'card:',card)
card=[str(i) for i in card]
print(' '.join(card))
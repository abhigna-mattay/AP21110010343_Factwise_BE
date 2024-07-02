# maximum score by picking cards

cardPoints=list(map(int,input().split()))
k=int(input())
score=0
if len(cardPoints)==k:
    score=sum(cardPoints)
else:
    for turn in range(k):
        n=len(cardPoints)
        if n==0:
            break
        fnum=cardPoints[0]
        lnum=cardPoints[n-1]
        
        if fnum==lnum and n>=4:
            # if first and last are equal then we choose based on the next of first and previous of last
            if cardPoints[n-2]>cardPoints[1]:
                score+=lnum
                cardPoints.pop()
            elif cardPoints[n-2]<cardPoints[1]:
                score+=fnum
                cardPoints.pop(0)
            else:
                score+=lnum
                cardPoints.pop()
        else:
            # if first and last are not equal we decide based on maximum of first and last
            if fnum>lnum:
                score+=fnum
                cardPoints.pop(1)
            elif fnum<lnum:
                score+=lnum
                cardPoints.pop()
                
print("Maximum score possible is : ",score)
                
                

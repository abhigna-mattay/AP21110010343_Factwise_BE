# counting number of letters to write one to thousand 

#define no. of letters for most occuring words inside a dictionary
d={'and':3,'1':3,'2':3,'3':5,'4':4,'5':4,'6':3,'7':5,'8':5,'9':4,'10':3,'100':7,'20':6,'30':6,'40':5,'50':5,'60':5,'70':7,'80':7,'90':6,'1000':11}
letters=0 #initializing letters needed as 0
for i in range(1,1001):
    number=str(i)
    n=len(number)
    if number in d.keys():
        letters+=d[number]
    
    else:
        if n==2: #for 2-digit numbers other than 10,20,30,....,90
            tp=int(number[0])
            letters+=(d[str(tp*10)]+d[number[1]])
        elif n==3: #for 3-digit numbers
            if number[1]=='0' and number[2]=='0': # all multiples of 100 from 100,200,....,900 
                letters+=(d[number[0]]+d['100'])
            elif number[2]=='0' and number[1]!='0': # all three digit numbers ending with 0 like 110,120,130,...,190,...,910,920,...,990
                tp=int(number[1])
                letters+=(d[number[0]]+d['100']+d[str(tp*10)]+d['and'])
            elif number[2]!='0' and number[1]=='0': # all three digit numbers with 0 as middle digit like 101,102,...109,...,901,902,...909
                letters+=(d[number[0]]+d['100']+d['and']+d[number[2]])
            elif number[2]!='0' and number[1]!=0: #all three digit numbers with none of the digits equal to zero like 332
                tp=int(number[1])
                letters+=(d[number[0]]+d['100']+d[str(tp*10)]+d['and']+d[number[2]])

# printing no. of letters needed for 1 to 1000
print("Number of letters needed for 1 to 1000 numbers : ",letters)
                
    


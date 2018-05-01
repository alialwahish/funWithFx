def oddEve(num):
    if num %2!=0:
        return "an odd number"
    elif num %2==0:
        return "an even number"

for i in range(1,10):
    print "number is", i , "this is a",oddEve(i)
a = [2,4,10,16]

def multiply(liA,num):
    liB=[i*5 for i in liA]
    return liB



def layerdMultip(fxLi):
    compLi=[]
    newLi=[]
    for i in fxLi:
        for d in range(0,i):
            newLi.append(1)
        compLi.append(newLi)
        newLi=[]
        
    return(compLi)
    

x=layerdMultip(multiply([2,4,5],3))
print(multiply(a,5))
print(x)

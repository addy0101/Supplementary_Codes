a  = int(input('Number: '))
import numpy as np
#a =128
b=[]
i=2
c=a
while(i<np.sqrt(a) and c>=2):
    if(c%i == 0):
        print(i,c)
        c=int(c/i)
        b.append(i)

    else:
        i+=1

#print(c)
b.append(c)
print(b)

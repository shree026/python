#! /usr/bin/python3
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
L1=[]
L2=[]
for i in adhoc:
    if int(i)>5:
        L1.append(i)


    elif int(i)<=2:
        L2.append(i)

print("list of numbers which are greater then 5: "+str(L1))
print("list of numbers which are less than equal to 2 :"+str(L2))
